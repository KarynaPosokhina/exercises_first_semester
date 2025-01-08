with open("tasks.csv", "r") as file:
    lines = file.readlines()

lines = lines[1:]
tasks = {}
for line in lines:
    row = line.strip().split(";")
    for person in row[1:]:
        if person in tasks:
            tasks[person] += 1
        else:
            tasks[person] = 1

print("Task distribution:")
for person in sorted(tasks):
    print(f"{person} {tasks[person]}")
