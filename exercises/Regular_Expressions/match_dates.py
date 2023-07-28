import re

dates = input()
pattern = re.compile(r"\b(?P<day>\d{2})([./-])"
                     r"(?P<month>[A-Z][a-z]{2})\2"
                     r"(?P<year>\d{4})\b")
dates_matches = re.finditer(pattern, dates)
if dates_matches:
    for date in dates_matches:
        day = date["day"]
        month = date["month"]
        year = date["year"]
        print(f"Day: {day}, Month: {month}, Year: {year}")