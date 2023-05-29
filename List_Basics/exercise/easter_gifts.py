gifts = input().split()

while True:
    string = input()
    if string == 'No Money':
        break

    command = string.split()

    gift_in_command = command[1]
    if command[0] == 'OutOfStock':
        gift_index = -1
        for index in range(len(gifts)):
            if gifts[index] == gift_in_command:
                gift_index = index

            if gift_index != -1:
                gifts[gift_index] = 'None'

    elif command[0] == 'Required':
        index_in_command = int(command[2])
        if 0 <= index_in_command < len(gifts):
            gifts[index_in_command] = gift_in_command
    elif command[0] == 'JustInCase':
        gifts[-1] = gift_in_command

for gift in gifts:
    if gift == 'None':
        continue
    print(gift, end=' ')