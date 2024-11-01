day = str(input("Enter the current day: "))

match day:
    case "Monday":
        print("This is a weekday. The 1st day of the week")
    case "Tuesday":
        print("This is a weekday. The 2nd day of the week")
    case "Wednesday":
        print("This is a weekday. The 3 rd day of the week.")
    case "Thursday":
        print("This is a weekday. The 4th day of the week")
    case "Friday":
        print("This is a weekday. The 5th day of the week")
    case "Saturday":
        print("This is a weekend day. The 6th day of the week")
    case "Sunday":
        print("This is a weekend day. The 7th day of the week")
    case _:
        print("Invalid entry")