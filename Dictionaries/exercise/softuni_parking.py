number_of_registrants = int(input())
users = {}
for user in range(number_of_registrants):
    command = input().split()

    if "register" in command:
        action, username, registration_number = command[0], command[1], command[2]
        if username not in users.keys():
            users[username] = registration_number
            print(f"{username} registered {users[username]} successfully")
        else:
            print(f"ERROR: already registered with plate number {users[username]}")
    elif "unregister" in command:
        action, username = command[0], command[1]
        if username not in users.keys():
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del users[username]

for username, registration_number in users.items():
    print(f"{username} => {users[username]}")
