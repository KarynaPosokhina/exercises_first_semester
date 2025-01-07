print("Classrooms: ")
with open("local_booking_2023.txt", 'r') as file:
    classroom_set = set()
    line = file.readline().rstrip()
    while line:
        record = line.split(';')
        classroom = record[3]
        classroom_set.add(classroom)
        line = file.readline().rstrip()
for classroom in sorted(classroom_set):
    print(classroom)