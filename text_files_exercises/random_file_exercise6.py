import random

number = random.randint(1,10)

print(f"Wish {number} \n")
with open(f'wish{number}.txt', 'r') as file:
     for line in file:
         print(line.strip())
