# number = int(input("Enter a number: "))
# zeros = str(number).count("0")
# sixes = str(number).count("6")
# print("The number consists of", zeros,"zeros and", sixes, "sixes")

zeros = 0
sixes = 0
number = int(input("Enter a number: "))

for digit in str(number):
    if digit == '0':
        zeros += 1
    if digit == '6':
        sixes += 1

print(f"the number consists of {zeros} zeros and {sixes} sixes")



