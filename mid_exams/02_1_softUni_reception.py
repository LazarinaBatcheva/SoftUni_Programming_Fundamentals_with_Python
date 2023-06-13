first_employee, second_employee, third_employee = int(input()), int(input()), int(input())
students = int(input())

answers_per_hour = first_employee + second_employee + third_employee
time_needed = 0

while students > 0:
    if students > 0:
        time_needed += 1
        if time_needed % 4 == 0:
            time_needed += 1
    students -= answers_per_hour

print(f"Time needed: {time_needed}h.")


# first_employee, second_employee, third_employee = int(input()), int(input()), int(input())
# students = int(input())

# answers_per_hour = first_employee + second_employee + third_employee

# working_hours = 0  # work without break - 3 hours
# time_needed_to_answers = 0

# while students > 0:
#     if working_hours == 3:
#         time_needed_to_answers += 1
#         working_hours = 0
#         continue

#     working_hours += 1
#     time_needed_to_answers += 1
#     students -= answers_per_hour

# print(f"Time needed: {time_needed_to_answers}h.")
