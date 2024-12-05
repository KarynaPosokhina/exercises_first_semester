import random


def shuffle(ordered_list):
    ordered_list_length = len(ordered_list)
    shuffled_list = []
    while len(shuffled_list) < ordered_list_length:
        index = random.randint(0,len(ordered_list) - 1)
        # print(index)
        shuffled_list.append(ordered_list[index])
        ordered_list.pop(index)
        # print(f"ordered_list = {ordered_list}")

    return shuffled_list
    # random.shuffle(ordered_list)
    # return ordered_list

# result = shuffle([6,7,8,9,10,"jack","queen","king","ace"])
# print(f"result = {result}")
# [2,3,1,4]

assert(len(shuffle([]))) == 0
assert(len(shuffle([1,2]))) == 2
assert(len(shuffle([1,2,3,4]))) == 4
test_shuffled_list = shuffle([1,2,3,4])
assert(1 in test_shuffled_list) == True
assert(2 in test_shuffled_list) == True
assert(3 in test_shuffled_list) == True
assert(4 in test_shuffled_list) == True


def password_structure(structure_length):
    allowed_numbers = [1,2,3,4]
    initial_list = [1,2,3,4]
    for i in range(1, structure_length - len(allowed_numbers) + 1):
        index = random.randint(0, len(allowed_numbers) - 1)
        initial_list.append(allowed_numbers[index])

    return shuffle(initial_list)

assert(len(password_structure(4))) == 4
assert(len(password_structure(5))) == 5
assert(len(password_structure(7))) == 7
assert(len(password_structure(9))) == 9
assert(1 in password_structure(5)) == True
assert(2 in password_structure(5)) == True
assert(3 in password_structure(5)) == True
assert(4 in password_structure(5)) == True
assert(0 in password_structure(5)) == False
assert(5 in password_structure(5)) == False

result = password_structure(12)
print(f"result = {result}")
