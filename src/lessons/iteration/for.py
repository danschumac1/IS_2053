'''
2025-07-16
Author: Dan Schumacher
How to run:
   python .\src\lessons\iteration\\for.py
'''

def main():
    print("Volunteer 1: You are myNum. You start at 1.")
    myNum = 1
    num_students = 5
    
    for i in range(num_students):
        response = input(f"Student {i+1}: Raise your hand? (yes/no): ").lower()
        if response == 'yes':
            myNum = myNum + 1
            print(f"Student {i+1} raised hand! myNum is now: {myNum}")
        else:
            print(f"Student {i+1} did not raise hand.")

    print("What is myNum? It is:", myNum)

if __name__ == "__main__":
    main()
