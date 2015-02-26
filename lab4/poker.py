import random


def deal(numhands, n = 5, deck=[r+s for r in "23456789TJQKA" for s in "SHDC"]):
    "Shuffle the deck and deal out numhands n-card hands."
    random.shuffle(deck)
    winner = poker([deck[n*i:n*(i+1)] for i in range(numhands)])
    #print "The winner is!"
    #print winner
#
#   returns the best hand: poker([hand,...]) => hand"
#
def poker(hands):
    #print hands
    #print ""
    return max(hands, key=hand_rank)
#
#
#
def hand_rank(hand):
    groups = card_ranks(hand)

    counts, ranks = unzip(groups)

    count_rankings = {(5,):10, (4, 1):8, (3, 2):7, (3, 1, 1):3,
                      (2, 2, 1):2, (2, 1, 1, 1):1, (1, 1, 1, 1, 1):0}

    straight1 = straight(ranks)
    flush1 = flush(hand)
    return max(count_rankings[counts], 4*straight1 + 5*flush1), ranks
#
#
#
def unzip(pairs): return zip(*pairs)
#
#
#
def card_ranks(cards):

    card_rank = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
                 "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

    ranks = list()
    for card in cards:
        ranks.append(card_rank[card[0]])

    ranks.sort(reverse=True)
    # The wheel (Ace, 2, 3, 4, 5)
    if ranks == [14, 5, 4, 3, 2]:
        ranks = [5, 4, 3, 2, 1]

    groups = list()
    for x in set(ranks):
        groups.append((ranks.count(x), x))
    return sorted(groups, reverse=True)
#
# Return True if the ordered ranks form a 5-card straight.
#
def straight(ranks):

    if (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5:
        return True
    else:
        return False
#
# Return True if all the cards have the same suit."
#
def flush(hand):
    suits = list()
    for card in hand:
        suits.append(card[1])

    if len(set(suits)) == 1:
        return True
    else:
        return False
#
#
#  ABOVE THIS IS THE ARE THE MAIN FUNCTIONS OF THE PROGRAM.
#  NOONE OF THE FUNCTIONS BELOW ARE NEEDED FOR THE PROGRAM TO RUN.
#
#
# Return the first rank that this hand has exactly n of.
# Return None if there is no n-of-a-kind in the hand.
#
def kind(n, ranks):
    for r in ranks:
        if ranks.count(r) == n:
            return r
    return None
#
def two_pair(ranks):
    return len(set(ranks)) == 3 and kind(3, ranks) == None
#
#
# Test cases for the functions in poker program.
#
def test():
    "Test cases for the functions in power program."
    sf = "6C 7C 8C 9C TC".split()   # sf straight flush
    fk = "9D 9H 9S 9C 7D".split()   # fk four of a kind
    tk = "9D 9H 9S 3C 7D".split()   # tk three of a kind
    fh = "TD TC TH 7C 7D".split()   # fh full house
    tp = "5S 5D 9H 9C 6S".split()   # tp two pair
    s1 = "AS 2S 3S 4S 5C".split()   # A-5 Straight
    s2 = "2C 3C 4C 5S 6S".split()   # 2-6 Straight
    ah = "AS 2S 3S 4S 6C".split()   # A high
    sh = "2S 3S 4S 6C 7D".split()   # 7 high


    assert poker([s1, s2, ah, sh]) == s2


    fkranks = card_ranks_old(fk)
    tkranks = card_ranks_old(tk)
    tpranks = card_ranks_old(tp)

    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7
    assert kind(3, tkranks) == 9

    assert two_pair(fkranks) == False
    assert two_pair(tpranks) == True
    #assert two_pair(tpranks) == (9, 5)

    # assert straight(card_ranks(sf)) == True
    # assert straight(card_ranks(s2)) == True
    # assert straight(card_ranks(s1)) == True

    #assert straight(card_ranks(ah)) == False
    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False

    assert flush(sf) == True
    assert flush(fh) == False

    assert card_ranks(sf) == [(1, 10), (1, 9), (1, 8), (1, 7), (1, 6)]
    assert card_ranks(fk) == [(4, 9), (1, 7)]
    assert card_ranks(fh) == [(3, 10), (2, 7)]

    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert poker([sf]) == sf
    assert poker([sf] + 99*[fh]) == sf
    assert poker([s1, s2, tp]) == s2
    assert poker([s1, s2, fh]) == fh

    assert hand_rank(sf) == (9, (10, 9, 8, 7, 6))

    assert hand_rank(fk) == (8, (9, 7))
    assert hand_rank(fh) == (7, (10, 7))

    return "tests pass"

#print test()
#deal(10)
#
#
# Lots of unused code, some of it from udacity.
#
#
#
# Returns a list of ranks, sorted with higher first.
#
def card_ranks_old(cards):

    card_rank = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
                 "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

    ranks = list()
    for card in cards:
        ranks.append(card_rank[card[0]])
    #tuple(ranks)
    ranks.sort(reverse=True)
# The wheel
    if ranks == [14, 5, 4, 3, 2]:
        ranks = [5, 4, 3, 2, 1]
    return ranks
#
#
#
def flush_udacity(hand):
    "Return True if all the cards have the same suit."
    suits = [s for r, s in hand]
    return len(set(suits)) == 1


def straight_udacity(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    return sum(ranks) - min(ranks)*5 == 10
#
#
# The refactored udacity version
#
# If there are two pair, return the two ranks as a
# tuple: (highest, lowest); otherwise return None.
#
def two_pair_udacity(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    result = [r for r in set(ranks) if ranks.count(r) == 2]
    if len(result) == 2:
        return (max(result), min(result))
#
# The first unrefactored udacity version
#
def two_pair_udacity_old(ranks):
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None

# def group(items):
#
#     groups = list()
#     for x in set(items):
#         groups.append((items.count(x), x))
#     return sorted(groups, reverse=True)
print test()

# if __name__ == '__main__':
#     import timeit
#     print(timeit.timeit("straight([9, 8, 7, 6, 5])", setup="from __main__ import straight"))
#     print(timeit.timeit("straight_udacity([9, 8, 7, 6, 5])", setup="from __main__ import straight_udacity"))
#     print(timeit.timeit("flush('6C 7C 8C 9C TC'.split())", setup="from __main__ import flush"))
#     print(timeit.timeit("flush_udacity('6C 7C 8C 9C TC'.split())", setup="from __main__ import flush_udacity"))
#     print(timeit.timeit("two_pair([9, 9, 5, 5, 2])", setup="from __main__ import two_pair"))
#     print(timeit.timeit("two_pair_udacity_old([9, 9, 5, 5, 2])", setup="from __main__ import two_pair_udacity_old"))
#     print(timeit.timeit("two_pair_udacity([9, 9, 5, 5, 2])", setup="from __main__ import two_pair_udacity"))
