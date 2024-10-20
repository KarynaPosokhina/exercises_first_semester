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

years = 0
your_age = int(input("How old are you: "))
father_age = int(input("How old is your father: "))

if father_age / your_age < 2:
    print("The simuation is no longer possible for your ages")
else:
    while years <= 120:
        years += 1
        father_age += 1
        your_age += 1
        if father_age / your_age == 2:
            print("Within", years, "years your father will have twice your age")
            print("Your father will be", father_age, "and you will be", your_age)
            break



