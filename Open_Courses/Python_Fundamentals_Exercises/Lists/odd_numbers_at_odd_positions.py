integers_list = [int(number) for number in input().split()]

for index in range(0, len(integers_list)):
    if index % 2 != 0:
        if integers_list[index] % 2 != 0:
            print(f"Index {index} -> {integers_list[index]}")