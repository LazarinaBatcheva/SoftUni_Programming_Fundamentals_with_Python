string = input().lower()

word_sand_counter = 0
word_water_counter = 0
word_fish_counter = 0
word_sun_counter = 0

if "sand" in string:
    word_sand_counter = string.count('sand')
if "water" in string:
    word_water_counter = string.count('water')
if "fish" in string:
    word_fish_counter = string.count('fish')
if "sun" in string:
    word_sun_counter = string.count('sun')

words_counter = word_sand_counter + word_water_counter + word_fish_counter + word_sun_counter

print(words_counter)