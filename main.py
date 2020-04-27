# SpamMessager
# Written by Tyler Dakin
# https://tylerdakin.com/SpamMessager
# Copyright 2020 Tyler Dakin

# to automate the keyboard
import pyautogui
# to make the countdown audible
import os
# for the countdown
import time
# for Integer checking
from isInt import *
# For path functionality
from pathlib import Path
# To open dialog box for file getter
from tkinter import *
from tkinter.filedialog import askopenfilename

Tk().withdraw()

# Create blank message variable to ensure message is available
message = ""

# Ask user if they're importing from txt file or just typing in the message
print("Choose one:\n[1] Type message\n[2] Import from .txt file")
choice = 3
while not (isInt(choice) and (choice == 1 or choice == 2)):
    print("CHOICE: ",end="")
    choiceIn = input()
    if (isInt(choiceIn)):
        choice = int(choiceIn)

if (choice == 1):
    # Get the message from the user
    print("MESSAGE: ",end="") #end="" to make sure it doesn't create a newline
    message = input()
elif (choice == 2):
    # Ask for text file and get words out of there
    validFile = False
    txtFilename = ''
    print("Please select the .txt file.")

    while (not validFile):
        #opens dialog box which will return a filename
        txtFilename = askopenfilename()

        if (txtFilename == ''):
            validFile = False
            print("Please choose your .txt file so we can make your bracket.")
            print("[Press ENTER or RETURN]")
            wait1 = input()
        elif (not txtFilename.endswith(".txt")):
            validFile = False
            print("Please choose a valid .txt file so we can make your bracket.")
            print("[Press ENTER or RETURN]")
            wait1 = input()

        else:
            validFile = True
    
    message = Path(txtFilename).read_text()

# Split message into parts determined by each word
array = message.split()

# Countdown code
# Set the countdown to 3 seconds
amount = 3
os.system("say Starting in")
for h in range(amount):
    os.system("say " + str(amount - h))
    # time.sleep is what makes the countdown accurate by adding a one second delay.
    time.sleep(1)

# Actually spits out the words, one by one.
for word in array:
    pyautogui.write(word)
    pyautogui.press('enter')