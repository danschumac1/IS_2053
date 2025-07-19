'''
2025-07-19
Author: Dan Schumacher
How to run:
   python .\src\lessons\try_except\rec_syntax.py
'''

import json

def main():
    try:
        my_number = 8 / 0
        print("I figured out how to devide by zero!")
    except ValueError as e:
        print("This is actually impossible!")
        print("Error: ", e)


if __name__ == "__main__":
    main()