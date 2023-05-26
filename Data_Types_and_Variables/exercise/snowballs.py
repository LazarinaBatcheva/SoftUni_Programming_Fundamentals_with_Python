number_of_snowballs = int(input())

max_snowball_weight = 0
max_snowball_time = 0
max_snowball_quality = 0
max_snowball_value = 0

for current_snowball in range(number_of_snowballs):
    current_weight = int(input())
    current_time = int(input())
    current_quality = int(input())

    current_snowball_value = (current_weight // current_time) ** current_quality
    if current_snowball_value > max_snowball_value:
        max_snowball_weight = current_weight
        max_snowball_time = current_time
        max_snowball_quality = current_quality
        max_snowball_value = current_snowball_value

print(f'{max_snowball_weight} : {max_snowball_time} = {max_snowball_value} ({max_snowball_quality})')