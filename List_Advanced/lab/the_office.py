employees = [int(x) for x in input().split()]
happiness_factor = int(input())

employees_happiness = list(map(lambda x: x * happiness_factor, employees))
average_happiness = sum(employees_happiness) / len(employees_happiness)
happy_employees = 0

for employee in employees_happiness:
    if employee >= average_happiness:
        happy_employees += 1
        continue

if happy_employees >= len(employees) / 2:
    print(f"Score: {happy_employees}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {happy_employees}/{len(employees)}. Employees are not happy!")