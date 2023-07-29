budget = float(input())
initial_capital = float(input())
number_of_investors = int(input())

for investor in range(1, number_of_investors + 1):
    money = float(input())

    if initial_capital < budget:
        initial_capital += money
        print(f"Investor {investor} gave us {money:.2f}.")

    if initial_capital >= budget:
        print(f"We will manage to build it. Start now! Extra money - {initial_capital - budget:.2f}.")
        break

if initial_capital < budget:
    print(f"Project can not start. We need {budget - initial_capital:.2f} more.")