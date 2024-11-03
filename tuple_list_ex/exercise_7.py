numbers = [2, 4, 5, 9]
print(numbers)

new_list = numbers * 2

for i in range(len(new_list) - 1):
    new_list[i] = 0
print(new_list)
