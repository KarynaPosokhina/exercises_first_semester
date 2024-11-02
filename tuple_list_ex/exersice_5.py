MAIN_NUMBER = 0

# numbers = [0, 42, 18, 17, 0, 2, 19, 10, 5, 14]
numbers = [42, 18, 0, 37, 0, 2, 19, 10, 5, 14]
# numbers = [42, 18, 17, 0, 2, 19, 0]
print(numbers)

for i in range(len(numbers)):
    if numbers[i] == MAIN_NUMBER:
        odd_list = []
        for j in range(i, len(numbers)):
            if numbers[j] % 2 > 0:
                odd_list.append(numbers[j])

        if odd_list:
            numbers[i] = max(odd_list)

print(numbers)

