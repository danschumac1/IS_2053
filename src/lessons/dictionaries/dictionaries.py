'''
2025-07-20
Author: Dan Schumacher
Chapter 9: Dictionaries
How to run:
   python .\\src\\lessons\\dictionaries\\dictionaries.py
'''


import string


def main():
    # Creating an empty dictionary
    menu = dict()
    print("Empty dictionary:", menu)

    # Adding key-value pairs
    menu['black coffee'] = 1.50
    menu['latte'] = 3.50
    menu['espresso'] = 2.15
    print("Menu:", menu)

    # Looking up a value
    print("The price of 'espresso:", menu['espresso'])

    # len function counts key-value pairs
    print("Number of items:", len(menu))

    # Using 'in' to check if key exists
    print("'espresso' in menu?", 'espresso' in menu)
    print("'mocha' in eng2sp?", 'mocha' in menu)

    # .values() returns all values
    vals = list(menu.values())
    print("'1.50' in values?", 1.50 in vals)

    # Example: counting letters in a word
    word = 'brontosaurus'
    letter_counts = dict()
    for c in word:
        letter_counts[c] = letter_counts.get(c, 0) + 1
    print("Letter counts in 'brontosaurus':", letter_counts)

    
    sentences = [
        "Once a upon a time in a lang far far away", 
        "There lived a dog named Louisa",
        "And she was all alone",
        "Until we decided we wanted a dog!",
        "And we adopted Louisa",
        "So that Louisa wouldn't have to be alone."
        ]

    word_counts = dict()
    for line in sentences:
        line = line.rstrip()
        line = line.translate(str.maketrans('', '', string.punctuation))
        line = line.lower()
        words = line.split()

        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1

    print("\nWord counts:", word_counts)

    # Looping through dictionary keys and values
    print("\nWords that appear more than 2 times:")
    for key in word_counts:
        if word_counts[key] > 2:
            print(key, word_counts[key])

    # Sorted output of dictionary keys
    sorted_keys = list(word_counts.keys())
    sorted_keys.sort()
    print("\nWord counts sorted alphabetically:")
    for key in sorted_keys:
        print(key, word_counts[key])

    # Debug tip
    print("\nTotal number of unique words:", len(word_counts))


if __name__ == "__main__":
    main()
