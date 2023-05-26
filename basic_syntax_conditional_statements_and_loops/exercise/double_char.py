command = input()

while command != "End":
    if command != "SoftUni":
        new_command = ""
        for ch in command:
            new_command += ch * 2
        print(new_command)
    command = input()
