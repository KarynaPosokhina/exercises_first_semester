MAIN_NUMBER = 4

numbers = (1, 2, 3, 4, 5, 4, 6, 7, 8)
# numbers = (4, 2, 3, 9, 1, 4)
# numbers = (4, 2, 3, 9, 1, 6, 7, 8)
# numbers = (2, 3, 7, 5, 6, 1, 9)
isPresent = False
for n in numbers:
    if n == MAIN_NUMBER:
        isPresent = True

if isPresent:
    num_list = list(numbers)

    num_list.reverse()
    number_index_reversed = num_list.index(MAIN_NUMBER)

    # print(number_index_reversed)
    num_list.reverse()
    print(num_list)

    number_index = len(num_list) - number_index_reversed - 1
    # print(number_index)

    new_list = num_list[number_index + 1:]
    # print(new_list)
    new_tuple = tuple(new_list)
    print(new_tuple)
else:
    print(f"The number {MAIN_NUMBER} does not appear in the Tuple")