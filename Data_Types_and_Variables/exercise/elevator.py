from math import ceil

number_of_person = int(input())
capacity = int(input())

courses = ceil(number_of_person / capacity)
print(courses)