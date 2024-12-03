print(f'iwdhqdih')
name = ''
students = []
distances = []

while name != "stop":
    name = str(input("Enter your name: "))
    if name != "stop":
        distance = float(input("Enter your distance to school: "))
        students.append(name)
        distances.append(distance)

for i in range(len(students)):
    print(f"{students[i]}  {distances[i]}")

max_distance = max(distances)
max_distance_index = distances.index(max_distance)
farthest_student = students[max_distance_index]
print(f'{farthest_student} lives farthest, namely {max_distance} km')

average_distance = sum(distances) / len(distances)
print(f"The average distance is: {average_distance}")