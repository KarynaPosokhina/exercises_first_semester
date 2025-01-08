import yaml

with open("roller_coasters.yaml", 'r') as file:
    roller_dict = yaml.safe_load(file)

countries = roller_dict["countries"]

for country in countries:
    print(country["name"])
    print('*' * len(country['name']))
    for park in country["parks"]:
        for ride in park['ride_types']:
            for roller_coaster in ride['rollercoasters']:
              print(f'- {roller_coaster['name']} --> {roller_coaster['speed']}')

        print()
