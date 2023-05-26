animals = input()

animal_type = 0
sheep_in_danger_counter = 0

animals_list = animals.split(', ')
animals_list_reversed = list(reversed(animals_list))
number_of_animals = len(animals_list)

if animals_list_reversed[0] == 'wolf':
    print('Please go away and stop eating my sheep')

else:
    for i in range(number_of_animals):
        animal_type = animals_list_reversed[i]
        sheep_in_danger_counter += 1
        if animal_type == 'wolf':
            sheep_in_danger_counter = i
            print(f'Oi! Sheep number {sheep_in_danger_counter}! You are about to be eaten by a wolf!')
