def password_length(some_password):
    if len(some_password) < 6 or len(some_password) > 10:
        print("Password must be between 6 and 10 characters")
        return False
    return True


def characters_in_password(some_password):
    if not some_password.isalnum():
        print("Password must consist only of letters and digits")
        return False
    return True


def digits_in_password(some_password):
    digits_counter = 0
    for character in some_password:
        if character.isdigit():
            digits_counter += 1
    if digits_counter < 2:
        print("Password must have at least 2 digits")
        return False
    return True


password = input()

password_is_valid = [password_length(password), characters_in_password(password), digits_in_password(password)]
if all(password_is_valid):
    print("Password is valid")