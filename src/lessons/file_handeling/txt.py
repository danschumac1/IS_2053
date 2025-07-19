'''
2025-07-18
Author: Dan Schumacher
How to run:
    python .\src/lessons\\file_handeling\\txt.py
'''
import csv
import json

def read_text_file(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def write_text_file(file_path: str, content: str):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def append_text_file(file_path: str, content: str):
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(content)

def main():
    my_path = './data/file_handeling/cat_in_the_hat.txt'
    my_text = read_text_file(my_path)
    print(f"Context from {my_path}: {my_text}")
    write_text_file('./data/output.txt', 'Hello, world!')
    append_text_file('./data/output.txt', '\nAnother line.')

if __name__ == "__main__":
    main()
