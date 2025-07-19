'''
2025-07-16
Author: Dan Schumacher
How to run:
   python .\src\lessons\conditionals\\else.py
'''

def main():
    # 1 - Glasses
    wearing_glasses = True
    if wearing_glasses:
        print("NICE GLASSES!")
    else:
        print("NO GLASSES!")

    # 2 - Number on board
    number_on_board = 4
    if number_on_board % 2 == 0:
        print("EVEN!")
    else:
        print("ODD!")

    # 3 - Lights
    lights_on = False
    if lights_on:
        print("BRIGHT!")
    else:
        print("dark...")

    # 4 - Standing
    is_standing = True
    if is_standing:
        print("UP!")
    else:
        print("DOWN!")

if __name__ == "__main__":
    main()
