MAX_NUMBER_OF_MEMBERS = 4
DISCOUNT = 0.1 # 10%

fee = 0

for i in range(MAX_NUMBER_OF_MEMBERS):
    name = str(input("Name: "))
    age = int(input("Age: "))
    years = int(input("Member for how many years: "))

    if age < 12:
        fee = 20
    elif 12 <= age <= 18:
        fee = 50
    else:
        fee = 95

    if years >= 5:
        fee = fee - fee * DISCOUNT


    print(f"Member fee for {name} - {fee} \n")