current_year = 2024

year_or_birth = int(input("Enter your year of birth: "))
your_age = current_year - year_or_birth
print(f"Your age is: {your_age}")
if your_age >= 18:
    print("So you are an adult")
else:
    print("You are not an adult yet")
    