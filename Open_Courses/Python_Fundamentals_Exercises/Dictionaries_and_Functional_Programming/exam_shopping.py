def stocking_up(current_product, current_quantity, products_info):
    if current_product not in products_info.keys():
        products_info[current_product] = 0
    products_info[current_product] += current_quantity
    return products_info


def selling(current_product, current_quantity, products_info):
    if current_product in products_info.keys():
        if products_info[current_product] > 0:
            products_info[current_product] -= current_quantity
        else:
            print(f"{product} out of stock")
    else:
        print(f"{product} doesn't exist")
    return products_info


command = input()
products_info_dict = {}

while command != "exam time":
    if command != "shopping time":
        action = command.split()
        product, quantity = action[1], int(action[2])
        if action[0] == "stock":
            products_info_dict = stocking_up(product, quantity, products_info_dict)
        elif action[0] == "buy":
            products_info_dict = selling(product, quantity, products_info_dict)
    command = input()

for key, value in products_info_dict.items():
    if products_info_dict[key] > 0:
        print(f"{key} -> {value}")