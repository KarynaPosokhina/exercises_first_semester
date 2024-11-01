difference = 0
largest = 0
smallest = 0
number = int(input("Enter a number: "))

if number == 0:
    print("No numbers entered ")
else:
    while number != 0:
        if number > largest:
            largest = number
        if number < smallest:
            smallest = number
        number = int(input("Enter a number: "))

    difference = largest - smallest
    print(f"The difference between the largest number {largest} and the smallest {smallest} = {difference}")