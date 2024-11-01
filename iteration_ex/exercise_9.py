MIN_NUMBER = 10
MAX_NUMBER = 21

for i in range(MIN_NUMBER, MAX_NUMBER, 2):
    for j in range(i, -1, -1):
        print(j, end=" ")

    print()