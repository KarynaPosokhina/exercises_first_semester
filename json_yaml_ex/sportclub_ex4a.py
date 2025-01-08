import json

all_orders = dict()

name = input('Name of the club member: ')

while name.lower() != 'end':
    short = input("Short size: ").upper()

    match short:
        case 'XS':
            key = "short extra small"
        case 'S':
            key = "short small"
        case 'M':
            key = "short medium"
        case 'L':
            key = "short large"
        case 'XL':
            key = "extra large"

    if key:
        all_orders[key] = all_orders.get(key, 0) + 1

    tshirt = input("T-shirt size: ").upper()

    match tshirt:
        case 'XS':
            key = "short extra small"
        case 'S':
            key = "short small"
        case 'M':
            key = "short medium"
        case 'L':
            key = "short large"
        case 'XL':
            key = "extra large"

    if key:
        all_orders[key] = all_orders.get(key, 0) + 1

    backpack = input("New backpack? (Y/N): ")

    if backpack == 'y':
        all_orders["backpacks"] = all_orders.get("backpacks", 0) + 1

    print()

    name = input("Name of the club member: ")

new_order = {"Club order": all_orders}

with open("Club_order.json", "w") as file:
    json.dump(new_order, file, indent= 3)

