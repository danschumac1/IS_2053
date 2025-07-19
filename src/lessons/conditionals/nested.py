'''
2025-07-16
Author: Dan Schumacher
How to run:
   python .\src\lessons\conditionals\\nested.py
'''

def main():
    hand_raised = True
    touched_forehead = False

    if hand_raised:
        if touched_forehead:
            print("FOREHEAD!")
        else:
            print("whisperwhisper")

    standing_on_one_foot = True
    spinning = False

    if standing_on_one_foot:
        if spinning:
            print("SPINNING!")
        else:
            print("BALANCING!")

    snapping_fingers = True

    if snapping_fingers:
        print("SNAP SNAP!")

if __name__ == "__main__":
    main()
