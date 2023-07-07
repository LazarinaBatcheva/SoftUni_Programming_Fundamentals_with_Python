def add_players_in_pool(name, place, points):
    if name not in pool.keys():
        pool[name] = {}
        pool[name][place] = points
    if place not in pool[name]:
        pool[name][place] = 0
    if pool[name][place] < points:
        pool[name][place] = points


def players_duel(player1, player2):
    if (player1 and player2) in pool.keys():
        for current_position in pool[player1]:
            if current_position in pool[player2]:
                player1_total_points = sum(pool[player1].values())
                player2_total_points = sum(pool[player2].values())
                if player1_total_points > player2_total_points:
                    del pool[player2]
                elif player1_total_points < player2_total_points:
                    del pool[player1]
                break


command = input()

pool = dict()

while command != "Season end":
    if "->" in command:
        player, position, skill = [int(x) if x.isdigit() else x for x in command.split(" -> ")]
        add_players_in_pool(player, position, skill)

    elif "vs" in command:
        first_player, second_player = command.split(" vs ")
        players_duel(first_player, second_player)

    command = input()

best_players = dict(sorted(pool.items(), key=lambda x: (-sum(x[1].values()), x)))

for key in best_players:
    total_score = sum(best_players[key].values())
    print(f"{key}: {total_score} skill")
    for chart, digit in sorted(best_players[key].items(), key=lambda x: (-x[1], x[0])):
        print(f"- {chart} <::> {digit}")