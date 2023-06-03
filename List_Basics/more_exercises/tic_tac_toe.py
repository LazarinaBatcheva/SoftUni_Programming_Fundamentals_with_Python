first_line_of_numbers = input().split()
second_line_of_numbers = input().split()
third_line_of_numbers = input().split()

winner = ""

if "1" == first_line_of_numbers[0] == first_line_of_numbers[1] == first_line_of_numbers[2] or \
    "1" == second_line_of_numbers[0] == second_line_of_numbers[1] == second_line_of_numbers[2] or \
    "1" == third_line_of_numbers[0] == third_line_of_numbers[1] == third_line_of_numbers[2] or \
    "1" == first_line_of_numbers[0] == second_line_of_numbers[0] == third_line_of_numbers[0] or \
    "1" == first_line_of_numbers[1] == second_line_of_numbers[1] == third_line_of_numbers[1] or \
    "1" == first_line_of_numbers[2] == second_line_of_numbers[2] == third_line_of_numbers[2] or \
    "1" == first_line_of_numbers[0] == second_line_of_numbers[1] == third_line_of_numbers[2] or \
    "1" == first_line_of_numbers[2] == second_line_of_numbers[1] == third_line_of_numbers[0]:
    winner = "1"

if "2" == first_line_of_numbers[0] == first_line_of_numbers[1] == first_line_of_numbers[2] or \
    "2" == second_line_of_numbers[0] == second_line_of_numbers[1] == second_line_of_numbers[2] or \
    "2" == third_line_of_numbers[0] == third_line_of_numbers[1] == third_line_of_numbers[2] or \
    "2" == first_line_of_numbers[0] == second_line_of_numbers[0] == third_line_of_numbers[0] or \
    "2" == first_line_of_numbers[1] == second_line_of_numbers[1] == third_line_of_numbers[1] or \
    "2" == first_line_of_numbers[2] == second_line_of_numbers[2] == third_line_of_numbers[2] or \
    "2" == first_line_of_numbers[0] == second_line_of_numbers[1] == third_line_of_numbers[2] or \
    "2" == first_line_of_numbers[2] == second_line_of_numbers[1] == third_line_of_numbers[0]:
    winner = "2"

if winner == "1":
    print("First player won")
elif winner == "2":
    print("Second player won")
else:
    print("Draw!")