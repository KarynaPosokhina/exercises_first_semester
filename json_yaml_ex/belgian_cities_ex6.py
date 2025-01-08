import yaml

cities = {}
city_list = []

with open("belgian_cities.txt", "r") as file:
    file.readline()
    line = file.readline().rstrip()
    record = line.split(';')
    while line:
        name = record[0]
        population = record[1]
        language = record[2]
        landmarks = record[3].split(',')
        is_capital = record[4]
        if is_capital == 'Y':
            capital = True
        else:
            capital = False

        city = {'name': name,
                    'population': int(population),
                    'official_language': language,
                    'landmarks': landmarks,
                    'ia_capital': is_capital
            }
        city_list.append(city)
        line = file.readline().rstrip()
        record = line.split(';')

cities['belgian_cities'] = city_list

with open('belgian_cities2.yaml', 'w') as file:
    yaml.dump(cities, file, sort_keys=False)
