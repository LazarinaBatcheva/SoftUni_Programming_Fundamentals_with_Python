import re

orders = input()
total_income = 0
pattern = re.compile(
    r"(%)(?P<customer>[A-Z][a-z]+)\1([^\|\$\%\.]*)"
    r"<(?P<product>[\w]+)>([^\|\$\%\.]*)"
    r"\|(?P<count>[\d]+)\|([^\|\$\%\.]*)"
    r"(?P<price>[1-9]+[.0-9]*)\$")

while orders != "end of shift":
    match = re.finditer(pattern, orders)
    for order in match:
        order_price = int(order["count"]) * float(order["price"])
        print(f"{order['customer']}: {order['product']} - {order_price:.2f}")
        total_income += order_price

    orders = input()
print(f"Total income: {total_income:.2f}")