import json
import yaml

with open('matches.txt') as file:
    lines = file.readlines()

rounds = []
i = 0
record = lines[i].split(';')

while i < len(lines):

    matchday = record[0]
    matches = []

    while i < len(lines) and record[0] == matchday:

        match = dict()
        match["date"] = record[1]
        match["home"] = record[2]
        match["visitors"] = record[3]

        score = dict()
        score["final"] = record[4].rstrip()

        match["score"] = score

        matches.append(match)

        i+= 1
        if i < len(lines):
            record = lines[i].split(';')

    round = dict()
    round["name"] = matchday
    round["matches"] = matches
    rounds.append(round)

result = dict()
result["results"] = rounds

with open('matches.json', 'w', encoding="UTF-8") as file:
    json.dump(result, file, indent=3)

with open('matches.yaml', 'w', encoding="UTF-8") as file:
    yaml.dump(result, file, indent=3)

