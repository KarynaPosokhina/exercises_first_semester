print('Average temperatures:')
with open('weather_2018 10.csv') as file:
    line = file.readline()

    line = file.readline().rstrip()
    date_info = line.split(';')
    while line:
        date_ind = date_info[0].split(' ')[0]
        number_of_measurements = 0
        total_of_measurements = 0
        while line and date_info[0].split(' ')[0] == date_ind:
            number_of_measurements += 1
            total_of_measurements += float(date_info[1])
            line = file.readline().rstrip()
            date_info = line.split(';')
        # end of group calculations
        average_temp = total_of_measurements / number_of_measurements
        print(date_ind + '\tnumber of measurements = ' + str(number_of_measurements) + '\taverage =',
              '{:.4}'.format(average_temp))
print(60 * '>')