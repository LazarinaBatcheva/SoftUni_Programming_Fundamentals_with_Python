number = int(input())

prime_number = True

for current_number in range(2, number):
    if number % current_number == 0:
        prime_number = False
        break

print(prime_number)