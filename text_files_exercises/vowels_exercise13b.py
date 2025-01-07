input_file = open("hamlet2.txt", "r")
output_file = open("hamlet3.txt", "w")

def remove_vowels(line):
    new_line = ""
    for character in line:
        if character not in "aeiouAEIOU":
            new_line += character
    return new_line

assert remove_vowels("Hello World") == "Hll Wrld"

read_count = 0
write_count = 0
line = input_file.readline()

while line:
    read_count += len(line)
    line = remove_vowels(line)
    write_count += len(line)
    output_file.write(line)
    line = input_file.readline()

output_file.close()
input_file.close()

print(f"The input file contains {read_count} characters")
print(f"The output file contains {write_count} characters")