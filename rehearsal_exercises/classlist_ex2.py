def possible_classes():
    class_set = set()
    with open("classlist.csv") as file:
        line = file.readline()
        while line:
            fields = line.rstrip().split(";")
            class_set.add(fields[3])
            line = file.readline()
    return class_set

def control(nameclass):
    attendance = []
    with open("classlist.csv") as file:
        line = file.readline()
        while line:
            fields = line.rstrip().split(';')
            if fields[3] == nameclass:
                presence = (input(fields[2]+' '+fields[1]+': '))
                student = fields[1]+';'+fields[2]+";"
                if presence == '':
                    student += 'OK\n'
                elif presence in 'nN':
                    student += 'NOT/n'
                else:
                    student += '?\n'
                attendance.append(student)
            line = file.readline()
        return attendance

classes = list(possible_classes())
classes.sort()
for c in classes:
    print(c)

myclass = input("In which class do you want to do the check?: ")
attendance_list = control(myclass)
if len(attendance_list) == 0:
    print("This class does not exist")
else:
    with open(myclass+".csv", "w") as output:
        output.write(f'Attendance list {myclass}\n')
        output.writelines(attendance_list)