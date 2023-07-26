def calculated_left_part(left):
    left_part_list = []
    middle_index = len(left) // 2
    left_part = left[:middle_index][::-1]
    right_part = left[middle_index:]
    for index in range(len(right_part)):
        left_part_result = right_part[index] + left_part[index]
        left_part_list.append(left_part_result)
    return left_part_list


def calculated_right_part(right):
    right_part_list = []
    middle_index = len(right) // 2
    right_part = right[middle_index:][::-1]
    left_part = right[:middle_index]
    for index in range(len(left_part)):
        right_part_result = left_part[index] + right_part[index]
        right_part_list.append(right_part_result)
    return right_part_list


def base_function(numbers_list):
    result = ""
    middle_index = len(numbers) // 2
    left_part = numbers[:middle_index]
    right_part = numbers[middle_index:]
    left_part_list = calculated_left_part(left_part)
    right_part_list = calculated_right_part(right_part)
    result = left_part_list + right_part_list
    for number in result:
        print(number, end=" ")


numbers = [int(number) for number in input().split()]
base_function(numbers)
