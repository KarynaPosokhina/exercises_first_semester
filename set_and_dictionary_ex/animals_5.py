animal_sounds = {}

with open("animal_sounds.txt", 'r') as file:
    for line in file:
        animal, sound = line.strip().split(';')
        animal_sounds[animal] = sound

score = 0
print("Do you know the animal sounds?")

for animal in animal_sounds:
    sound = input(f"What is the sound of a {animal} ")
    if sound == animal_sounds[animal]:
        score += 1

print(f"You have {score} correct answers")