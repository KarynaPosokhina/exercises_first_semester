computer_choice = "rock"
choice = str(input("What do you choose: paper, rock or scissors: "))
if computer_choice == choice:
    answer = "Tie!"
else:
    if computer_choice == "paper":
        if choice == "rock":
            answer = "I win ^^"
        else:
            answer = "You win ^^"
    if computer_choice == "rock":
        if choice == "scissors":
            answer = "I win ^^"
        else:
            answer = "You win ^^"
    else:
        if choice == "paper":
            answer = "I win^^"
        else:
            answer = "You win ^^"
print(f"You chose {choice}")
print(f"I chose {computer_choice}")
print(answer)