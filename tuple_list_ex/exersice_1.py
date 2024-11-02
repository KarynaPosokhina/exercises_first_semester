original_list = ['cat', 'dog', 'mouse', 'rat', 'squirrel', 'owl', 'rabbit']
print(f' Original list: {original_list}')
original_list[0], original_list[-1] = original_list[-1], original_list[0]
print(f' After the switch: {original_list}')