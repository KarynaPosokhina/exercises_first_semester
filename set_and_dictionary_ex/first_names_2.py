with open("first_names1ITF.txt", 'r') as file_1:
    list_1_itf = file_1.readlines()
with open("first_names2ITF.txt", 'r') as file_2:
    list_2_itf = file_2.readlines()

set_1 = set(list_1_itf)
set_2 = set(list_2_itf)

print(f'In 1ITF there are: {len(set_1)} different first names')
print(f'In 2ITF there are {len(set_2)} different first names')

set_popular = set_1 & set_2
print(f'These are the {len(set_popular)} first names in both 1ITF & 2ITF')

sorted_names = sorted(list(set_popular))
for popular_name in sorted_names:
    print(popular_name.rstrip())