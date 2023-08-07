def create_triangle(number):
    start_number = 1
    for num in range(1, number + 1):
        print(start_number, end=" ")
        if num <= number:
            for num1 in range(2, num + 1):
                print(num1, end=" ")
            print()
    for num in range(0, number - 1):
        print(start_number, end=" ")
        if num <= number:
            for num1 in range(2, number - num):
                print(num1, end=" ")
            print()


number_limit = int(input())
create_triangle(number_limit)