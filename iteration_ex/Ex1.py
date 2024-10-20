number = int(input("enter a number: "))
product = 1;
while not number == 0:
    product *= number
    number = int(input("enter a number: "))

print(product)