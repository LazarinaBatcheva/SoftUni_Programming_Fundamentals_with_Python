<<<<<<< HEAD:Open_Courses/Fundamentals_of_Programming/Fundamentals_of_Programming_Exams/2_message_translator.py
import re

number_of_messages = int(input())
pattern = r"(!([A-Z][a-z]{2,})!):(\[([A-Za-z]{8,})\])"
for _ in range(number_of_messages):
    some_message = input()
    valid_message = re.findall(pattern, some_message)
    if re.fullmatch(pattern, some_message):
        for message in valid_message:
            command = message[1]
            current_message = message[3]
            print(f"{command}: ", end="")
            for letter in current_message:
                print(ord(letter), end=" ")
            print()
    else:
        print("The message is invalid")
=======
import re

number_of_messages = int(input())
pattern = r"(!([A-Z][a-z]{2,})!):(\[([A-Za-z]{8,})\])"
for _ in range(number_of_messages):
    some_message = input()
    valid_message = re.findall(pattern, some_message)
    if re.fullmatch(pattern, some_message):
        for message in valid_message:
            command = message[1]
            current_message = message[3]
            print(f"{command}: ", end="")
            for letter in current_message:
                print(ord(letter), end=" ")
            print()
    else:
        print("The message is invalid")
>>>>>>> 30199c1e940310b17e9505a02bf78db7c6ad0e14:exercises/Fundamentals_of_Programming_Exams/2_message_translator.py
