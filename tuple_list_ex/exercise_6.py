text = str(input("Enter a text: "))
strings = []

for i in range(len(text)):
    if text[i] != ' ':
        strings.append(text[i])

print(strings)
print()
print(*strings)
print()
for letter in strings:
    print(letter, '\t', end='')
