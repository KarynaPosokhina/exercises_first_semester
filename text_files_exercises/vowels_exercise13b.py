# with open("hamlet2.txt", "r") as rf:
#     with open("hamlet3.txt", "w") as wf:
#         lines = rf.readline()
# def remove_vowels(line):
#     new_line = ""
#     for character in line:
#         if character not in "aeiouAEIOU":
#             new_line += character
#     return new_line


input_file = open("hamlet2.txt", "r")
output_file = open("hamlet3.txt", "w")

def remove_vowels(line):
    new_line = ""
    for character in line:
        if character not in "aeiouAEIOU":
            new_line += character
    return new_line

read_count = 0
write_count = 0


print(f"The input file contains {read_count} characters")
print(f"The output file contains {write_count} characters")