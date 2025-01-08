import json

with open("plants.json", "r") as json_file:
    data = json.load(json_file)

datadict = data["catalog"]
counter = 1

for plant in datadict:
    if plant.get("light") == "SUN":
        print(f'Plant number {counter}: ')
        print("\t" "Name: " + plant.get("common"))
        print("\t" "Light: " + plant.get("light"))
        print("\t" "Price: " + str(plant.get("price")))

        # print(f"Plant number {counter}:")
        # print("\t", "common " + plant.get("common"))
        # print("\t", "botanical " + plant.get("botanical"))
        # print("\t", "zone " + str(plant.get("zone")))
        # print("\t", "light " + plant.get("light"))
        # print("\t", "price " + str(plant.get("price")))
        # print("\t", "availability " + plant.get("availability"))

        counter += 1