first_number = int(input("number 1: "))
second_number = int(input("number 2: "))
third_number = int(input("number 3: "))

if (first_number == second_number + third_number
        or second_number == first_number + third_number
        or third_number == second_number + first_number):
    print("yipeeee")
else:
    print("won't work")


