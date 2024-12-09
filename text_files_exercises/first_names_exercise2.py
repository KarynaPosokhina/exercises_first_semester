name_list = []

with open("first_names.txt", "r") as file:
    for line in file:
        name_list.append(line.strip())
print(name_list)

# using 'reverse()' method
reversed_list = name_list.copy()
reversed_list.reverse()
print(reversed_list)

# using slicing
# reversed_list = name_list[::-1]
# print(reversed_list)

# using a for loop with 'reversed()'
# for name in reversed(name_list):
#     print(name)