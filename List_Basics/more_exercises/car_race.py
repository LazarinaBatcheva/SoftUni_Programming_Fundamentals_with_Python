sequence_of_numbers = input().split()

time_of_left_racer = 0
time_of_right_racer = 0

middle_of_sequence = len(sequence_of_numbers) // 2
left_side_of_sequence = sequence_of_numbers[:middle_of_sequence]
right_side_of_sequence = sequence_of_numbers[::-1][:middle_of_sequence]

for number_in_left_side in left_side_of_sequence:
    current_left_number = int(number_in_left_side)
    if current_left_number == 0:
        time_of_left_racer *= 0.80
    time_of_left_racer += current_left_number

for number_in_right_side in right_side_of_sequence:
    current_right_number = int(number_in_right_side)
    if current_right_number == 0:
        time_of_right_racer *= 0.80
    time_of_right_racer += current_right_number

if time_of_left_racer < time_of_right_racer:
    print(f"The winner is left with total time: {time_of_left_racer:.1f}")

elif time_of_left_racer > time_of_right_racer:
    print(f"The winner is right with total time: {time_of_right_racer:.1f}")
