integers = [int(number) for number in input().split()]
command = input()

while command != "End":
    target_index = int(command)

    if 0 <= target_index < len(integers):
        target = integers[target_index]
        integers[target_index] = -1

        for element in range(len(integers)):
            if integers[element] == -1:
                continue
            elif integers[element] > target:
                integers[element] -= target
            else:
                integers[element] += target

    command = input()

print(f"Shot targets: {sum(1 for number in integers if number == -1)} ->", *integers)
