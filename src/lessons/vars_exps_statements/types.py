'''
2025-07-16
Author: Dan Schumacher
How to run:
   python .\\src\\lessons\\vars_exps_statements\\types.py
'''

def main():
    # 1
    message = "hello"
    print(type(message)) # yes quotes

    # 2
    num_4 = 4
    print(type(num_4)) # no decimal

    # 3
    float_4 = 4.0
    print(float_4) # yes decimal

    # 4
    princess = "4.0" 
    print(princess) # yes decimal, but in quotes?
    # you can technically name (almost) anything, 
    # but don't -> confusing

    # 5
    my_bool = True
    print(my_bool) # must be capital 'T'

if __name__ == "__main__":
    main()