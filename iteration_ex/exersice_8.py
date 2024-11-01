MAX_NUMBERS = 10

counter = 0
final_digit = str(input("What final digit do you want to check the numbers on: "))


for i in range(MAX_NUMBERS):
    number = str(input("Enter a number: "))

    last_digit = number[len(number) - 1]
    if last_digit == final_digit:
        counter += 1

print(f"{counter} out of {MAX_NUMBERS} numbers end on {final_digit} ")
