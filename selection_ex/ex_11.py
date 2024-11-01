weight = int(input("Your weight in kilograms: "))
length = int(input("You length in centimetres: "))

BMI = weight / (length / 100) ** 2

if BMI < 18:
    result = "underweight"
elif (18 <= BMI < 25):
    result = "normal weight"
elif (25 <= BMI < 27):
    result = "slightly overweight"
elif (27 <= BMI < 30):
    result = "moderate overweight"
elif (30 <= BMI < 40):
    result = "obese"
else:
    result = "sickly obese"

print(f"A person of {weight} kg with a length of {length} has as BMI {BMI}")
print(f"This is {result} .")