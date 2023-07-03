command = input()
courses_info = {}

while command != "end":
    course, student = command.split(" : ")

    if course not in courses_info.keys():
        courses_info[course] = []
    courses_info[course].append(student)

    command = input()

for course, students in courses_info.items():
    print(f"{course}: {len(students)}")
    for student in students:
        print(f"-- {student}")