items = input().split('|')
budget = float(input())

TRAIN_TICKET_PRICE = 150
sell_prices = []
profit = 0

for item in items:
    type_item, buying_price = item.split('->')
    buying_price = float(buying_price)
    price_is_valid = False

    if type_item == 'Clothes' and buying_price <= 50.00:
        price_is_valid = True
    elif type_item == 'Shoes' and buying_price <= 35.00:
        price_is_valid = True
    elif type_item == 'Accessories' and buying_price <= 20.50:
        price_is_valid = True

    if price_is_valid:
        if budget >= buying_price:
            budget -= buying_price
            sell_price = buying_price * 1.4
            profit += sell_price - buying_price
            sell_prices.append(sell_price)

print(' '.join([f'{sell_price:.2f}' for sell_price in sell_prices]))
print(f'Profit: {profit:.2f}')

if (budget + sum(sell_prices)) >= TRAIN_TICKET_PRICE:
    print('Hello, France!')
else:
    print('Not enough money.')