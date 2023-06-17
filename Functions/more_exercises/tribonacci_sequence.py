def tribonacci_sequence(some_number):
    numbers_list = [1, 0, 0]
    for current_number in range(some_number):
        new_number = sum(numbers_list)
        print(new_number, end=" ")
        numbers_list.append(new_number)
        numbers_list.remove(numbers_list[0])


number = int(input())

tribonacci_sequence(number)
