# FIXED_AMOUNT = 83.6
# AT_NIGHT = 0.073
# DURING_THE_DAY = 0.146
# VAT_PAYMENT = 1.6 # 6%
#
# consuption_day = int(input("Power consuption during the day (killowatt/h): "))
# consuption_night = int(input("Power consuption during the day (kilowatt/h): "))
#
# daily = round(consuption_day * DURING_THE_DAY, 2)
# night = round(consuption_night * AT_NIGHT, 2)
# excluding_vat = round(FIXED_AMOUNT + daily + night, 2)
# including_vat = round(excluding_vat * VAT_PAYMENT, 2)
#
# print(f"Fixed costs: {FIXED_AMOUNT}€")
# print(f"Daily consumption: {daily}€")
# print(f"Night consumption: {night}€")
# print(f"Total excluding VAT: {excluding_vat}€")
# print(f"Total including VAT: {including_vat}€"

day_consumption = int(input("Power consumption during the day (kilowatt per hour): "))
night_consumption = int(input("Power consumption at night (kilowatt per hour): "))
fixed_costs = 83.6
day_costs = day_consumption * 0.146
night_costs = night_consumption * 0.073
total_excluding_vat = fixed_costs + day_costs + night_costs
total_including_vat = total_excluding_vat * 1.06

print("Invoice\n*******")
print("Fixed costs: €" + str(fixed_costs))
print("Daily consumption: €" + str(day_costs))
print("Night consumption: €" + str(night_costs))
print("Total excluding VAT: €" + str(total_excluding_vat))
print("Total including VAT: €" + str(total_including_vat))