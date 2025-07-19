'''
2025-07-16
Author: Dan Schumacher
How to run:
   python .\src\lessons\conditionals\conditional_execution.py
'''

def main():
    # Simulate classroom conditionals!
    
    # 1 - Raise hand
    hand_raised = True
    if hand_raised:
        print("CLAP!")

    # 2 - Stomp foot
    stomp_foot = False
    if stomp_foot:
        print("STOMP!")

    # 3 - Number written on board
    number_on_board = 7
    if number_on_board > 5:
        print("BIGG!")
    else:
        print("SMALL!")

    # 4 - Point to door
    pointed_to_door = True
    if pointed_to_door:
        print("Wave goodbye!")

    # 5 - Say "Python"
    word_said = "Python"
    if word_said == "Python":
        print("Pretend to type on a keyboard")

    # 6 - Smile or serious
    smiling = False
    if smiling:
        print("Happy!")
    else:
        print("Serious!")

if __name__ == "__main__":
    main()
