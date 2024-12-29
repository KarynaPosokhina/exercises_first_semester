
with open("weather_2024_08.csv", "r") as file:
    line = file.readline()

    temperature = []
    line = file.readline()
    while line:
        date = line.split(';')
        temperature.append(date[1])
        line = file.readline()

print(f"The highest temperature in this period = {max(temperature)} °C")