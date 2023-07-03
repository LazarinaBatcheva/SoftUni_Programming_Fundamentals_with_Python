command = input()
company_info = {}

while command != "End":
    company_name, employee_id = command.split(" -> ")

    if company_name not in company_info.keys():
        company_info[company_name] = []
    if employee_id not in company_info[company_name]:
        company_info[company_name].append(employee_id)

    command = input()

for company_name, employees in company_info.items():
    print(company_name)
    for employee in employees:
        print(f"-- {employee}")
