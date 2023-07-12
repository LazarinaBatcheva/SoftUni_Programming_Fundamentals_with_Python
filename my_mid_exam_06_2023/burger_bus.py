def profit(cities_count):
    total_profit = 0
    for city in range(1, number_of_cities + 1):
        name_of_the_city = input()
        incomes = float(input())
        expenses = float(input())
        if city % 5 == 0:
            incomes -= incomes * 0.1

        elif city % 3 == 0:
            expenses += expenses * 0.5

        current_profit = incomes - expenses
        total_profit += current_profit
        print(f"In {name_of_the_city} Burger Bus earned {current_profit:.2f} leva.")
    print(f"Burger Bus total profit: {total_profit:.2f} leva.")


number_of_cities = int(input())
profit(number_of_cities)


# number_of_cities = int(input())
#
# total_profit = 0
#
# for city in range(1, number_of_cities + 1):
#     name_of_the_city = input()
#     incomes = float(input())
#     expenses = float(input())
#
#     if city % 5 == 0:
#         incomes -= incomes * 0.1
#
#     elif city % 3 == 0:
#         expenses += expenses * 0.5
#
#     current_profit = incomes - expenses
#     total_profit += current_profit
#
#     print(f"In {name_of_the_city} Burger Bus earned {current_profit:.2f} leva.")
#
# print(f"Burger Bus total profit: {total_profit:.2f} leva.")