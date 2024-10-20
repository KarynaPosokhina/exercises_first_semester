from random import randint


positive_number = 0
turns = 0
computer_number = randint(1, 10)

while positive_number != computer_number:
    positive_number = int(input("Enter a positive number: "))
    if positive_number < computer_number:
        print("Higher!")
    elif positive_number > computer_number:
        print("lower!")

    turns += 1

print("You have passed the number", positive_number, "in", turns, "turns")