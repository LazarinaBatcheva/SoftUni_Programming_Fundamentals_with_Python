email = input()
at_index = email.find('@')
before_sum = sum(ord(char) for char in email[:at_index])
after_sum = sum(ord(char) for char in email[at_index + 1:])
if before_sum >= after_sum:
    print("Call her!")
else:
    print("She is not the one.")