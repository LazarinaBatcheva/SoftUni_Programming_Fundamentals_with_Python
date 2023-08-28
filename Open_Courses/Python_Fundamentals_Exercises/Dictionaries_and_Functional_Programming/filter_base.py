def add_person_info(name, info, persons_info):
    if info.isdigit():
        persons_info["Age"][name] = info
    elif info.isalpha():
        persons_info["Position"][name] = info
    else:
        persons_info["Salary"][name] = info
    return persons_info


def show_result(case):
    for name, info in persons_info_dict[case].items():
        print(f"Name: {name}\n{case}: {info}\n{'=' * 20}")


command = input()
persons_info_dict = {"Age": {}, "Salary": {}, "Position": {}}

while command != "filter base":
    current_name, information = command.split(" -> ")
    persons_info_dict = add_person_info(current_name, information, persons_info_dict)
    command = input()

show_result(input())