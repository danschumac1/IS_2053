'''
2025-07-16
Author: Dan Schumacher
How to run:
   python .\src\lessons\iteration\min_max.py
'''

def main():
    print("Let's find the tallest student in class!")

    tallest = None
    student_heights = [60, 65, 72, 68, 75, 70]  # example heights in inches

    for i, height in enumerate(student_heights):
        print(f"Student {i+1} height: {height}")
        if tallest is None or height > tallest:
            tallest = height
            print("New tallest student! Height is:", tallest)

    print("Tallest student is", tallest, "inches tall!")

if __name__ == "__main__":
    main()
