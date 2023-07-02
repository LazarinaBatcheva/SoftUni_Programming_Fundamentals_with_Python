command = input().split()
information = {}

while command[0] != "buy":
    product, price, quantity = command[0], float(command[1]), int(command[2])

    if product not in information.keys():
        information[product] = [price, quantity]
    else:
        information[product][0] = price
        information[product][1] += quantity

    command = input().split()

for key, value in information.items():
    total_price = value[0] * value[1]
    print(f"{key} -> {total_price:.2f}")