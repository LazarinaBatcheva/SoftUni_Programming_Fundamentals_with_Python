command = input()
users_info_dict = {}

while command != "login":
    username, password = command.split(" -> ")
    if username not in users_info_dict.keys():
        users_info_dict[username] = ""
    users_info_dict[username] = password
    command = input()

user = input()
login_filed_count = 0

while user != "end":
    username, password = user.split(" -> ")
    if username in users_info_dict.keys():
        if users_info_dict[username] == password:
            print(f"{username}: logged in successfully")
        else:
            print(f"{username}: login failed")
            login_filed_count += 1
    else:
        print(f"{username}: login failed")
        login_filed_count += 1
    user = input()

print(f"unsuccessful login attempts: {login_filed_count}")