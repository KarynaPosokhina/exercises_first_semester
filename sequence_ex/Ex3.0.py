three_digit_number = int(input("Emter a three-digit number: "))
print(str(type(three_digit_number)))
print(three_digit_number/2)
print(three_digit_number*2)
print(three_digit_number**3)
print(three_digit_number*10)

first_digit = int(three_digit_number/100)
print(first_digit)
second_digit = int(three_digit_number%100/10)
print(second_digit)
third_digit = int(three_digit_number%100)%10
print(third_digit)