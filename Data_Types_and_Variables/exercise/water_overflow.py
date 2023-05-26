number_of_lines = int(input())

water_tank_capacity = 255
filled_capacity = 0

for i in range(number_of_lines):
    litters_of_water = int(input())
    if water_tank_capacity - litters_of_water < 0:
        print('Insufficient capacity!')
        continue
    water_tank_capacity -= litters_of_water
    filled_capacity += litters_of_water
print(f'{filled_capacity}')