first_number = int(input("First number: "))
second_number = int(input("Second number: "))

if first_number < 0:
    first_number = first_number * -1
if second_number < 0:
    second_number = second_number * -1
if first_number == second_number:
    output = 0
else:
    if first_number % 5 == second_number % 5:
        if first_number < second_number:
            output = first_number
        else:
            output = second_number
    else:
        if first_number > second_number:
            output = second_number
        else:
            output = first_number
print(f"The answer for the numbers: {first_number} and {second_number} = {output}")




