with open("hamlet.txt", "r") as rf:
    lines = rf.readlines()
    with open("hamlet2.txt", "w") as wf:
        for line in lines:
            for character in ",.;!:'?":
                line = line.replace(character, ' ')
            wf.write(line)

