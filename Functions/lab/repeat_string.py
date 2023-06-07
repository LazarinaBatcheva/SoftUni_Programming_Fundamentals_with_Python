string = input()
number = int(input())

repeat_string = lambda text, num: text * num
result = repeat_string(string, number)

print(result)