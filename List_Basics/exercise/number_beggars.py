integers_as_string = input().split(', ')
count_of_beggars = int(input())

profit_of_beggars = []

for element in integers_as_string:
    profit_of_beggars.append(int(element))

total_sum = []
start_index = 0

while start_index < count_of_beggars:
    sum_for_current_beggar = 0
    for current_beggar in range(start_index, len(profit_of_beggars), count_of_beggars):
        sum_for_current_beggar += profit_of_beggars[current_beggar]
    total_sum.append(sum_for_current_beggar)
    start_index += 1

print(total_sum)