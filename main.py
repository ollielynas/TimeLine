import keyboard
import os
import time

print("\n  welcome to my game")
print("  in order to win press spacebar while the cursor in in the middle of the line")
print("Eg. -----[|]-----")
print("not ---|-[]-----")
input("press enter to begin")

cursor_position = 0

def update(cursor_position):

    os.system('cls' if os.name == 'nt' else 'clear')
    if cursor_position < 6:
        print("-" * cursor_position + "|"+ "-" * (5 - cursor_position)+"[-]"+"-" * 5)
    if cursor_position == 6:
        print("-" * 5 + "[|]" + "-" * 5)
    if cursor_position > 6:
        print("-" *5 + "[-]"+"-"*(5-(11 - cursor_position)) +"|"+ "-" * (11 - cursor_position))
    for i in range (20):
        time.sleep(0.05/20)
        if keyboard.is_pressed(' '):
            if cursor_position == 6:
                input("You won!")
                quit()
            else:
                input("You Lost!")
                quit()
while True:
    while cursor_position < 11:
        cursor_position += 1
        update(cursor_position)
    while cursor_position > 0:
        cursor_position -= 1
        update(cursor_position)

