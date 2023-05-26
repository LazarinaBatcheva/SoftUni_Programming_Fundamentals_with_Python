n = int(input())

for i in range(n):
    string = input()
    string_list = [",", ".", "_"]

    for ch in string_list:
        if ch in string:
            print(f"{string} is not pure!")
            break
    else:
        print(f"{string} is pure.")