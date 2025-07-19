'''
2025-07-18
Author: Dan Schumacher
How to run:
   python .\src\lessons\\file_handeling\jsonl.py
'''

import json

def read_jsonl_file(file_path: str) -> list:
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            data.append(json.loads(line))
    return data

def write_jsonl_file(file_path: str, data: list):
    with open(file_path, 'w', encoding='utf-8') as file:
        for item in data:
            file.write(json.dumps(item) + '\n')

def append_jsonl_file(file_path: str, data: list):
    with open(file_path, 'a', encoding='utf-8') as file:
        for item in data:
            file.write(json.dumps(item) + '\n')

def main():
    jsonl_data = [{"name": "Charlie", "age": 35}]
    write_jsonl_file('./data/output.jsonl', jsonl_data)
    append_jsonl_file('./data/output.jsonl', [{"name": "Dana", "age": 40}])

if __name__ == "__main__":
    main()
