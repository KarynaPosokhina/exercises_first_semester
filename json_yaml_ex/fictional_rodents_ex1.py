import json

with open("fictional_rodents.json") as json_file:
    my_file = json.load(json_file)

# for text in my_file:
#     print(text)
#     details = my_file[text]
#     for detail in details:
#         character = detail.get("Character")
#         notes = detail.get("Notes")
#         print(f"\t{character}: {notes}")

new_squirrel = {
    "character": "Felldoh",
    "author": "Brian Jacques",
    "work": "Martin the Warrior",
    "notes": "A young red squirrel"
}

my_file["Squirrels"].append(new_squirrel)

with open("fictional_rodents.json", 'w') as json_file:
    json.dump(my_file, json_file, indent = 4)
