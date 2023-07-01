def correct_lab_bounds(current_row, current_col, lab):
    return current_row < 0 or current_col < 0 or current_row >= len(lab) or current_col >= len(lab[0])


def check_wall(current_row, current_col, lab):
    return lab[current_row][current_col] in "#v"


def find_way_out(current_row, current_col, lab):
    return current_row == 0 or current_row == len(lab) - 1 or current_col == 0 or current_col == len(lab[0])


def find_starting_point():
    for pos_row, row in enumerate(maze):
        for pos_col, col in enumerate(row):
            if col == "k":
                return pos_row, pos_col


def find_lab_path(current_row, current_col, lab):
    if correct_lab_bounds(current_row, current_col, lab) or check_wall(current_row, current_col, lab):
        return
    steps.append(1)

    if find_way_out(current_row, current_col, lab):
        path_length.append(sum(steps))

    lab[current_row][current_col] = "v"
    find_lab_path(current_row, current_col + 1, lab)    # right check
    find_lab_path(current_row, current_col - 1, lab)    # left check
    find_lab_path(current_row + 1, current_col, lab)    # check up
    find_lab_path(current_row - 1, current_col, lab)    # check down
    lab[current_row][current_col] = " "

    steps.pop()


rows = int(input())

maze, steps, path_length = [], [], []
for _ in range(rows):
    maze.append(list(input()))
col = len(maze[0])

start_row, start_col = find_starting_point()

find_lab_path(start_row, start_col, maze)

if path_length:
    print(f"Kate got out in {max(path_length)} moves")
else:
    print("Kate cannot get out")