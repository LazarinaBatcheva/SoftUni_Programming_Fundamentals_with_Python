strings_list = input().split()
list_items = strings_list.pop()
strings_list.insert(0, list_items)
print(" ".join(strings_list))