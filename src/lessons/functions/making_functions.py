'''
2025-07-16
Author: Dan Schumacher
How to run:
   python .\src\lessons\functions\making_functions.py
'''

import json

# Void function: just prints
def burp():
    print("burp")

# Void function: prints 'burp' n times
def burp_ntimes(n: int):
    print("burp " * n)

# Void function: default n=6
def burp_ntimes6(n: int = 6):
    print("burp " * n)

# Void function: belch or burp
def belch_or_burp(n: int = 6, belch: bool = True):
    if belch:
        print("belch " * n)
    else:
        print("burp " * n)

# Return function: returns "burp" string
def burp_return() -> str:
    return "burp"

# Return function: returns the sound repeated
def belch_or_burp_return(n: int = 6, belch: bool = True) -> str:
    if belch:
        sound = "belch " * n
    else:
        sound = "burp " * n
    return sound

def main():
    # Void function calls
    # what makes these void?
    burp()

    burp_ntimes(n=3)
    burp_ntimes(3)

    # what would happen if I ran below?
    # burp_ntimes()

    burp_ntimes6()

    # what would happen if I ran below?
    # burp_ntimes6(n=7)

    # notice that we don't have to put n=4, just 4
    # that's because 4 is in the first slot of our function
    belch_or_burp(4, belch=True)
    belch_or_burp(4, belch=False)

    # Return function calls
    sound = burp_return()
    print("Returned sound:", sound)

    sound2 = belch_or_burp_return(2, belch=True)
    print("Returned belch:", sound2)

    sound3 = belch_or_burp_return(3, belch=False)
    print("Returned burp:", sound3)

if __name__ == "__main__":
    main()
