'''
2025-07-20
Author: Dan Schumacher
How to run:
   python .\\src\lessons\\lists\\iterate.py
'''

def main():
    # ITERATE
    grocery_list = [
        "Bread", 
        "Cheese", 
        "Milk", 
        "Spatula", 
        "Protein Powder"
        ]
    print("\nIterate over grocery list:")
    for grocery in grocery_list:
        print(grocery)

    # MUTATE (MUTABLE)
    # whoops we forgot to get dog food!
    grocery_list.append("Dog Food")
    print("\nAfter appending Dog Food (mutable example):")
    print(grocery_list)

    # My grandma broke her leg she gave me her list
    grandmas_list = [
        "Laxatives",
        "Roses",
        "Wheaties Cereal"
    ]

    # we can combine our lists.
    # what happens if we use .append?
    grocery_list.append(grandmas_list)
    print("\nAfter appending grandma's list:")
    print(grocery_list)

    # instead we should use .extend
    # reset our grocery list
    grocery_list = [
        "Bread", 
        "Cheese", 
        "Milk", 
        "Spatula", 
        "Protein Powder"
        ]
    
    grocery_list.extend(grandmas_list)
    print("\nAfter extending grocery list with grandma's list:")
    print(grocery_list)

    # IS / IN
    print("\nIs 'Roses' in grocery list?")
    print("Roses" in grocery_list)

    # INDEXING and SLICING
    print("\nIndexing and Slicing:")
    print("First item:", grocery_list[0])
    print("Last item:", grocery_list[-1])
    print("Items 2 to 4:", grocery_list[1:4])

    # REASSIGN ITEMS
    print("\nReassigning items:")
    grocery_list[0] = "Almond Bread"
    print("Changed first item to Almond Bread:", grocery_list)

    # CHANGE ORDER
    print("\nChanging order:")
    grocery_list.reverse()
    print("Reversed list:", grocery_list)

    grocery_list.sort()
    print("Sorted list:", grocery_list)

    # OPERATIONS
    print("\nList operations:")
    doubled_list = grocery_list * 2
    print("List multiplied by 2:", doubled_list)

    more_items = ["Apples", "Bananas"]
    combined_list = grocery_list + more_items
    print("Combined with another list:", combined_list)

    # REMOVE ELEMENTS
    print("\nRemoving elements:")
    grocery_list.remove("Roses")  # removes by value
    print("After removing 'Roses':", grocery_list)

    popped_item = grocery_list.pop()  # removes last item
    print(f"Popped last item ({popped_item}):", grocery_list)

    del grocery_list[0]  # removes by index
    print("After deleting first item:", grocery_list)


if __name__ == "__main__":
    main()
