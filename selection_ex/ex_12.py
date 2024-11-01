age = int(input("Tell me your age: "))

if age < 6:
    print("You are too young")
elif age <= 7:
    section = "Beavers"
elif age <= 10:
    section = "Cubs"
elif age <= 13:
    section = "Scouts"
elif age <= 18:
    section = "Explorers"
else:
    section = "Leaders"

print(f"You will be assigned to the {section} section")
