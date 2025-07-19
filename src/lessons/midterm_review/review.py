'''
2025-07-19
Author: Dan Schumacher
How to run:
   python .\src\lessons\midterm_review\review.py
'''

import json
import random

# 2. Variables, expressions, statements
x = 5
word = "hello"
print("Value of x:", x)
print("Type of word:", type(word))

# 2.5 Operators and operands
print("Addition:", 2 + 3)
print("Multiplication:", 4 * 5)
print("Modulus:", 9 % 2)

# 2.7 Order of operations
print("Order of operations:", 2 + 3 * 4)

# 2.10 User Input
user_name = input("What is your name? ")
print(f"Hello, {user_name}!")

# 3. Conditional execution
num = int(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

# 3.7 Try and except
try:
    print(10 / 0)
except ZeroDivisionError:
    print("You cannot divide by zero!")

# 4. Functions
def greet(name):
    return f"Welcome, {name}!"

print(greet(user_name))

# 4.5 Random numbers
print("Random number between 1 and 10:", random.randint(1, 10))

# 5. Loops
for i in range(5):
    print(f"For loop iteration: {i}")

counter = 0
while counter < 3:
    print(f"While loop count: {counter}")
    counter += 1

# 6. Strings
my_string = "wolverine"
print("Length of string:", len(my_string))
print("First three letters:", my_string[:3])
print("Reversed string:", my_string[::-1])

# 7. Files
try:
    with open('./data/midterm_sample.txt', 'w') as f:
        f.write("This is a midterm review file.")
    with open('./data/midterm_sample.txt', 'r') as f:
        content = f.read()
        print("File content:", content)
except FileNotFoundError:
    print("File not found!")

def main():
    print("Midterm Review Complete!")

if __name__ == "__main__":
    main()
