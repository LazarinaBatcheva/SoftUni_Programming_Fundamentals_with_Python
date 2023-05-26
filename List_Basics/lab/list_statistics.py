number_of_lines = int(input())

positives_numbers = []
negatives_numbers = []

for i in range(number_of_lines):
    current_number = int(input())
    if current_number >= 0:
        positives_numbers.append(current_number)
    elif current_number < 0:
        negatives_numbers.append(current_number)

print(positives_numbers)
print(negatives_numbers)
print(f'Count of positives: {len(positives_numbers)}\nSum of negatives: {sum(negatives_numbers)}')