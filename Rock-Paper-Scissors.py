from random import randint
player = str
move = str
computer_move = str
print("To play, select Rock, Paper, or Scissors(1,2,or 3) or select q to quit.")
while True:
    computer = randint(1, 3)
    if int(computer) == 1:
        computer_move = "Rock"
    elif int(computer) == 2:
        computer_move = "Paper"
    elif int(computer) == 3:
        computer_move = "Scissors"
    while True:
        player = input("Select your move: ")
        if player == 'q':
            exit(0)
        try:
            if 0 < int(player) < 4:
                if int(player) == 1:
                    move = "Rock"
                elif int(player) == 2:
                    move = "Paper"
                elif int(player) == 3:
                    move = "Scissors"
                print(f"Your move is {move}")
                break
            else:
                print(f"{player} is not a option.")
        except ValueError:
            print(f"{player} is not a valid option.")
    print(f"Computer's move is {computer_move}")
    if int(player) == int(computer):
        print("tie")
    elif int(player) + int(computer) == 3:
        if int(player) > int(computer):
            print("You win!")
        else:
            print("You lose!")
    elif int(player) + int(computer) == 4:
        if int(player) > int(computer):
            print("You lose!")
        else:
            print("You win!")
    elif int(player) + int(computer) == 5:
        if int(player) > int(computer):
            print("You win!")
        else:
            print("You lose!")
