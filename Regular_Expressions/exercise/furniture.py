import re

command = input()
pattern = r"\>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)\b"
total_money = 0
bought_furniture = []

while command != "Purchase":
    matches = re.search(pattern, command)
    if matches:
        furniture, price, quantity = matches.groups()
        bought_furniture.append(furniture)
        total_money += float(price) * int(quantity)
    command = input()

print("Bought furniture:")
for current_furniture in bought_furniture:
    print(current_furniture)
print(f"Total money spend: {total_money:.2f}")
