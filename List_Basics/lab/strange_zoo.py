tail = input()
body = input()
head = input()

strings_list = [tail, body, head]
strings_list[0], strings_list[2] = strings_list[2], strings_list[0]

print(strings_list)