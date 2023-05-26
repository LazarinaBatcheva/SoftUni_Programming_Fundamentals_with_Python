budget = float(input())
flour_price = float(input())

eggs_price = flour_price * 0.75
milk_price = (flour_price * 1.25) / 4
one_bread_price = flour_price + eggs_price + milk_price

budget_left = budget
made_breads_counter = 0
colored_eggs = 0

while one_bread_price <= budget_left:
    budget_left -= one_bread_price
    made_breads_counter += 1
    colored_eggs += 3

    if made_breads_counter % 3 == 0:
        colored_eggs -= (made_breads_counter - 2)

print(f"You made {made_breads_counter} loaves of Easter bread! Now you have "
      f"{colored_eggs} eggs and {budget_left:.2f}BGN left.")