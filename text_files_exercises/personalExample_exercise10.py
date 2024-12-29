# number = 1
# with open("fatherAgeEx3.py", "r") as rf:
#     with open("copy_exercise.txt", "w") as wf:
#         for line in rf:
#             wf.write(f"{number} {line}")
#             number += 1

file = open('playlist_exercise7.py')
new_file = open('copy_exercise.txt', 'w')

lines = file.readlines()
number = 1
for line in lines:
    new_file.write('{:4}'.format(number) + ' ' + line)
    number += 1

new_file.close()
file.close()