def add_clothes(clothes_, clothes_info):
    color, items = clothes_[0], clothes_[1].split(",")
    if color not in clothes_info.keys():
        clothes_info[color] = {}
    for clothing in items:
        if clothing not in clothes_info[color]:
            clothes_info[color][clothing] = 0
        clothes_info[color][clothing] += 1
    return clothes_info


def show_result(items):
    needed_color, needed_dress = items[0], items[1]
    for color in clothes_info_dict.keys():
        print(f"{color} clothes:")
        for dress, count in clothes_info_dict[color].items():
            if color == needed_color and dress == needed_dress:
                print(f"* {dress} - {count} (found!)")
            else:
                print(f"* {dress} - {count}")


number_of_lines = int(input())
clothes_info_dict = {}

for i in range(number_of_lines):
    clothes = input().split(" -> ")
    clothes_info_dict = add_clothes(clothes, clothes_info_dict)

show_result(input().split())
