name_list = []

with open("first_names.txt", "r") as file:
    for line in file:
        name_list.append(line.strip())

for i in range(0, len(name_list), 10):
    table = name_list[i:i+10]
    for name in table:
        print(name.ljust(13), end="")
    print()