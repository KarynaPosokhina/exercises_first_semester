with open("classrooms.txt", "r") as file:
    line = file.readline().rstrip()
    record = line.split(';')
    while line:
        number_per_room = 0
        roomind = record[2]
        print(roomind)
        while line and record[2] == roomind:
            number_per_room += 1
            print("\t", record[0], record[1])
            line = file.readline().rstrip()
            record = line.split(';')
        print(f"Number of students in classroom {roomind} = {number_per_room}")
