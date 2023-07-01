def correct_lab_bounds(row, col, lab):
    return row < 0 or col < 0 or row >= len(lab) or col >= len(lab[0])


def check_wall(row, col, lab):
    return lab[row][col] in "--"


def visited_positions(row, col, lab):
    return lab[row][col] == "v"


def find_way_out(row, col, lab):
    return lab[row][col] == "."


def find_path(row, col, lab):
    if correct_lab_bounds(row, col, lab) or check_wall(row, col, lab) or visited_positions(row, col, lab):
        return

    steps.append(1)

    if find_way_out(row, col, lab):
        largest_count_of_dots.append(sum(steps))

    lab[row][col] = "v"
    find_path(row, col + 1, lab)    # right check
    find_path(row, col - 1, lab)    # left check
    find_path(row + 1, col, lab)    # check up
    find_path(row - 1, col, lab)    # check down


number_of_rows = int(input())

lab_list = []
largest_count_of_dots = [0]

for current_row in range(number_of_rows):
    lab_list.append(list(input().split()))
col_range = len(lab_list[0])

for current_row in range(len(lab_list)):
    for current_col in range(col_range):
        steps = []
        if not check_wall(current_row, current_col, lab_list):
            find_path(current_row, current_col, lab_list)

print(max(largest_count_of_dots))