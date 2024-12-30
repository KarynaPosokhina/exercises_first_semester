with open('courses.csv') as rf:
    with open('students.csv', 'w') as wf:
        rf.readline()
        line = rf.readline().rstrip()
        record = line.split(';')
        while line:
            studentind = record[3]
            student_info = studentind+';' + record[4] + ';' + record[5]
            while line and record[3] == studentind:
                student_info += ';'+record[1]+' ('+record[2] + ')'
                line = rf.readline().rstrip()
                record = line.split(';')
            wf.write(student_info + '\n')
            print(student_info)