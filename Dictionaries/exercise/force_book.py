def add_user_to_side(name, side):
    for users in force_book.values():
        if name in users:
            return
    force_book[side] = force_book.get(side, []) + [name]


def switch_side(name, side):
    for sides, users in force_book.items():
        if name in users:
            force_book[sides].remove(name)
    force_book[side] = force_book.get(side, []) + [name]
    print(f"{name} joins the {side} side!")


command = input()
force_book = {}

while command != "Lumpawaroo":
    if "|" in command:
        force_side, user = command.split(" | ")
        add_user_to_side(user, force_side)

    elif "->" in command:
        user, force_side = command.split(" -> ")
        switch_side(user, force_side)

    command = input()

for sides_, users_ in force_book.items():
    if users_:
        print(f"Side: {sides_}, Members: {len(users_)}")
        for user in users_:
            print(f"! {user}")