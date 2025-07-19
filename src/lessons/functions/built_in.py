'''
2025-07-16
Author: Dan Schumacher
How to run:
   python .\src\lessons\\functions\\built_in.py
'''

import json

def main():
    message = "hello"
    print(len(message))    # how many characters?

    number = 3.14
    print(type(number))    # what type?

    text_num = "42"
    print(int(text_num))   # convert string to int

    num = 7
    print(str(num))        # convert number to string

if __name__ == "__main__":
    main()