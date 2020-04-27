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

# Get the message from the user
print("MESSAGE: ",end="") #end="" to make sure it doesn't create a newline
message = input()

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