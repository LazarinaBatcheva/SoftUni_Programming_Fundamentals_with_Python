integers = [int(x) for x in input().split()]

integers = sorted(integers, reverse=True)
greatest_number = []
average_number = sum(integers) / len(integers)

for number in integers:
    if number > average_number:
        greatest_number.append(number)
        if len(greatest_number) == 5:
            break

if greatest_number:
    print(*greatest_number)
else:
    print("No")