from math import floor


def longer_line(arg1, arg2, arg3, arg4):
    first_line = arg1 + arg2
    second_line = arg3 + arg4
    if first_line >= second_line:
        if arg1 <= arg2:
            return f"({floor(a1)}, {floor(b1)})({floor(a2)}, {floor(b2)})"
        return f"({floor(a2)}, {floor(b2)})({floor(a1)}, {floor(b1)})"
    elif second_line >= first_line:
        if arg3 <= arg4:
            return f"({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})"
        return f"({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y1)})"


a1, b1, a2, b2 = float(input()), float(input()), float(input()), float(input())
x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())

ab1_sum = abs(a1) + abs(b1)
ab2_sum = abs(a2) + abs(b2)
xy1_sum = abs(x1) + abs(y1)
xy2_sum = abs(x2) + abs(y2)

print(longer_line(ab1_sum, ab2_sum, xy1_sum, xy2_sum))