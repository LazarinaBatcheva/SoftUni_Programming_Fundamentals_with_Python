command = input()
ref_dict = {}

while command != "end":
    action, amount = command.split(" = ")
    if amount.isdigit():
        amount = int(amount)
        if action not in ref_dict.keys():
            ref_dict[action] = 0
        ref_dict[action] = amount
    else:
        if amount in ref_dict.keys():
            ref_dict[action] = ref_dict[amount]
    command = input()

for key, value in ref_dict.items():
    print(f"{key} === {value}")