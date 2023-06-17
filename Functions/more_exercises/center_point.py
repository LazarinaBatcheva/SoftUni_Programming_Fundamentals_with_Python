from math import floor


def closest_point(x1, y1, x2, y2):
    if abs(x1) + abs(y1) <= abs(x2) + abs(y2):
        return floor(x1), floor(y1)
    return floor(x2), floor(y2)


n1 = float(input())
m1 = float(input())
n2 = float(input())
m2 = float(input())

print(closest_point(n1, m1, n2, m2))