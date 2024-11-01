first_name = str(input("Enter the first name: "))

second_name = str(input("Enter the second name: "))

print(first_name, second_name)
temp = first_name
first_name = second_name
second_name = temp
print(first_name, second_name)


