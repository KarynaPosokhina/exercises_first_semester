def celsius_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

def fahrenheit_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

assert celsius_fahrenheit(38) == 100.4
assert celsius_fahrenheit(39) == 102.2
assert celsius_fahrenheit(39.3) == 102.74
assert celsius_fahrenheit(40.7) == 105.26

assert fahrenheit_celsius(99.5) == 37.5
assert fahrenheit_celsius(101.3) == 38.5
assert fahrenheit_celsius(104) == 40
assert fahrenheit_celsius(107.6) == 42

question = 'c'
while question == "c" or question == "f":
    question = input("Do you want to convert starting from Celsius (enter C) or Fahrenheit (enter F): ").lower()
    if question == "c":
        entered_value = float(input("Degrees: "))
        result = celsius_fahrenheit(entered_value)
        print(entered_value, "degrees Celsius = ", result, "degrees Fahrenheit")
    elif question == "f":
        entered_value = float(input("Degrees: "))
        result = fahrenheit_celsius(entered_value)
        print(entered_value, "degrees Fahrenheit = ", result, "degrees Celsius")


# while degrees_celsius != 0:
#     degrees_celsius = float(input("Degrees Celsius: "))
#     if degrees_celsius == 0:
#         print("Degrees Celsius: 0")
#     else:
#         degrees_fahrenheit = celsius_fahrenheit(degrees_celsius)
#         print(str(degrees_celsius), "degrees Celsius =", str(degrees_fahrenheit), "degrees Fahrenheit")