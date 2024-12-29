with open("playlist.txt", "r") as file:
    lines = file.readlines()
    print('Playlist:')
    for line in lines:
        if line != '/n':
            text = line.split(";")
            print(text[0],"\t",text[1],text[2],end="")

