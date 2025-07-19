'''
2025-07-16
Author: Dan Schumacher
How to run:
   python .\src\lessons\iteration\while.py
'''

# grab our time tool box. 
import time

def main():
    print("Volunteer 1: You are myNum. You start at 1.")
    myNum = 1
    hand_raised = input("Volunteer 2: Is your hand raised? (yes/no): ").lower()

    while hand_raised == 'yes':
        myNum = myNum + 1
        print("myNum is now:", myNum)
        time.sleep(1)  # wait 1 second
        hand_raised = input("Volunteer 2: Is your hand still raised? (yes/no): ").lower()

    print("Volunteer 2 put hand down!")
    print("What is myNum? It is:", myNum)

if __name__ == "__main__":
    main()