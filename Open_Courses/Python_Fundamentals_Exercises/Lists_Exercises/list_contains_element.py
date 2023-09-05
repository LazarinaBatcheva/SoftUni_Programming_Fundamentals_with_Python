list_of_integers = [int(num) for num in input().split()]
number = int(input())

if number in list_of_integers:
    print("yes")
else:
    print("no")