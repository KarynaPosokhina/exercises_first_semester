text = input("Enter a text consisting only numbers and letters: ")
numbers = set()
letters = set()
for character in text:
    if character.isdigit():
        numbers.add(character)
    else:
        letters.add(character)

print("The numbers: ")
for digit in numbers:
    print(digit)
print("The letters: ")
for letter in letters:
    print(letter)