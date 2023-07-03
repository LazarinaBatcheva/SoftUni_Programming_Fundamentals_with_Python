contest_data = input()
contests = {}
while contest_data != "end of contests":
    contest, password = contest_data.split(":")
    if contest not in contests.keys():
        contests[contest] = password
    contest_data = input()

submission_data = input()
users_info = {}
while submission_data != "end of submissions":
    contest, password, username, points = [int(x) if x.isdigit() else x for x in submission_data.split("=>")]
    if contests.get(contest) == password:
        users_info[username] = users_info.get(username, {})
        users_info[username][contest] = users_info[username].get(contest, 0)
        if users_info[username][contest] < points:
            users_info[username][contest] = points
    submission_data = input()

max_points = 0
best_candidate = ""
for name in users_info:
    candidate_points = sum(users_info[name].values())
    if candidate_points > max_points:
        best_candidate = name
        max_points = candidate_points
print(f"Best candidate is {best_candidate} with total {max_points} points.")
print("Ranking:")
for name in sorted(users_info):
    print(name)
    for contest, points in sorted(users_info[name].items(), key=lambda item: -item[1]):
        print(f"#  {contest} -> {points}")