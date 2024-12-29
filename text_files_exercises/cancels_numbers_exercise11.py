file = open('copy_exercise.txt')
new_file = open('nonumbers.py', 'w')

lines = file.readlines()
for line in lines:
    new_file.write(line[5:])


new_file.close()
file.close()