names = 0
with open("first_names.txt", "r") as file:
    for line in file:
        print(line.strip())
        names += 1

print(f"There are {names} first names in the file")

z_names = 0
with open("first_names.txt", "r") as file:
    for line in file:
        name = line.strip()
        if 'z' in name:
            print(name)
            z_names += 1

print(f"{z_names} of them contain the letter 'z'")


