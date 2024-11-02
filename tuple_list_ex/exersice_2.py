numbers = [9, 17, 25, 1, 12, 7]
new_numbers = []

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        new_numbers.insert(0, numbers[i])
    else:
        new_numbers.append(numbers[i])

print(f'{numbers} becomes: {new_numbers}')
