

temperature = 45

if temperature < 0:
    print("temp is below zero")
elif temperature < 10:
    print("temp is cold")
elif temperature < 15:
    print("temp is fine")
else:
    print("the temp is very cold")

match temperature:
    case 1:
        print("1 degree")
    case 2:
        print("2 degree")
    case 6:
        print("6 degrees")
    case _:
        print("no matches")

print("end of the file")