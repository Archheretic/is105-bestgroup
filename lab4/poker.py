
import random


def deal(numhands, n = 5, deck=[r+s for r in "23456789TJQKA" for s in "SHDC"]):
    "Shuffle the deck and deal out numhands n-card hands."
    random.shuffle(deck)
    winner = poker([deck[n*i:n*(i+1)] for i in range(numhands)])
#    print "The winner is!"
#    print winner
#hand 5 cards. rank and a suit

#
#   returns the best hand: poker([hand,...]) => hand"
#
def poker(hands):
#    print hands
#    print ""
    return max(hands, key=hand_rank)



def hand_rank(hand):
#9 hands 0-8
    ranks = card_ranks(hand)

    if straight(ranks) and flush(hand):
        return (8, max(ranks))

    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))

    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))

    elif flush(hand):
        return (5, ranks)

    elif straight(ranks):
        return (4, max(ranks))

    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)

    # elif two_pair(ranks):
    #     return (2, two_pair(ranks), ranks)

    elif two_pair(ranks):
        return (2, kind(2, ranks), kind(2, list(reversed(ranks))), ranks)

    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)

#
# Returns a list of ranks, sorted with higher first.
#
def card_ranks(cards):

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
# Return True if the ordered ranks form a 5-card straight.
#

def straight(ranks):

    if (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5:
        return True
    else:
        return False


def straight_udacity(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    return sum(ranks) - min(ranks)*5 == 10
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

def flush_udacity(hand):
    "Return True if all the cards have the same suit."
    suits = [s for r, s in hand]
    return len(set(suits)) == 1
#
# Return the first rank that this hand has exactly n of.
# Return None if there is no n-of-a-kind in the hand.
#

def kind(n, ranks):
    for r in ranks:
        if ranks.count(r) == n:
            return r
    return None
    
def two_pair(ranks):
    return len(set(ranks)) == 3 and kind(3, ranks) == None
#
# If there are two pair, return the two ranks as a
# tuple: (highest, lowest); otherwise return None.
#
def two_pair2(ranks):
    if kind(2, ranks) == kind(2, list(reversed(ranks))):
        return None

    else:
        return (kind(2, ranks), kind(2, list(reversed(ranks))))

def two_pair_udacity(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    result = [r for r in set(ranks) if ranks.count(r) == 2]
    if len(result) == 2:
        return (max(result), min(result))
#
# Test cases for the functions in poker program.
#
def test():
    "Test cases for the functions in power program."
    sf = "6C 7C 8C 9C TC".split()   # sf straight flush
    fk = "9D 9H 9S 9C 7D".split()   # fk four of a kind
    fh = "TD TC TH 7C 7D".split()   # fh full house
    tp = "5S 5D 9H 9C 6S".split()   # tp two pair
    s1 = "AS 2S 3S 4S 5C".split()   # A-5 Straight
    s2 = "2C 3C 4C 5S 6S".split()   # 2-6 Straight
    ah = "AS 2S 3S 4S 6C".split()   # A high
    sh = "2S 3S 4S 6C 7D".split()   # 7 high

    assert poker([s1, s2, ah, sh]) == s2


    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)

    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7

    assert two_pair(fkranks) == False
    assert two_pair(tpranks) == True
    #assert two_pair(tpranks) == (9, 5)

    # assert straight(sf) == True
    # assert straight(s1) == True
    # assert straight(s2) == True
    # assert straight(ah) == False
    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False


    assert flush(sf) == True
    assert flush(fh) == False

    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]

    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert poker([sf]) == sf
    assert poker([sf] + 99*[fh]) == sf

    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)

    return "tests pass"

#print test()

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("straight([9, 8, 7, 6, 5])", setup="from __main__ import straight"))
    print(timeit.timeit("straight_udacity([9, 8, 7, 6, 5])", setup="from __main__ import straight_udacity"))
    print(timeit.timeit("flush('6C 7C 8C 9C TC'.split())", setup="from __main__ import flush"))
    print(timeit.timeit("flush_udacity('6C 7C 8C 9C TC'.split())", setup="from __main__ import flush_udacity"))
    print(timeit.timeit("two_pair([9, 9, 5, 5, 2])", setup="from __main__ import two_pair"))
    print(timeit.timeit("two_pair2([9, 9, 5, 5, 2])", setup="from __main__ import two_pair2"))
    print(timeit.timeit("two_pair_udacity([9, 9, 5, 5, 2])", setup="from __main__ import two_pair_udacity"))
