import re

places = input()
travel_points = 0
destinations_list = []
pattern = r"([=/])([A-Z][A-Za-z]{2,})\1"
valid_places = re.finditer(pattern, places)
for destination in valid_places:
    travel_points += len(destination[2])
    destinations_list.append(destination[2])
print("Destinations:", ", ".join(destinations_list))
print(f"Travel Points: {travel_points}")