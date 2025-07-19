'''
2025-07-19
Author: Dan Schumacher
How to run:
   python .\src\lessons\try_except\do_these_crash.py
'''

import json

def main():
    
    try:
        8 / 0
    except:
        print("I can't divide by zero!")
    
    if 8 / 0 == 0:
        print("success!")
    
    try:
        my_formula = 8 / 0
    except:
        print(f"{my_formula} is impossible")



if __name__ == "__main__":
    main()