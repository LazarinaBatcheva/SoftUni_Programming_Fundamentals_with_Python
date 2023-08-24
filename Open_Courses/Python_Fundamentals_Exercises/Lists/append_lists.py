integers_lists = input().split("|")
new_list = []

for lst in integers_lists[::-1]:
    lst = lst.split()
    new_list.append(lst)

for lst in new_list:
    for number in lst:
        print(number, end=" ")