'''
2025-03-09
Author: Dan Schumacher
How to run:
   python ./src/utils/prompter.py
'''
import base64
import os
import importlib
import json
from typing import List, Dict, Optional, Tuple, Type, Union
from abc import ABC, abstractmethod
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
from pydantic import BaseModel
import yaml
from dotenv import load_dotenv
import torch
torch.cuda.empty_cache()
import re
from json_repair import repair_json

import openai
from transformers import (
    AutoTokenizer, 
    BitsAndBytesConfig, 
    AutoModelForCausalLM, 
    Gemma3ForConditionalGeneration, 
    AutoProcessor,
    # pipeline
    )

from utils.logging_utils import MasterLogger

def normalize_device_map(device_map):
    if isinstance(device_map, list):
        if len(device_map) == 1:
            return {"": device_map[0]}
        else:
            return "auto"
    elif isinstance(device_map, int):
        return {"": device_map}
    elif isinstance(device_map, str) and device_map.isdigit():
        return {"": int(device_map)}
    elif isinstance(device_map, dict):
        return device_map
    else:
        raise ValueError("device_map must be int, list of ints, 'auto', or dict")


class QAs(BaseModel):
    question: Dict[str, str]  # Multiple inputs as a dictionary
    answer: Union[BaseModel, str]   # Allow both strings and BaseModel

class Prompter(ABC):
    def __init__(
        self,
        prompt_path: Optional[str],
        prompt_headers: Dict[str, str],
        llm_model: str = "gpt-4o-mini",
        temperature: float = 0.1,
        show_prompt: bool = True,
        device_map: int = 0,  # Default to GPU0
        repeition_penalty: float = 1.1
    ):
        self.llm_model = llm_model
        self.prompt_path = prompt_path
        self.prompt_headers = prompt_headers
        self.temperature = temperature
        self.first_print = True
        self.show_prompt = show_prompt
        self.device_map = device_map
        self.repeition_penalty = repeition_penalty
        (
            self.output_format_class,
            self.examples,
            self.system_prompt,
            self.main_prompt_header,
            self.prompt_headers,
            self.is_structured_output  # ← add this line
        ) = self._load_yaml_examples_with_model()

        self.format_examples()


    def __repr__(self) -> str:
        return f"Prompter(model={self.llm_model}, examples={len(self.examples)})"

    def _load_yaml_examples_with_model(self) -> Tuple[Type[BaseModel], List[QAs], str, str, Dict[str, str], bool]:
        with open(self.prompt_path, "r") as f:
            raw = yaml.safe_load(f)

        meta = raw.get("__meta__", {})
        model_path = meta.get("output_model")
        if not model_path:
            raise ValueError("YAML file must contain __meta__.output_model")

        unstructured_aliases = {"simple_string", "string", "str"}
        if model_path in unstructured_aliases:
            model_class = str
            is_structured = False
        else:
            try:
                module_name, class_name = model_path.rsplit(".", 1)
                model_module = importlib.import_module(module_name)
                model_class = getattr(model_module, class_name)
                is_structured = True
            except (ValueError, ImportError, AttributeError) as e:
                raise ImportError(
                    f"Could not load output_model '{model_path}'. Either:\n"
                    f"  - Use one of: {unstructured_aliases}, or\n"
                    f"  - Provide a valid import path like 'my_module.MyModelClass'\n"
                    f"Full error: {e}"
                )

        system_prompt = raw.get("system_prompt", "You are a helpful assistant.")
        main_prompt_header = raw.get("main_prompt_header", "")
        prompt_headers = raw.get("prompt_headers", {})
        # print(raw.get("examples", []))
        examples = [
            QAs(
                question=ex["input"], 
                answer=model_class(**ex["output"]) if is_structured else ex["output"])
            for ex in raw.get("examples", [])
        ]

        return model_class, examples, system_prompt, main_prompt_header, prompt_headers, is_structured

    def format_q_as_string(self, question_dict: Dict[str, str]) -> str:
        """Formats multiple question fields for the LLM"""
        formatted_questions = "\n\n".join(
            f"{self.prompt_headers.get(key, key).upper()}: {value}" for key, value in question_dict.items()
        )

        if self.is_structured_output:
            prompt = (
                f"{formatted_questions}\n"
                f"Provide your response in JSON format using the schema below:\n"
                f"{self.output_format_class.model_json_schema()}\n"
                f"Do not include any extra text, explanations, or comments outside the JSON object."
            )
        else:
            prompt = (
                f"{formatted_questions}\n"
                f"Answer the question clearly and concisely. Do not include explanations unless asked."
            )

        return prompt

    def format_examples(self):
        """Formats few-shot examples by prepending prompt headers"""
        for qa in self.examples:
            qa.question = self.format_q_as_string(qa.question)
            if isinstance(qa.answer, BaseModel):
                qa.answer = qa.answer.model_dump_json()

    @abstractmethod
    def parse_output(self, llm_output: str):
        """Extract response-text from the LLM output"""
        pass

    @abstractmethod
    def get_completion(self, user_inputs: Dict[str, str]) -> str:
        """Send the prompt to the LLM and get a response"""
        pass

