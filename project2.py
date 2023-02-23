import random

action_list = ["rock", "paper", "scissors"]

computer_score = 0
player_score = 0

total_rounds = input("How many rounds do you want to play plase enter a number here: ")

round_counter = 0

while True:
    round_counter += 1
    print("Round number", round_counter)

    computer_choice = random.choice(action_list)
    player_choice = input("Please choose your action")

    print("Computer", computer_choice)
    print("Player", player_choice)
    
    if computer_choice == player_choice:
        print("Tial! Both players choose the same action")
    elif computer_choice == "paper":
        if player_choice == "rock":
            print("Winner is: Computer")
            computer_score += 1
        else: 
            print("Winner is: player")
            player_score += 1
    elif computer_choice == "rock":
        if player_choice == "paper":
            print("winner is: PLayer")
            player_score += 1
        else:
            print("Winner is: Computer")
            computer_score += 1
    elif computer_choice == "scissors":
       if player_choice == "paper":
            print("Winner is: Computer")
            computer_score += 1
       else:
           print("Winner is: Player")
           player_score += 1

    if round_counter == int(total_rounds):
        break

if computer_score == player_score:
    print("There is no winner, tie.", computer_score, ":", player_score)
elif computer_score >player_score:
    print("Computer won with score", computer_score, ":", player_score)
elif computer_score < player_score:
    print("Player won with score", computer_score, ":", player_score)
