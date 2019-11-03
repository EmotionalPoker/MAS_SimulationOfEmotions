# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 21:37:28 2019

@author: Hari Vidharth
"""

# import itertools
# import PokerGame

"""
dck = PokerGame.Deck()
dck.build_deck()
# dck.shuffle_deck()
d = dck.return_deck()
# print(d)
final_data = []
hand_2 = itertools.combinations(d, 2)
for i in hand_2:
    final_data.append(i)
"""


def hand_score(handcards):
    """
    A function to calculate the score of the cards during the pre flop round of
    the poker game. Its based on this score that each bot makes a
    decision to perform the action of call, check, bet, fold, or raise. This
    score determines the strength of the cards and returns a score value.
    """
    score = 0
    flush_final_data = []
    handcards = [handcards]
    for x in handcards:
        # print(x)
        a, b = x[0].split("_"), x[1].split("_")
        # print(a, b)
        c, d = [a[0], b[0]], [a[1], b[1]]
        # print(c, d)
        if d[0] == d[1]:
            score += 30
            # print(score)
            flush_final_data.append([x, score])
        else:
            flush_final_data.append([x, score])
            # print(score)
        score = 0
    score = 0
    pair_flush_final_data = []
    rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    for pos1, x in enumerate(handcards):
        # print(x)
        a, b = x[0].split("_"), x[1].split("_")
        # print(a, b)
        c, d = [a[0], b[0]], [a[1], b[1]]
        # print(c, d)
        if c[0] == c[1]:
            for pos2, item in enumerate(rank):
                if c[0] == c[1] == item:
                    score = score + ((pos2 + 1) * 3)
            e = flush_final_data[pos1][-1]
            score = score + e
            pair_flush_final_data.append([x, score])
        else:
            e = flush_final_data[pos1][-1]
            score = score + e
            pair_flush_final_data.append([x, score])
        e = 0
        score = 0
    score = 0
    straight_pair_flush_final_data = []
    rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    for pos1, x in enumerate(handcards):
        # print(x)
        a, b = x[0].split("_"), x[1].split("_")
        # print(a, b)
        c, d = [a[0], b[0]], [a[1], b[1]]
        # print(c, d)
        for pos2, item in enumerate(rank):
            if c[0] == item:
                position1 = pos2
            if c[1] == item:
                position2 = pos2
        if position1 + 1 == position2 or position2 + 1 == position1:
            if position1 > position2:
                score = score + ((position1 + 1) * 2)
            elif position2 > position1:
                score = score + ((position2 + 1) * 2)
            # print(score)
            e = pair_flush_final_data[pos1][-1]
            score = score + e
            straight_pair_flush_final_data.append([x, score])
        elif position1 - position2 <= 4 or position2 - position1 <= 4:
            if position1 > position2:
                score = score + ((position1 + 1) * 2)
            elif position2 > position1:
                score = score + ((position2 + 1) * 2)
            # print(score)
            e = pair_flush_final_data[pos1][-1]
            score = score + e
            straight_pair_flush_final_data.append([x, score])
        else:
            e = pair_flush_final_data[pos1][-1]
            score = score + e
            straight_pair_flush_final_data.append([x, score])
        e = 0
        score = 0
    score = 0
    high_straight_pair_flush_final_data = []
    rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    for pos1, x in enumerate(handcards):
        # print(x)
        a, b = x[0].split("_"), x[1].split("_")
        # print(a, b)
        c, d = [a[0], b[0]], [a[1], b[1]]
        # print(c, d)
        for pos2, item in enumerate(rank):
            if c[0] == item:
                position1 = pos2
            if c[1] == item:
                position2 = pos2
        if position1 > position2:
            score = score + ((position1 + 1))
            e = straight_pair_flush_final_data[pos1][-1]
            score = score + e
            high_straight_pair_flush_final_data.append([x, score])
        elif position2 > position1:
            score = score + ((position2 + 1))
            e = straight_pair_flush_final_data[pos1][-1]
            score = score + e
            high_straight_pair_flush_final_data.append([x, score])
        elif position2 == position1:
            score = score + ((position2 + 1))
            e = straight_pair_flush_final_data[pos1][-1]
            score = score + e
            high_straight_pair_flush_final_data.append([x, score])
        else:
            e = straight_pair_flush_final_data[pos1][-1]
            score = score + e
            high_straight_pair_flush_final_data.append([x, score])
        # print(score)
        # print(high_straight_pair_flush_final_data)
        e = 0
        score = 0
        if (high_straight_pair_flush_final_data[-1][-1]/100) > 1.0:
            return 1.0
        else:
            return (high_straight_pair_flush_final_data[-1][-1]/100)
