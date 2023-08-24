integers_list = [int(number) for number in input().split()]
positive_numbers = []

for number in integers_list:
    if number >= 0:
        positive_numbers.append(number)

if positive_numbers:
    positive_numbers = positive_numbers[::-1]
    for number in positive_numbers:
        print(number, end=" ")
else:
    print("empty")