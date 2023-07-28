command = input()

while command != "stop playing":
    numbers = [int(number) for number in command.split() if number.strip()]
    unique_numbers = set(numbers)
    if len(numbers) == len(unique_numbers):
        updated_numbers = [num + 2 if num % 2 == 0 else num for num in numbers]
        updated_numbers = sorted(updated_numbers)
        unique_list_str = ",".join(map(str, updated_numbers))
        print(f"Unique list: {unique_list_str}")
    else:
        updated_numbers = [num + 3 if num % 2 != 0 else num for num in numbers]
        updated_numbers = sorted(updated_numbers)
        non_unique_list_str = ":".join(map(str, updated_numbers))
        print(f"Non-unique list: {non_unique_list_str}")
    average = sum(updated_numbers) / len(updated_numbers)
    print(f"Output: {average:.2f}")
    command = input()