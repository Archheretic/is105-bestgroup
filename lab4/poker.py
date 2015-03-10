#
# gruppe = {  'student1': 'Viktor Setervang', \
#			  'student2': 'Ola Mathiesen', \
#             'student3': 'Tord Resch Lindaas', \
#             'student4': 'Michael Matthew Desmond', \
#             'student4': 'Linus Weagba', \
#
import random
import time
import re

def welcome():

    print ("\nWelcome to our poker program!\nWe got many options for you, " +
           "so listen carefully.\nThe options are marked with a number, write "+
           "the number to choose option:")
    time.sleep(2.5)
    print "1. Deal poker hands."
    time.sleep(1)
    print "2. Run test function to check asserts."
    time.sleep(1)
    print ("3. Run the speed test to test the speed of our functions up " +
             "against Udacitys.")

    valid_answer = False
    while valid_answer == False:
        answer = raw_input("I choose option: ")
        if (re.match(r"^[1-3]*$", answer) and len(answer) == 1):
            valid_answer = True
        elif (re.match(r"^[qQ]*$", answer)):
            print "Goodbye!"
            quit()
        else:
            print "pick an option 1-3, type q to quit the program"


    _chosen_procedure(answer)
#
#   This function checks the answer the user gave and sends him to the function
#   of choice.
#
def _chosen_procedure(answer):

    if answer == "1":
        valid_answer = False
        while valid_answer == False:
            answer = raw_input("How many hands do you want dealt? (1-10): ")
            if int(answer) > 0 and int(answer) < 11:
                valid_answer = True

        deal(int(answer))

    if answer == "2":
        print test()

    if answer == "3":
        speedtest()

def print_winner(winners, hand_num):
    hand_names = ["High card", "One pair", "Two pair", "Three of a kind",
                  "Straight", "Flush", "WITH WHAT?" , "Full house",
                  "Four of a kind", "Straight flush", "Five of a kind"]

    winner = winners[0]
    counts, ranks = unzip(group(card_ranks(winner)))

    points = 0
    if straight(ranks):
        points = 4

    if flush(winner):
        points = points + 5

    winner = _count_ranking(counts)

    if winner < points:
        winner = points

    win_print = ("Hand number: %swon with " % hand_num
                + hand_names[winner] + "! " + str(winners))

    print win_print

    return win_print
#
# This function creates a unshuffled deck.
# The args num_deck is the number of decks, and shuffle is a boolean value
# if True it will access the function that shuffles the deck.
#
def card_deck(numdeck, shuffle):
    suits = "SHDC"
    ranks = "23456789TJQKA"

    deck = list()
    # For each deck
    for x in range(numdeck):
        # For each card in deck
        for i in range(52):
            suit = suits[i / 13]
            rank = ranks[i % 13]
            card = (rank + suit)
            deck.append(card)

    #shuffle is on by default.
    if shuffle:
        return _shuffle_deck(deck)
    else:
        return deck
#
#  This function shuffles the deck using the Durstenfeld shuffle algorithm.
#

def _shuffle_deck(deck):
    for i in reversed(range(1, len(deck))):
        index = random.randrange(i + 1);
        # swaps
        a = deck[index]
        deck[index] = deck[i]
        deck[i] = a

    return deck
#
#
#
def deal(numhands, n = 5):
    deck = card_deck(1, True)

    hands = [deck[n*i:n*(i+1)] for i in range(numhands)]
    winners = poker(hands)

    #hand_num #1 = element 0 of hands, #10 = element 9.
    i = 1
    hand_num = list()

    for hand in hands:

        if hand == winners[0] and len(hand_num) == 0:
            hand_num.append("#" + str(i) + " ")

        elif hand == winners[0] and len(hand_num) == (len(winners)-1):
            hand_num.append("and " "#" + str(i) + " ")

        elif hand == winners[0]:
            hand_num.append(", " "#" + str(i) + " ")
        i+= 1
    hand_ref = ""
    for i in hand_num:
        hand_ref = hand_ref + i

    print_winner(winners, hand_ref)
#
# Return a list of winning hands: poker([hand,...]) => [hand,...]
#
def poker(hands):
    #print hands
    #print ""
    return allmax(hands, key=hand_rank)
#
#
#
def hand_rank(hand):
    groups = group(card_ranks(hand))
    counts, ranks = unzip(groups)

    straight1 = straight(ranks)
    flush1 = flush(hand)

    return max(_count_ranking(counts), 4*straight1 + 5*flush1), ranks
