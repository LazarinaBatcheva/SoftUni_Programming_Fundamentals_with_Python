numbers = sorted([int(number) for number in input().split()], reverse=True)
if len(numbers) > 3:
    print(numbers[0], numbers[1], numbers[2])
else:
    for number in numbers:
        print(number, end=" ")