original_list = ['cat', 'dog', 'mouse', 'rat', 'squirrel', 'owl', 'rabbit']
print(f'Original list: {original_list}')
new_list = original_list
temp = original_list[0]
new_list.pop(0)
new_list.append(temp)
print(f'After sliding: {new_list}')

