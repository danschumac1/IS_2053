'''
2025-07-16
Author: Dan Schumacher
How to run:
   python .\src\lessons\conditionals\\logical_operators.py
'''

def main():
    # Conditions
    is_tall = False
    has_brown_hair = True

    print("I am tall and have brown hair:", is_tall and has_brown_hair)
    print("I am tall or have brown hair:", is_tall or has_brown_hair)
    print("I am not tall and have brown hair:", (not is_tall) and has_brown_hair)

    # Hard: Remember PEMDAS - parentheses first!
    print("not (I am tall and have brown hair):", not (is_tall and has_brown_hair))


if __name__ == "__main__":
    main()
