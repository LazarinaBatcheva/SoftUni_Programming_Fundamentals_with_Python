def add_lesson(lessons_list, title):
    if title not in lessons_list:
        lessons_list.append(title)
    return lessons_list


def insert_lesson(lessons_list, title, index):
    if title not in lessons_list:
        lessons_list.insert(index, title)
    return lessons_list


def remove_lesson(lessons_list, title):
    if title in lessons_list:
        title_index = lessons_list.index(title)
        if title_index + 1 in range(len(lessons_list)):
            if "Exercise" in lessons_list[title_index + 1]:
                lessons_list.pop(title_index + 1)
        lessons_list.remove(title)
    return lessons_list


def swap_lesson(lessons_list, title1, title2):
    if title1 in lessons_list and title2 in lessons_list:
        title1_index = lessons_list.index(title1)
        title2_index = lessons_list.index(title2)
        title1_has_exercise = False
        title2_has_exercise = False
        if title1_index + 1 in range(len(lessons_list)):
            title1_has_exercise = "Exercise" in lessons_list[title1_index + 1]
        if title2_index + 1 in range(len(lessons_list)):
            title2_has_exercise = "Exercise" in lessons_list[title2_index + 1]
        lessons_list[title1_index], lessons_list[title2_index] = \
            lessons_list[title2_index], lessons_list[title1_index]
        if title1_has_exercise and title2_has_exercise:
            lessons_list[title1_index + 1], lessons_list[title2_index + 1] = \
                lessons_list[title2_index + 1], lessons_list[title1_index + 1]
        elif title1_has_exercise and not title2_has_exercise:
            lessons_list.insert(title2_index + 1, lessons_list.pop(title1_index + 1))
        elif not title1_has_exercise and title2_has_exercise:
            lessons_list.insert(title1_index + 1, lessons_list.pop(title2_index + 1))
    return lessons_list


def exercise(lessons_list, title):
    if title in lessons_list and f"{title}-Exercise" not in lessons_list:
        title_index = lessons_list.index(title)
        lessons_list.insert(title_index + 1, f"{title}-Exercise")
    elif title not in lessons_list:
        lessons_list.append(title)
        lessons_list.append(f"{title}-Exercise")
    return lessons_list


lessons = input().split(", ")
command = input()

while command != "course start":
    command = command.split(":")
    action, lesson_title = command[0], command[1]

    if len(command) > 2:
        lesson_title_or_index = command[2]

    if action == "Add":
        lessons = add_lesson(lessons, lesson_title)

    elif action == "Insert":
        lessons = insert_lesson(lessons, lesson_title, int(lesson_title_or_index))

    elif action == "Remove":
        lessons = remove_lesson(lessons, lesson_title)

    elif action == "Swap":
        lessons = swap_lesson(lessons, lesson_title, lesson_title_or_index)

    elif action == "Exercise":
        lessons = exercise(lessons, lesson_title)

    command = input()

for lesson_index, lesson in enumerate(lessons):
    print(f"{lesson_index + 1}.{lesson}")