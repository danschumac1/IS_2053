def main():
    # 1 - Basic example
    number1 = input("Enter the first number: ")
    number2 = input("Enter the first number: ")

    try: # first we **try** this route. if it works awesome!
        # we take input and make it be a integer
        number1 = int(number1)
        number2 = int(number2)
        my_sum = number1 + number1
        print("Those numbers sum to the value:", my_sum)
    except: # it if doesn't work we end up here.
        print("Oops! That's not a number.")

if __name__ == "__main__":
    main()