# === OpenAI Implementation ===
class OpenAIPrompter(Prompter):
    def __init__(self, llm_model="gpt-4o-mini", **kwargs):
        super().__init__(**kwargs)
        self.client = openai.Client(api_key=self._load_env())

    def _load_env(self) -> str:
        """Loads API key from .env"""
        load_dotenv("./resources/.env")
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError(f"API Key not found. Set OPENAI_API_KEY=xxxx in ./resources/.env")
        return api_key
    
    def parse_output(self, llm_output) -> Union[str, dict]:
        """Parses LLM output based on structured/unstructured mode"""
        content = llm_output.choices[0].message.content.strip()

        if self.is_structured_output:
            try:
                content = repair_json(content, return_objects=True)
                return content
            except json.JSONDecodeError:
                raise ValueError(f"Expected JSON but got invalid response:\n{content}")
        else:
            return content  # raw string
        
    def add_image(self, input_dict: Dict[str, str], image_path: str):
        with open(image_path, "rb") as img:
            base64_img = base64.b64encode(img.read()).decode("utf-8")
        input_dict["__image__"] = f"data:image/png;base64,{base64_img}"


    def _build_messages(self, input_texts: Dict[str, str]):
        """Builds the messages list for the OpenAI API with few-shot examples and the final input."""
        messages = [{"role": "system", "content": self.system_prompt}]

        # Add few-shot examples (already pre-formatted)
        for qa in self.examples:
            messages.append(
                {"role": "user", "content": f"{self.main_prompt_header}\n{qa.question}"}
            )
            messages.append(
                {"role": "assistant", "content": qa.answer}
            )

        # Format final user input
        user_input_prompt = self.format_q_as_string(input_texts)
        if "__image__" in input_texts:
            messages.append({
                "role": "user",
                "content": [
                    {"type": "text", "text": user_input_prompt},
                    {"type": "image_url", "image_url": {"url": input_texts["__image__"]}}
                ]
            })
        else:
            messages.append({"role": "user", "content": f"{self.main_prompt_header}\n{user_input_prompt}"})


        if self.show_prompt and self.first_print:
            self.first_print = False
            print("=" * 50)
            print("=" * 17, "EXAMPLE PROMPT", "=" * 17)
            print(json.dumps(messages, indent=4))
            print("=" * 50)

        return messages

    def get_completion(
            self, input_texts: Dict[str, str], parse=True, verbose=False) -> Union[dict, None]:
        """Calls OpenAI API with multiple formatted inputs"""
        input_text_str = self._build_messages(input_texts)
        completion_kwargs = {
            "model": self.llm_model,
            "messages": input_text_str,
            "temperature": self.temperature,
        }

        if self.is_structured_output:
            completion_kwargs["response_format"] = {"type": "json_object"}

        response = self.client.chat.completions.create(**completion_kwargs)


        final_resp = self.parse_output(response) if parse else response

        if verbose:
            print("\n" + "="*60)
            print("OUTPUT FROM LLM:")
            print(json.dumps(final_resp, indent=4))
            print("="*60 + "\n")

        return final_resp
    
    def batch_generate(
        self,
        inputs: List[Dict[str, str]],
        max_workers: int = 10,
        verbose: bool = False,
        sleep_between: float = 0.0
    ) -> List[Union[str, dict]]:
        """
        Concurrently generate completions for a list of inputs using ThreadPoolExecutor.
        
        Args:
            inputs (List[Dict[str, str]]): List of user inputs.
            max_workers (int): Max number of parallel requests.
            verbose (bool): Print LLM responses.
            sleep_between (float): Seconds to wait between launching requests (to avoid bursts).

        Returns:
            List[Union[str, dict]]: Parsed completions.
        """
        results = [None] * len(inputs)

        def task(i, input_data):
            if sleep_between > 0:
                time.sleep(sleep_between)
            try:
                result = self.get_completion(input_data, parse=True, verbose=verbose)
                return i, result
            except Exception as e:
                return i, {"error": str(e)}

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [executor.submit(task, i, inputs[i]) for i in range(len(inputs))]
            for future in as_completed(futures):
                i, output = future.result()
                results[i] = output

        return results

