import re

text_string = input()

total_calories = 0
days = 0
food_info_list = list()
pattern = re.compile(r"([|#])(?P<food_name>[A-Za-z\s]+)\1"
                     r"(?P<date>\d{2}/\d{2}/\d{2})"
                     r"\1(?P<calories>[\d]+)\1")
match = re.finditer(pattern, text_string)
for food_info in match:
    total_calories += int(food_info["calories"])
    food_info_list.append({"name": food_info["food_name"],
                           "date": food_info["date"],
                           "calories": food_info["calories"]})
days = total_calories // 2000
print(f"You have food to last you for: {days} days!")
for food in food_info_list:
    print(f"Item: {food['name']}, Best before: {food['date']}, Nutrition: {food['calories']}")
