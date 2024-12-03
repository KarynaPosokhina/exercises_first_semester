import random


def roll_dice(number_of_dices):
    result = []
    for i in range(number_of_dices):
        result.append(random.randint(1,6))
    return result


def is_poker(rolls):
    if len(rolls) == 0:
        return False

    result = True
    for roll in rolls:
        if rolls[0] != roll:
            result = False
    return result


# def is_poker(rolls):
#     if len(rolls) == 0:
#         return False
#     return all(roll == rolls[0] for roll in rolls)

assert(is_poker([1,2,3])) == False
assert(is_poker([1,2,1])) == False
assert(is_poker([2,2,2])) == True
assert(is_poker([1,2,2])) == False
assert(is_poker([1,1,2])) == False
assert(is_poker([])) == False


counter = 0
dices = int(input("How many dices you want to work with: "))
roll_result = roll_dice(dices)

while not is_poker(roll_result):
    roll_result = roll_dice(dices)
    counter += 1
    print(f"{counter} - {roll_result}")

print(f"After {counter} rolls we got a poker!")