class HFPrompter(Prompter):
    def __init__(
        self,
        llm_model: str,
        model=None,                # <- New: shared model instance
        tokenizer=None,            # <- New: shared tokenizer
        max_new_tokens: int = 2000,
        temperature: float = 0.1,
        quantize: bool = False,
        device_map: Union[int, List[int], dict, str] = 0,
        torch_dtype=torch.float16,
        **kwargs, 
    ):
        super().__init__(llm_model=llm_model, temperature=temperature, **kwargs)

        self.max_new_tokens = max_new_tokens
        self.first_print = True

        if model is not None and tokenizer is not None:
            self.model = model
            self.tokenizer = tokenizer
            self.tokenizer.pad_token = self.tokenizer.eos_token
            return  # Exit init early if sharing

        model_kwargs = {
            "device_map": normalize_device_map(device_map),
            "torch_dtype": torch_dtype
        }

        if quantize:
            model_kwargs["quantization_config"] = BitsAndBytesConfig(
                load_in_8bit=True,
                bnb_4bit_compute_dtype=torch.float16
            )

        self.tokenizer = AutoTokenizer.from_pretrained(llm_model)
        self.tokenizer.pad_token = self.tokenizer.eos_token
        self.model = AutoModelForCausalLM.from_pretrained(llm_model, **model_kwargs)


    def parse_output(self, llm_output) -> Union[str, dict]:
        """Parses LLM output based on structured/unstructured mode"""
        
        content = llm_output.strip()

        if not self.is_structured_output:
            return content

        # Extract first JSON-like block
        match = re.search(r"\{.*", content, re.DOTALL)
        if not match:
            raise ValueError(f"Could not find a JSON object in output:\n{content}")
        
        json_candidate = match.group(0)

        try:
            return repair_json(json_candidate, return_objects=True)
        except Exception as e:
            raise ValueError(f"Output could not be repaired to valid JSON:\n{json_candidate}\nError: {e}")



    def _build_messages(self, input_texts: Dict[str, str]) -> List[Dict[str, str]]:
        messages = [{"role": "system", "content": self.system_prompt}]
        for qa in self.examples:
            messages.append({"role": "user", "content": f"{self.main_prompt_header}\n{qa.question}"})
            messages.append({"role": "assistant", "content": qa.answer})
        final_prompt = self.format_q_as_string(input_texts)
        messages.append({"role": "user", "content": f"{self.main_prompt_header}\n{final_prompt}"})

        if self.first_print:
            self.first_print = False
            print("=" * 50)
            print("=" * 17, "EXAMPLE PROMPT", "=" * 17)
            print(json.dumps(messages, indent=4))
            print("=" * 50)

        return messages

    def get_completion(
            self, 
            input_texts: Union[Dict[str, str],List[Dict[str, str]]], 
            parse=True
            ) -> Union[dict, List[dict], str]:
        if isinstance(input_texts, dict):
            input_texts = [input_texts]

        messages_list = [self._build_messages(item) for item in input_texts]

        prompts = [
            self.tokenizer.apply_chat_template(m, add_generation_prompt=True, tokenize=False)
            for m in messages_list
        ]

        inputs = self.tokenizer(prompts, return_tensors="pt", padding=True, truncation=True)
        input_ids = inputs["input_ids"].to(self.model.device)
        attention_mask = inputs["attention_mask"].to(self.model.device)

        outputs = self.model.generate(
            input_ids=input_ids,
            attention_mask=attention_mask,
            max_new_tokens=self.max_new_tokens,
            repetition_penalty=self.repeition_penalty,
            return_dict_in_generate=True,
            pad_token_id=self.tokenizer.eos_token_id,
        )

        generated_sequences = outputs.sequences
        results = []
        for i in range(len(generated_sequences)):
            input_len = (input_ids[i] != self.tokenizer.pad_token_id).sum().item()
            gen_tokens = generated_sequences[i][input_len:]
            decoded = self.tokenizer.decode(gen_tokens, skip_special_tokens=True)
            results.append(self.parse_output(decoded) if parse else decoded)

        return results[0] if len(results) == 1 else results

