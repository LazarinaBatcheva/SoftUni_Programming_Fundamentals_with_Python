def calculated_triangle_area(base, height):
    area = base * height / 2
    print(f"{area:.12g}")


base_triangle = float(input())
height_triangle = float(input())
calculated_triangle_area(base_triangle, height_triangle)