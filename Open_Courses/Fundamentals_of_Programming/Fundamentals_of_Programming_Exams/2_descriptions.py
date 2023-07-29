import re

command = input()
name_pattern = r"name\sis\s([A-Z][a-z]+\s[A-Z][a-z]+)"
years_pattern = r"\s(\d{2})\syears"
date_pattern = r"on\s(\d{2}-\d{2}-\d{4})."
data_base = []

while command != "make migrations":
    description_of_people = command
    name_match = re.findall(name_pattern, description_of_people)
    years_match = re.findall(years_pattern, description_of_people)
    date_match = re.findall(date_pattern, description_of_people)
    if name_match and years_match and date_match:
        data_base.append([name_match[0], years_match[0], date_match[0]])
    command = input()

if data_base:
    for name, age, date in data_base:
        print(f"Name of the person: {name}.")
        print(f"Age of the person: {age}.")
        print(f"Birthdate of the person: {date}.")
else:
    print("DB is empty")
