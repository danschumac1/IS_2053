'''
2025-07-16
Author: Dan Schumacher
How to run:
   python .\src\lessons\conditionals\elif.py
'''

def main():
    # 1 - Number size check
    number = 8
    if number < 3:
        print("Small!")
    elif number < 7:
        print("Medium!")
    else:
        print("Large!")

if __name__ == "__main__":
    main()
