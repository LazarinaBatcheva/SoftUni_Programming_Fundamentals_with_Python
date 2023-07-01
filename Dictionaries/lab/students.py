student_information = input()

course_dic = {}

while not course_dic.get(student_information):
    student_information = student_information.split(":")
    student_name = student_information[0]
    student_id = student_information[1]
    course = student_information[2]
    if course not in course_dic:
        course_dic[course] = {}
    course_dic[course][student_name] = student_id

    student_information = input()
    student_information = student_information.replace("_", " ")

for key, value in course_dic[student_information].items():
    print(f"{key} - {value}")