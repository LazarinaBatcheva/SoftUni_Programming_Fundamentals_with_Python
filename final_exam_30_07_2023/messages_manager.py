def add_user(action, usernames_dict):
    username = action[1]
    sent = int(action[2])
    received = int(action[3])
    if username not in usernames_dict:
        usernames_dict[username] = {"sent": sent, "received": received}
    return usernames_dict


def increase_messages(action, usernames_dict, capacity):
    sender = action[1]
    receiver = action[2]
    if sender in usernames_dict and receiver in usernames_dict:
        usernames_dict[sender]["sent"] += 1
        usernames_dict[receiver]["received"] += 1
        if (usernames_dict[sender]["sent"] + usernames_dict[sender]["received"]) >= capacity:
            del usernames_dict[sender]
            print(f"{sender} reached the capacity!")
        if (usernames_dict[receiver]["sent"] + usernames_dict[receiver]["received"]) >= capacity:
            del usernames_dict[receiver]
            print(f"{receiver} reached the capacity!")
    return usernames_dict


def delete_records(action, usernames_dict):
    username = action[1]
    if username == "All":
        del usernames_dict
        usernames_dict = {}
    else:
        if username in usernames_dict:
            del usernames_dict[username]
    return usernames_dict


messages_capacity = int(input())
command = input()
users_dict = {}

while command != "Statistics":
    current_command = command.split("=")
    if current_command[0] == "Add":
        users_dict = add_user(current_command, users_dict)
    elif current_command[0] == "Message":
        users_dict = increase_messages(current_command, users_dict, messages_capacity)
    elif current_command[0] == "Empty":
        users_dict = delete_records(current_command, users_dict)
    command = input()

print(f"Users count: {len(users_dict)}")
for user, messages in users_dict.items():
    sum_messages = users_dict[user]["sent"] + users_dict[user]["received"]
    print(f"{user} - {sum_messages}")