people_for_execute = input().split()
execution_number = int(input())

people_for_execute_list = [int(number) for number in people_for_execute]
executed_people = []
execution_counter = 0
current_index = 0

while len(people_for_execute_list) > 0:
    execution_counter += 1

    if current_index >= len(people_for_execute_list):
        current_index = 0

    if execution_counter % execution_number == 0:
        executed_people.append(people_for_execute_list[current_index])
        people_for_execute_list.pop(current_index)
    else:
        current_index += 1

print(str(executed_people).replace(" ", ""))