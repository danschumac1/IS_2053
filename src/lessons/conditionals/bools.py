'''
2025-07-16
Author: Dan Schumacher
How to run:
   python .\src\lessons\conditionals\\bools.py
'''

def main():
    # Booleans: True or False based on conditions
    x = 3
    y = 5
    z = x  # z points to the same value as x

    print("x == y:", x == y)          # is equal to
    print("x != y:", x != y)          # is not equal to
    print("x < y:", x < y)            # less than
    print("x > y:", x > y)            # greater than
    print("x <= y:", x <= y)          # less than or equal to
    print("x is z:", x is z)          # is the same object
    print("x is not y:", x is not y)  # is not the same object
    
if __name__ == "__main__":
    main()