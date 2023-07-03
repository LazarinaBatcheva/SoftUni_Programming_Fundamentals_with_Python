results = {}
submissions = {}

while True:
    command = input().split("-")

    if len(command) == 1:
        break

    elif len(command) == 2:
        name = command[0]
        del results[name]

    elif len(command) == 3:
        name, language, points = command[0], command[1], int(command[2])
        if name not in results.keys():
            results[name] = 0
        if results[name] < points:
            results[name] = points
        if language not in submissions.keys():
            submissions[language] = 0
        submissions[language] += 1

print("Results:")
for name, points in results.items():
    print(f"{name} | {points}")

print("Submissions:")
for language, submissions_count in submissions.items():
    print(f"{language} - {submissions_count}")