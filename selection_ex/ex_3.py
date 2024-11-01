number_1 = int(input("Enter the number: "))
number_2 = int(input("Enter the number: "))
number_3 = int(input("Enter the number: "))


if number_1 <= number_2 and number_3:
    smallest_number = number_1
elif number_2 <= number_1 and number_3:
    smallest_number = number_2
else:
    smallest_number = number_3



smallest = print(f"The smallest number is {smallest_number} ")