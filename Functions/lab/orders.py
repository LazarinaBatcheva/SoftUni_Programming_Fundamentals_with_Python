type_of_product = input()
quantity_of_the_product = int(input())

# coffee_price = 1.50
# water_price = 1.00
# coke_price = 1.40
# snacks_price = 2.00


def total_price(product, quantity):
    result = None
    if product == "coffee":
        result = quantity * 1.50
    elif product == "water":
        result = quantity
    elif product == "coke":
        result = quantity * 1.40
    elif product == "snacks":
        result = quantity * 2.00
    return f"{result:.2f}"


print(total_price(type_of_product, quantity_of_the_product))