#
#
#
def unzip(pairs):
    return zip(*pairs)

# Help function for hand_rank and print_winner, this function returns the
# rank of the hand.
#
def _count_ranking(counts):
    count_rankings = {(5,):10, (4, 1):8, (3, 2):7, (3, 1, 1):3,
                     (2, 2, 1):2, (2, 1, 1, 1):1, (1, 1, 1, 1, 1):0}
    return count_rankings[counts]
#
#
#
def group(hand):
    groups = list()
    for x in set(hand):
        groups.append((hand.count(x), x))

    return sorted(groups, reverse=True)
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

    return ranks
#
# This function is for handling ties, if more then one player got the
# same hand, both will be declared winner.
#
# This function copied directly from Udacity.
#
def allmax(iterable, key=None):
    result, maxval = [], None
    key = key or (lambda x: x)
    #print iterable
    for x in iterable:
        xval = key(x)
        if not result or xval > maxval:
            result, maxval = [x], xval
        elif xval == maxval:
            result.append(x)

    #print result
    return result
#
# Return True if the ordered ranks form a 5-card straight.
#
def straight(ranks):
    for i in range(len(ranks)-1):
        if ranks[i+1] != ranks[i]-1:
            return False
    return True


#
# Return True if all the cards have the same suit."
#
def flush(hand):
    suits = list()
    for card in hand:
        suits.append(card[1])
    return len(set(suits)) == 1
#
#
#  ABOVE THIS IS THE ARE THE MAIN FUNCTIONS OF THE PROGRAM.
#  NOONE OF THE FUNCTIONS BELOW ARE NEEDED FOR THE MAIN PART OF THE
#  PROGRAM TO RUN.
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


    assert poker([s1, s2, ah, sh]) == [s2]


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


    assert straight(card_ranks(sf)) == True
    assert straight(card_ranks(s2)) == True
    assert straight(card_ranks(s1)) == True

    assert straight(card_ranks(ah)) == False
    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False

    assert flush(sf) == True
    assert flush(fh) == False


    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]

    assert poker([sf, fk, fh]) == [sf]
    assert poker([fk, fh]) == [fk]
    assert poker([fh, fh]) == [fh, fh]
    assert poker([sf]) == [sf]
    assert poker([sf] + 99*[fh]) == [sf]
    assert poker([s1, s2, tp]) == [s2]
    assert poker([s1, s2, fh]) == [fh]

    assert hand_rank(sf) == (9, (10, 9, 8, 7, 6))

    assert hand_rank(fk) == (8, (9, 7))
    assert hand_rank(fh) == (7, (10, 7))

    return "tests passed! :)"
#
# Below this are:
# Lots of unused code, some of it from udacity.
# Some of the functions below are needed to pass the asserts in the
# test() function.
#
def card_ranks_old(cards):
    ranks.append(card_rank[card[0]])
    #tuple(ranks)
    ranks.sort(reverse=True)
# The wheel
    if ranks == [14, 5, 4, 3, 2]:
        ranks = [5, 4, 3, 2, 1]
    return ranks
#
#
#thehand
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


def speedtest():
    import timeit
    print "Our Straight:"
    print(timeit.timeit("straight([9, 8, 7, 6, 5])", setup="from __main__ import straight"))
    print "Udacity Straigth:"
    print(timeit.timeit("straight_udacity([9, 8, 7, 6, 5])", setup="from __main__ import straight_udacity"))
    print "Our Flush:"
    print(timeit.timeit("flush('6C 7C 8C 9C TC'.split())", setup="from __main__ import flush"))
    print "Udacity Flush:"
    print(timeit.timeit("flush_udacity('6C 7C 8C 9C TC'.split())", setup="from __main__ import flush_udacity"))
    print "Our Two Pair:"
    print(timeit.timeit("two_pair([9, 9, 5, 5, 2])", setup="from __main__ import two_pair"))
    print "Udacitys first Two Pair:"
    print(timeit.timeit("two_pair_udacity_old([9, 9, 5, 5, 2])", setup="from __main__ import two_pair_udacity_old"))
    print "Udacitys refactored Two Pair:"
    print(timeit.timeit("two_pair_udacity([9, 9, 5, 5, 2])", setup="from __main__ import two_pair_udacity"))


if __name__ == '__main__':
    welcome()
