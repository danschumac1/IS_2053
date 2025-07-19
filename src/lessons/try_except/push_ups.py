'''
2025-07-19
Author: Dan Schumacher
How to run:
   python .\src\lessons\try_except\push_ups.py
'''

import json

def main():
    some_task = ... # do 50 pushups
    some_failure_task = ... # cry yourself to sleep
    try:
        some_task
        print("I'm the best!")
    except:
        print("I gotta train harder!")
        some_failure_task

if __name__ == "__main__":
    main()



