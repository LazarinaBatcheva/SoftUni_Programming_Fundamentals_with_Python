def actions(value_type, value):
    if value_type == "int":
        return int(value) * 2
    elif value_type == "real":
        return f"{float(value) * 1.5:.2f}"
    else:
        return f"${value}$"


data_type = input()
number = input()

print(actions(data_type, number))