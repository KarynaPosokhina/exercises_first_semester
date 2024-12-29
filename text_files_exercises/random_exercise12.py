import random

number = random.randint(1,10)
name_file = f"table_{number}.txt"
new_file = open(name_file, "w")

for numbers in range(1, 11):
    new_file.write(f"{numbers} * {number} = {numbers * number} \n")

new_file.close()