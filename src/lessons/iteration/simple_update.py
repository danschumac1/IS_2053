'''
2025-07-16
Author: Dan Schumacher
How to run:
   python .\src\lessons\iteration\simple_update.py
'''

def main():
    x = 2
    print("first value:", x)

    # just write over it
    x = 45
    print("second value:", x)

    x = x + 2
    print("third value:", x)

    # reset it 
    x = 45
    x += 2 # this is equivalent to `x = x + 2`
    print("fourth value:", x)

    x = x * 2
    print("fifth value:", x)

if __name__ == "__main__":
    main()