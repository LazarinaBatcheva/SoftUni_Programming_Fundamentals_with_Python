from math import ceil

students = int(input())
lectures = int(input())
additional_bonus = int(input())

max_bonus_points = 0
attendances = 0

for i in range(students):
    student_attendances = int(input())
    total_bonus = student_attendances / lectures * (5 + additional_bonus)
    if total_bonus > max_bonus_points:
        max_bonus_points = total_bonus
        attendances = student_attendances

print(f"Max Bonus: {ceil(max_bonus_points)}.")
print(f"The student has attended {attendances} lectures.")