def found_bigger(first, second):
    if first > second:
        return first
    else:
        return second


def base_function(v_type):
    first = input()
    second = input()
    if v_type == "int":
        result = found_bigger(int(first), int(second))
    elif v_type == "char":
        result = found_bigger(first, second)
    else:
        result = found_bigger(first, second)
    return result


values_type = input()
print(base_function(values_type))



# def found_bigger_int(first, second):
#     first, second = int(first), int(second)
#     if first > second:
#         return first
#     else:
#         return second


# def found_bigger_char(first, second):
#     if ord(first) > ord(second):
#         return first
#     else:
#         return second


# def found_bigger_string(first, second):
#     if first > second:
#         return first
#     else:
#         return second


# def base_function(v_type):
#     first = input()
#     second = input()
#     if v_type == "int":
#         result = found_bigger_int(first, second)
#     elif v_type == "char":
#         result = found_bigger_char(first, second)
#     else:
#         result = found_bigger_string(first, second)
#     return result


# values_type = input()
# print(base_function(values_type))
