def verify_card_number(card):
    card = card.replace(' ', '').replace('-', '')
    if len(card) < 2:
        return False

    card = [int(e) for e in card]

    index = -2
    while index >= -1 * len(card):
        card[index] *= 2
        if card[index] > 9:
            card[index] -= 9
        index -= 2

    return 'VALID!' if (sum(card) % 10 == 0) else 'INVALID!'

res = verify_card_number('453914889')
print(res)
