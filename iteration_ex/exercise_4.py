# from random import randint
#
#
# positive_number = 0
# turns = 0
# computer_number = randint(1, 10)
#
# while positive_number != computer_number:
#     positive_number = int(input("Enter a positive number: "))
#     if positive_number < computer_number:
#         print("Higher!")
#     elif positive_number > computer_number:
#         print("lower!")
#
#     turns += 1
#
# print("You have passed the number", positive_number, "in", turns, "turns")

number_to_guess = 9
turns = 0
guess = -1

while guess != number_to_guess:
    guess = int(input("enter a positive number: "))
    turns += 1
    if guess < number_to_guess:
        print("higher")
    if guess > number_to_guess:
        print("lower")

print(f"you have guessed the number {guess} in {turns} turns")
