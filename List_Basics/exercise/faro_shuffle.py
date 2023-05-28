deck_of_cards = input().split()
count_of_shuffles = int(input())

for shuffle in range(count_of_shuffles):
    cards_after_last_shuffle = []
    middle_of_cards = len(deck_of_cards) // 2
    left_part_of_deck = deck_of_cards[:middle_of_cards]
    right_part_of_deck = deck_of_cards[middle_of_cards:]
    for current_card in range(len(left_part_of_deck)):
        cards_after_last_shuffle.append(left_part_of_deck[current_card])
        cards_after_last_shuffle.append(right_part_of_deck[current_card])

    deck_of_cards = cards_after_last_shuffle

print(deck_of_cards)