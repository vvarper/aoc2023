def get_rank(card):
    if len(set(card)) == 1:
        rank = 7  # 5 of a kind
    elif len(set(card)) == 2:
        if max(card.count(a) for a in card) == 4:
            rank = 6  # 4 of a kind
        else:
            rank = 5  # Full house
    elif len(set(card)) == 3:
        if max(card.count(a) for a in card) == 3:
            rank = 4  # 3 of a kind
        else:
            rank = 3  # 2 pairs
    elif len(set(card)) == 4:
        rank = 2  # Pair
    else:
        rank = 1  # High card

    return rank


class Card:
    strength = dict([(v, k) for k, v in enumerate('23456789TJQKA', 2)])

    def __init__(self, card, bid):
        self.card = card
        self.bid = int(bid)
        self.rank = get_rank(card)

    def __lt__(self, other):
        if self.rank == other.rank:
            for i in range(len(self.card)):
                if self.card[i] != other.card[i]:
                    return self.strength[self.card[i]] < self.strength[
                        other.card[i]]
        else:
            return self.rank < other.rank

    def __str__(self):
        return self.card + ' ' + str(self.bid) + ' ' + str(self.rank)


class CardJoker(Card):
    strength = dict([(v, k) for k, v in enumerate('J23456789TQKA', 2)])

    def __init__(self, card, bid):
        best_card = card
        if 'J' in card and card != 'JJJJJ':
            clean_card = card.replace('J', '')

            max_freq = max(clean_card.count(a) for a in clean_card)
            max_value = \
                [a for a in clean_card if clean_card.count(a) == max_freq][0]
            best_card = card.replace('J', max_value)

        super().__init__(best_card, bid)
        self.card = card


# Solution to Problem 1 #######################################################
def problem1(file_path):
    with open(file_path) as file:
        hands = [Card(*line.strip().split()) for line in file.readlines()]
        hands.sort()

        return sum(hands[i].bid * (i + 1) for i in range(len(hands)))


# Solution to Problem 2 #######################################################
def problem2(file_path):
    with open(file_path) as file:
        hands = [CardJoker(*line.strip().split()) for line in file.readlines()]
        hands.sort()

        return sum(hands[i].bid * (i + 1) for i in range(len(hands)))


###############################################################################

# File paths
test_path = "data/test07.txt"
input_path = "data/input07.txt"

# Execute the two problems
print("--- Tests ---")
print("Problem 1 test: ", problem1(test_path))
print("Problem 2 test: ", problem2(test_path))

# # Execute the two problems solutions
print("\n--- Solutions ---")
print("Problem 1 result: ", problem1(input_path))
print("Problem 2 result: ", problem2(input_path))
