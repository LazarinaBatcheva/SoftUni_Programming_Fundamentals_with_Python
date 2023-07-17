def add_piece(a_piece, a_composer, a_key, pieces_info_dict):
    if a_piece not in pieces_info_dict:
        pieces_info_dict[a_piece] = [a_composer, a_key]
        print(f"{a_piece} by {a_composer} in {a_key} added to the collection!")
    else:
        print(f"{a_piece} is already in the collection!")
    return pieces_info_dict


def remove_piece(a_piece, pieces_info_dict):
    if a_piece in pieces_info_dict.keys():
        del pieces_info_dict[a_piece]
        print(f"Successfully removed {a_piece}!")
    else:
        print(f"Invalid operation! {a_piece} does not exist in the collection.")
    return pieces_info_dict


def change_key(a_piece, the_new_key, pieces_info_dict):
    if a_piece in pieces_info_dict:
        pieces_info_dict[a_piece][1] = the_new_key
        print(f"Changed the key of {a_piece} to {the_new_key}!")
    else:
        print(f"Invalid operation! {a_piece} does not exist in the collection.")
    return pieces_info_dict


number_of_pieces = int(input())

pieces_info = dict()
for current_piece in range(number_of_pieces):
    piece, composer, piece_key = input().split("|")
    if piece not in pieces_info.keys():
        pieces_info[piece] = [composer, piece_key]

while True:
    command = input()
    if command == "Stop":
        [print(f"{piece} -> Composer: {pieces_info[piece][0]}, Key: {pieces_info[piece][1]}") for piece in pieces_info]
        break
    command = command.split("|")
    if "Add" in command:
        action, current_piece, current_composer, current_key = command[0], command[1], command[2], command[3]
        add_piece(current_piece, current_composer, current_key, pieces_info)
    elif "Remove" in command:
        action, current_piece = command[0], command[1]
        remove_piece(current_piece, pieces_info)
    elif "ChangeKey" in command:
        action, current_piece, new_key = command[0], command[1], command[2]
        change_key(current_piece, new_key, pieces_info)
