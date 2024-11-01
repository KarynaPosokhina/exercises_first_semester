computer = "rock"
choice = input("What do you choose: paper, rock or scissors? ")
if computer == choice:
    answer = "Tie!"
else:
    match computer:
        case "paper":
            if choice == "rock":
                answer = "i win"
            else:
                answer ="u win"
        case "rock":
            if choice == "scissors":
                answer = "i win"
            else:
                answer = "u win"
        case "scissors":
            if choice == "paper":
                answer = "i win"
            else:
                answer = "u win"

print(f"you chose {choice}")
print(f"i chose {computer}")
print(answer)