'''
2025-07-21
Author: Dan Schumacher
Chapter 10: Tuples - Examples and Practice
How to run:
    python .\\src\\lessons\\tuples\\tuples.py
'''

def calculate_stats(numbers):
    """Return the min and max from a list of numbers."""
    smallest = min(numbers)
    largest = max(numbers)
    return smallest, largest  # returns a tuple

def main():
    # 10.1 Tuples are immutable
    print("=== 10.1 Tuples are Immutable ===")
    t = ('apple', 'banana', 'cherry')
    print("Tuple t:", t)
    print("First element:", t[0])
    print("Slice:", t[1:])

    # Uncommenting the next line would cause an error:
    # t[0] = 'apricot'

    # Creating a tuple from a list
    fruits = ['grape', 'orange', 'kiwi']
    t2 = tuple(fruits)
    print("Tuple from list:", t2)

    # Single-element tuple
    single = ('solo',)
    print("Single-element tuple:", single, "| Type:", type(single))


    # 10.2 Comparing tuples
    print("\n=== 10.2 Comparing Tuples ===")
    player1 = (100, 3)   # score, lives
    player2 = (120, 1)
    print("Is player1 < player2?", player1 < player2)

    levels = [(3, 'Easy'), (2, 'Medium'), (5, 'Hard')]
    levels.sort()
    print("Levels sorted by difficulty number:", levels)


    # 10.3 Tuple assignment
    print("\n=== 10.3 Tuple Assignment ===")
    person = ('Ada', 'Lovelace')
    first_name, last_name = person
    print("First name:", first_name)
    print("Last name:", last_name)

    # Swap variables
    a, b = 5, 10
    print("Before swap:", a, b)
    a, b = b, a
    print("After swap:", a, b)

    # Split email address
    email = 'grace.hopper@nasa.gov'
    username, domain = email.split('@')
    print("Username:", username)
    print("Domain:", domain)


    # 10.4 Dictionaries and Tuples
    print("\n=== 10.4 Dictionaries and Tuples ===")
    capitals = {'France': 'Paris', 'Japan': 'Tokyo', 'Brazil': 'Brasilia'}
    cap_items = list(capitals.items())
    print("Dictionary items as list of tuples:", cap_items)
    cap_items.sort()
    print("Sorted by country:", cap_items)


    # 10.5 Multiple assignment with dictionaries
    print("\n=== 10.5 Multiple Assignment with Dictionaries ===")
    for country, city in capitals.items():
        print(f"The capital of {country} is {city}.")

    # Sorting by value (city name)
    cap_tuples = []
    for country, city in capitals.items():
        cap_tuples.append((city, country))

    cap_tuples.sort()
    print("Countries sorted by capital city name:")
    for city, country in cap_tuples:
        print(city, "-", country)


    # 10.6 Most common colors in a list
    print("\n=== 10.6 Most Common Colors ===")
    colors = ['red', 'blue', 'green', 'red', 'yellow', 'blue', 'red', 'green', 'green', 'blue']
    color_count = dict()
    for color in colors:
        color_count[color] = color_count.get(color, 0) + 1

    count_color_tuples = []
    for color, count in color_count.items():
        count_color_tuples.append((count, color))

    count_color_tuples.sort(reverse=True)
    print("Color frequency sorted descending:")
    for count, color in count_color_tuples:
        print(color, "appeared", count, "times")


    # 10.7 Tuples as dictionary keys
    print("\n=== 10.7 Tuples as Dictionary Keys ===")
    seating_chart = dict()
    seating_chart[('A', 1)] = 'Alice'
    seating_chart[('B', 2)] = 'Bob'
    seating_chart[('A', 2)] = 'Carol'

    print("Seating chart (Row, Seat):")
    for (row, seat), name in seating_chart.items():
        print(f"Seat {row}{seat}: {name}")


    # 10.8 Sequences: strings, lists, and tuples
    print("\n=== 10.8 Sequences: Strings, Lists, Tuples ===")
    seq_list = ['dog', 'cat']
    seq_tuple = ('parrot', 'hamster')
    seq_string = "fish"

    print("List:", seq_list)
    print("Tuple:", seq_tuple)
    print("String:", seq_string)
    print("First item from each:", seq_list[0], seq_tuple[0], seq_string[0])

    # 10.9 Functions Returning Tuples
    print("\n=== 10.9 Functions Returning Tuples ===")

    scores = [87, 95, 45, 68, 92, 100, 56]
    min_score, max_score = calculate_stats(scores)
    print("Scores:", scores)
    print("Minimum score:", min_score)
    print("Maximum score:", max_score)


if __name__ == "__main__":
    main()
