note = input()

to_do_list = []

while note != "End":
    note = note.split("-")
    to_do_list.append(note)

    note = input()

sorted_to_do_list = sorted(to_do_list, key=lambda x: int(x[0]))
final_to_do_list = [note[1] for note in sorted_to_do_list]

print(final_to_do_list)