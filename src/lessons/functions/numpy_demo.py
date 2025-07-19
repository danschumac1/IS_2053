'''
2025-07-17
Author: Dan Schumacher
How to run:
   python .\src\lessons\\functions\\numpy_demo.py
'''

import numpy as np

def main():
    # Example 1: Pi and sine
    print("Pi:", np.pi)
    print("sin(pi / 2):", np.sin(np.pi / 2))

    # Example 2: Degrees to radians
    degrees = 45

    # radians are the length of the slice of the circle's circumf
    radians = np.deg2rad(degrees)
    print(f"{degrees} degrees in radians:", radians)

    # Example 3: Random numbers
    print("Random float [0,1):", np.random.rand())
    print("Random int between 1 and 10:", np.random.randint(1, 11))

    # Example 4: Square root
    print("Square root of 16:", np.sqrt(16))

if __name__ == "__main__":
    main()
