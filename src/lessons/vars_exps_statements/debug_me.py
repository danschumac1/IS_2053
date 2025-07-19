'''
2025-07-16
Author: Dan Schumacher
How to run:
   python .\src\lessons\\vars_exps_statements\debug_me.py
'''

# Debug Me! Activity
# Instructions:
# The following code is full of bugs! Your job is to:
# - Identify syntax errors, runtime errors, and logic (semantic) errors
# - Fix the code so that it prints the correct final amount after interest is applied
# - Bonus: Add helpful comments to explain the corrections

def main():
    # Declaring variables
    principal = 1000.0
    rate = 0.05
    years = 5

    # Calculate compound interest
    # ERROR: Incorrect formula and a typo in 'principle'
    interest = principle * (1 + rate) ** years

    # ERROR: wrong capitalization of variable 'Interest'
    print("After", years, "years, your investment will be worth:", Interest)

    # Bonus semantic bug:
    # What if we wanted to calculate half of pi? What does this give us?
    pi = 3.14159
    half_pi = 1.0 / 2.0 * pi  # Is this half of pi?
    print("Half of pi is:", half_pi)

if __name__ == "__main__":
    main()
