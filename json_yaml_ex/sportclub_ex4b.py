import json

all_orders = dict()

name = input('Name of the club member: ')
while name.lower() != 'end':
    member_order = {"shorts": {}, "tshirts": {}, "backpacks": 0}

    short = input('Short size: ').upper()
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
            key = "short extra large"
        case _:
            key = None
    if key:
        member_order["shorts"][key] = member_order["shorts"].get(key, 0) + 1

    tshirt = input('T-shirt size: ').upper()
    match tshirt:
        case 'XS':
            key = "t-shirt extra small"
        case 'S':
            key = "t-shirt small"
        case 'M':
            key = "t-shirt medium"
        case 'L':
            key = "t-shirt large"
        case 'XL':
            key = "t-shirt extra large"
        case _:
            key = None
    if key:
        member_order["tshirts"][key] = member_order["tshirts"].get(key, 0) + 1


    backpack = input('New Backpack? (Y/N) ').lower()
    if backpack == "y":
        member_order["backpacks"] += 1


    all_orders[name] = member_order

    print()
    name = input('Name of the club member: ')


new_order = {"Club orders": all_orders}


with open("Club_orders.json", "w", encoding="UTF-8") as file:
    json.dump(new_order, file, indent=3)
