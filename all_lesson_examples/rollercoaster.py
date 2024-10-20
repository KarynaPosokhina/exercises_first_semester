number_of_trains = int(input("How many trains are available?"))
print(str(type(number_of_trains)))
number_of_seats = int(input("How many seats are available?"))
print(str(type(number_of_seats)))
boarding_time_in_seconds = 30
duration_of_trip_minutes = 2

entire_time_per_train_in_seconds = duration_of_trip_minutes * 60 + boarding_time_in_seconds
amount_of_runs_per_train = 60 * 60 / entire_time_per_train_in_seconds

total_capacity_per_hour = amount_of_runs_per_train * number_of_seats * number_of_trains


print("The total amount of people who can ride the Python per hour is: " + str(int(total_capacity_per_hour)))