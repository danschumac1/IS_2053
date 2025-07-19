'''
2025-07-17
Author: Dan Schumacher
How to run:
   python .\src\lessons\strings\indexing.py
'''

def main():
    word = "wolverine"

    print("Word:", word)
    print("---------------------------")

    # 1. Single letter grab
    print("1. Single letter grab")
    print("Letter at index 0:", word[0])  # 'w'
    print("Letter at index 3:", word[3])  # 'v'
    print("Letter at index 5:", word[5])  # 'r'
    print("---------------------------")

    # 2. Range of letter grab (start:stop)
    print("2. Range of letter grab")
    print("Letters from index 0 to 3:", word[0:4])  # 'wolv'
    print("Letters from index 3 to 7:", word[3:8])  # 'verin'
    print("Full word from index 0 to end:", word[0:])  # 'wolverine'
    print("---------------------------")

    # 3. Using negative indexes
    print("3. Negative indexing")
    print("Last letter:", word[-1])       # 'e'
    print("Second to last letter:", word[-2])  # 'n'
    print("Letters from index -4 to end:", word[-4:])  # 'rine'
    print("---------------------------")

    # 4. Reversing the string
    print("4. Reversing the word")
    print("Reversed:", word[::-1])  # 'enirevlow'

if __name__ == "__main__":
    main()