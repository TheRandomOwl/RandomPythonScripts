STEP_1 = False  # step 1
SHOWN_ONCE = False  # disables welcome message after being shown once
while True:
    while True:
        if not SHOWN_ONCE:
            print(' ')
            print("Welcome to: Do I Need To Fix My Lamp.\n Please put yes or no: ")
            SHOWN_ONCE = True
        WORKING = input("Does your Lamp work? (Y/N): ")
        WORKING = WORKING.capitalize()
        if WORKING == 'Y':
            print("Great! Lamp is working.")
            exit()
        if WORKING == "N":
            break
        else:
            print("Please put Y or N")
    while True:
        PLUG = input("Is it plugged in? (Y/N): ")
        PLUG = PLUG.capitalize()
        if PLUG == 'N':
            print("Plug it in.")
            STEP_1 = True
            break
        if PLUG == 'Y':
            break
        else:
            print("Please put Y or N")
    if STEP_1:
        STEP_1 = False
        continue
    while True:
        BULB = input("Is bulb burned out? (Y/N): ")
        BULB = BULB.capitalize()
        if BULB == 'N':
            print("Repair Lamp.")
            break
        if BULB == 'Y':
            BULB = True
            print("Replace your bulb.")
            break
        else:
            print("Please put Y or N")
