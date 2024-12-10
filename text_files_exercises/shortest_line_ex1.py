with open("irish_song.txt", "r") as file:
    line = file.readline().strip()
    shortest_line = line
    shortest_length = len(line)

    line = file.readline().strip()
    while line:
        length = len(line)
        if length > shortest_length:
            shortest_length = length
            shortest_line = line

        line = file.readline().strip()

print(f"The shortest line has {shortest_length} lines")
print(shortest_line)


