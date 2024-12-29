girls = []
boys = []

with open("contacts.csv", "r") as file:
    lines = file.readline().rstrip()
    while lines:
        line = lines.split(';')
        if line[3] == 'M':
            boys.append(f"{line[0]}  {line[1]}")
        else:
            girls.append(f"{line[0]}  {line[1]}")
        lines = file.readline().rstrip()

boys.sort()
girls.sort()

print(len(girls), "girls:")
for girl in girls:
    print( "\t", girl)
print(len(boys), "boys:")
for boy in boys:
    print("\t" ,boy)