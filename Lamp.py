#!/usr/bin/env python3
# Script that tells you if your lamp need to be fixed.
import sys

STEP_1 = 1  # step 1
STEP_2 = 0  # step 2
STEP_3 = 0  # step 3
SHOWN_ONCE = False
while True:
    while STEP_1 == 1:
        if not SHOWN_ONCE:
            print(' ')
            print("Welcome to do I Need To Fix My Lamp. Please put your input below")
            print(' ')
            SHOWN_ONCE = True
        WORKING = input("Does your Lamp work? (Y/N) ")
        WORKING = WORKING.capitalize()
        if WORKING == 'Y':
            print("Lamp is Working")
            sys.exit(0)
        if WORKING != "N":
            print("Please put Y or N")
            print(' ')
        if WORKING == 'N':
            STEP_1 = 0
            STEP_2 = 1
    while STEP_2 == 1:
        PLUG = input("Is it plugged in? (Y/N) ")
        PLUG = PLUG.capitalize()
        if PLUG == 'N':
            PLUG = False
            print("Plug it in.")
            STEP_1 = 1
            STEP_2 = 0
        if PLUG == 'Y':
            PLUG = True
            STEP_2 = 0
            STEP_3 = 1
        if PLUG == str(PLUG):
            print("Please put Y or N")
    while STEP_3 == 1:
        BULB = input("Is bulb burned out? (Y/N) ")
        BULB = BULB.capitalize()
        if BULB == 'N':
            BULB = False
            print("Repair Lamp.")
            STEP_1 = 1
            STEP_2 = 1
            STEP_3 = 0
        if BULB == 'Y':
            BULB = True
            print("Replace bulb.")
            STEP_1 = 1
            STEP_2 = 1
            STEP_3 = 0
        if BULB == str(BULB):
            print("Please put Y or N")
