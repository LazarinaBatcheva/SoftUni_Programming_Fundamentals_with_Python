integers = [int(number) for number in input().split()]

removed_numbers_sum = 0

while integers:
    index = int(input())
    removed_element = 0

    if 0 <= index < len(integers):
        removed_element = integers.pop(index)
    elif index < 0:
        removed_element = integers.pop(0)
        integers.insert(0, integers[-1])
    elif index >= len(integers):
        removed_element = integers.pop(-1)
        integers.append(integers[0])

    new_integers_list = []
    for element in integers:
        if element <= removed_element:
            element += removed_element
        else:
            element -= removed_element
        new_integers_list.append(element)
    integers = new_integers_list

    removed_numbers_sum += removed_element

print(removed_numbers_sum)