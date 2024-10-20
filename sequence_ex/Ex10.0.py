FIXED_AMOUNT = 83.6
AT_NIGHT = 0.073
DURING_THE_DAY = 0.146
VAT_PAYMENT = 1.6 # 6%

consuption_day = int(input("Power consuption during the day (killowatt/h): "))
consuption_night = int(input("Power consuption during the day (kilowatt/h): "))

daily = round(consuption_day * DURING_THE_DAY, 2)
night = round(consuption_night * AT_NIGHT, 2)
excluding_vat = round(FIXED_AMOUNT + daily + night, 2)
including_vat = round(excluding_vat * VAT_PAYMENT, 2)

print(f"Fixed costs: {FIXED_AMOUNT}€")
print(f"Daily consumption: {daily}€")
print(f"Night consumption: {night}€")
print(f"Total excluding VAT: {excluding_vat}€")
print(f"Total including VAT: {including_vat}€")