# years = 0
# flag = False
# your_age = int(input("How old are you: "))
# father_age = int(input("How old is your father: "))
#
# while years <= 120:
#     years += 1
#     father_age += 1
#     your_age += 1
#     if father_age / your_age == 2:
#         flag = True
#         print("Within", years, "years your father will have twice your age")
#         print("Your father will be", father_age, "and you will be", your_age)
#         break
#
# if flag == False:
#     print("The simuation is no longer possible for your ages")

my_age = int(input("how old are you? "))
father_age = int(input("how old is ur father? "))
if father_age / my_age < 2:
    print("the situation is no longer possible")
else:
    i = 0
    while father_age / my_age > 2:
        i += 1
        father_age += 1
        my_age +=1
    print(f"within {i} years, your father will have twice your age")
    print(f"your father will be {father_age} and you will be {my_age}")



