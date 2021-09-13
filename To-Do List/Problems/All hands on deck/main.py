cards = [input() for _ in range(6)]
sum = 0
for card in cards:
    if card.isnumeric():
        sum += int(card)
    elif card == "Jack":
        sum += 11
    elif card == "Queen":
        sum += 12
    elif card == "King":
        sum += 13
    elif card == "Ace":
        sum += 14

print(sum / len(cards))
