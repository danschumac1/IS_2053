'''
2025-07-16
Author: Dan Schumacher
How to run:
   python .\src\lessons\iteration\counting.py
'''


def main():
    print("Let's count the total number of letters in these words!")

    total_letters = 0
    words = ['Fellowship', 'Ring', 'Mordor', 'Shire', 'Gandalf']

    for word in words:
        letter_count = len(word)
        total_letters = total_letters + letter_count
        print(f"'{word}' has {letter_count} letters. Total letters so far: {total_letters}")

    print("Total number of letters in all words:", total_letters)

if __name__ == "__main__":
    main()