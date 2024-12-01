def convert(amount_in_euro, dollar_rate):
    return amount_in_euro * dollar_rate

assert convert(965,1.2327) == 1189.5555
assert convert(200,1.1234) == 224.67999999999998
assert convert(350,1.4321) == 501.23499999999996

rate = float(input("Current dollar rate (€ -> $):"))
amount = int(input("Your amount in Euro: "))
print("€", amount, "=", convert(amount,rate))