class GemmaPrompter(Prompter):
    def __init__(
        self,
        llm_model: str = "google/gemma-3-12b-it",
        model=None,                # NEW: shared model
        processor=None,            # NEW: shared processor
        max_new_tokens: int = 2000,
        temperature: float = 0.1,
        device_map: Union[int, List[int], dict, str] = 0,
        torch_dtype=torch.bfloat16,
        **kwargs,
    ): 
        torch.backends.cuda.enable_mem_efficient_sdp(False)
        torch.backends.cuda.enable_flash_sdp(False)
        torch.backends.cuda.enable_math_sdp(True)

        super().__init__(llm_model=llm_model, temperature=temperature, **kwargs)

        self.max_new_tokens = max_new_tokens
        self.temperature = temperature

        if model is not None and processor is not None:
            self.model = model
            self.processor = processor
            print(f"MODEL ON: {self.model.device}")
            return  # ✅ Shared model loaded

        self.processor = AutoProcessor.from_pretrained(llm_model)
        device_map = normalize_device_map(device_map)

        self.model = Gemma3ForConditionalGeneration.from_pretrained(
            llm_model,
            device_map=device_map,
            torch_dtype=torch_dtype,
        )
        print(f"MODEL ON: {self.model.device}")

    def _build_messages(self, input_texts: Dict[str, str]) -> List[Dict[str, Union[str, List[Dict[str, str]]]]]:
        """
        Builds a message list compatible with Gemma 3's chat template.
        """
        messages = []

        # Add system message
        messages.append({
            "role": "system",
            "content": [{"type": "text", "text": self.system_prompt}]
        })

        # Add few-shot examples (if any)
        for example in self.examples:
            messages.append({
                "role": "user",
                "content": [{"type": "text", "text": example.question}]
            })
            messages.append({
                "role": "assistant",
                "content": [{"type": "text", "text": example.answer}]
            })

        # Add actual user question
        user_input = self.format_q_as_string(input_texts)
        messages.append({
            "role": "user",
            "content": [{"type": "text", "text": user_input}]
        })

        return messages
    
    def parse_output(self, generated_text: str) -> Union[str, dict]:
        """
        Parses the generated text output. Repairs JSON if structured output is expected.
        """
        cleaned = generated_text.strip().split("<|file_separator|>")[0].strip()

        if not self.is_structured_output:
            return cleaned

        # Extract first JSON-like block
        match = re.search(r"\{.*", cleaned, re.DOTALL)
        if not match:
            raise ValueError(f"Could not find a JSON object in output:\n{cleaned}")

        json_candidate = match.group(0)

        try:
            return repair_json(json_candidate, return_objects=True)
        except Exception as e:
            raise ValueError(f"Output could not be repaired to valid JSON:\n{json_candidate}\nError: {e}")

    
    def get_completion(
        self,
        input_texts: Union[Dict[str, str], List[Dict[str, str]]],
        parse: bool = True
    ) -> Union[dict, List[dict], str]:
        if isinstance(input_texts, dict):
            input_texts = [input_texts]

        results = []
        for input_entry in input_texts:
            messages = self._build_messages(input_entry)

            # Apply chat template and tokenize
            inputs = self.processor.apply_chat_template(
                messages,
                add_generation_prompt=True,
                tokenize=True,
                return_dict=True,
                return_tensors="pt",
                # padding=True,
                # padding_side="right",
                # truncation=True,
            ).to(self.model.device, dtype=self.model.dtype)
            input_len = inputs["input_ids"].shape[-1]

            # Run model generation
            with torch.inference_mode():
                generation = self.model.generate(
                    **inputs,
                    max_new_tokens=self.max_new_tokens,
                    do_sample=True,
                    temperature=self.temperature,
                    top_p=0.95,
                    top_k=50,
                )
                # Remove the input portion from the output
                generation = generation[0][input_len:]

            decoded = self.processor.decode(generation, skip_special_tokens=True)
            parsed = self.parse_output(decoded) if parse else decoded
            results.append(parsed)

        return results[0] if len(results) == 1 else results
