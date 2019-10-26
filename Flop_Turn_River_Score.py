# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 21:37:28 2019

@author: Hari Vidharth
"""

import itertools


def royal_flush(a):
    """
    To check for a flush in the set, Takes the player cards and community
    cards as input, and checks for a flush among the players, and returns
    the players whose cards matches. Does not return any cards if
    multiple flush cards or no flush cards are detected.
    Also checks for the value of the cards are according to the rank
    ["10", "J", "Q", "K", "A"] returns the player whose cards matches,
    combing it with the above flush result to check for a ROYAL FLUSH,
    returns the player if winner else returns None and moves to the next
    check function!
    """
    suit = []
    playercommunitycards = a
    player = []
    flushcount = []
    playercount = []
    flushplayercount = []
    for items in playercommunitycards:
        for item in items:
            player.append(item.split("_")[1])
        suit.append(player)
        player = []
    # print(suit)
    cardclass = ["♣", "♦", "♥", "♠"]
    for items in cardclass:
        for item in suit:
            flushcount.append(item.count(items))
        # print(flushcount)
        for position, item in enumerate(flushcount):
            if item >= 5:
                playercount.append(position)
        # print(playercount)
        flushplayercount.append(playercount)
        playercount = []
        flushcount = []
    # print(flushplayercount)
    rank = ["10", "J", "Q", "K", "A"]
    count = 0
    value = []
    for items in playercommunitycards:
        for item in items:
            player.append(item.split("_")[0])
        value.append(player)
        player = []
    # print(value)
    royal = []
    for pos, items in enumerate(value):
        for ranking in rank:
            if ranking in items:
                count += 1
        royal.append((pos, count))
        count = 0
    # print(royal)
    new_royal = []
    for items in royal:
        if items[1] == 5:
            new_royal.append(items[0])
    # print(new_royal)
    final_royal = []
    for item in new_royal:
        for items in flushplayercount:
            if item in items:
                final_royal.append(item)
    # print(final_royal)
    for items in final_royal:
        return items


def straight_flush(a):
    """
     To check for a flush in the set, Takes the player cards and community
     cards as input, and checks for a flush among the players, and returns
     the players whose cards matches. Does not return any cards if
     multiple flush cards or no flush cards are detected.
     Also checks for the value of the cards are according to the straight
     rank returns the player whose cards matches, combing it with the above
     flush result to check for a STRAIGHT FLUSH, returns the player if
     winner else returns None and moves to the next check function!
     """
    suit = []
    playercommunitycards = a
    player = []
    flushcount = []
    playercount = []
    flushplayercount = []
    for items in playercommunitycards:
        for item in items:
            player.append(item.split("_")[1])
        suit.append(player)
        player = []
    # print(suit)
    cardclass = ["♣", "♦", "♥", "♠"]
    for items in cardclass:
        for item in suit:
            flushcount.append(item.count(items))
        # print(flushcount)
        for position, item in enumerate(flushcount):
            if item >= 5:
                playercount.append(position)
        # print(playercount)
        flushplayercount.append(playercount)
        playercount = []
        flushcount = []
    # print(flushplayercount)
    value = []
    for items in playercommunitycards:
        for item in items:
            player.append(item.split("_")[0])
        value.append(player)
        player = []
    # print(value)
    rank = ["2", "3", "4", "5", "6", "7", "8", "9",
            "10", "J", "Q", "K", "A"]
    card_position = []
    playerp = []
    for items in value:
        for position, item in enumerate(rank):
            if item in items:
                playerp.append(position)
        card_position.append(playerp)
        playerp = []
    # print(card_position)
    groups = []
    group = []
    for items in card_position:
        value1 = value2 = items[0]
        for item in items[1:]:
            if item == value2 + 1:
                value2 = item
            else:
                groups.append(value1 if value1 == value2 else
                              (value1, value2))
                value1 = value2 = item
        groups.append(value1 if value1 == value2 else (value1, value2))
        group.append(groups)
        groups = []
    # print(group)
    new_group = []
    player = []
    for items in group:
        for item in items:
            if type(item) is tuple:
                player.append(item)
        new_group.append(player)
        player = []
    # print(new_group)
    straightplayer = []
    for pos, items in enumerate(new_group):
        if len(items) != 0:
            if items[0][-1] - items[0][0] == 4:
                straightplayer.append(pos)
    # print(straightplayer)
    straightflushplayer = []
    for item in straightplayer:
        for items in flushplayercount:
            if item in items:
                straightflushplayer.append(item)
    for items in straightflushplayer:
        return items


def four_of_a_kind(a):
    """
     To check for a four of a kind in the set, Takes the player cards and
     community cards as input, and checks for a four of a kind among the
     players, and returns the players whose cards matches. Does not return
     any cards if multiple or no four of a kinds are detected. Returns the
     player if winner else returns None and moves to the next check
     function!
     """
    value = []
    player = []
    playercommunitycards = a
    player = []
    # print(playercommunitycards)
    for items in playercommunitycards:
        for item in items:
            player.append(item.split("_")[0])
        value.append(player)
        player = []
    # print(value)
    new_value = []
    player = []
    for items in value:
        for value1, value2, value3, value4 in itertools.combinations(
                                                                items, 4):
            player.append((value1, value2, value3, value4))
        new_value.append(player)
        player = []
    four_of_a_kind = []
    player = []
    for items in new_value:
        for item in items:
            if (item[0] == item[1] and item[1] == item[2] and item[2] ==
                    item[3]):
                player.append((item[0], item[1], item[2], item[3]))
        four_of_a_kind.append(player)
        player = []
    # print(four_of_a_kind)
    new_four_of_a_kind = []
    for pos, items in enumerate(four_of_a_kind):
        if len(items) >= 1:
            new_four_of_a_kind.append(pos)
    # print(new_four_of_a_kind)
    if len(new_four_of_a_kind) == 1:
        return new_four_of_a_kind[0]
    else:
        return None


def full_house(a):
    """
    To check for a three of a kind in the set, Takes the player cards and
    community cards as input, and checks for a three of a kind among the
    players, and returns the players whose cards matches. Does not return
    any cards if multiple or no three of a kinds are detected. Returns the
    player if winner else returns None and moves to the next check
    function!
    To check for a highest pair in the set, Takes the player cards and
    community cards as input, and checks for the two pairs among the
    players and returns the players value. Does not return any cards if
    multiple or no two pair cards are detected, it is then directed to the
    next check function!
    """
    value = []
    player = []
    playercommunitycards = a
    player = []
    # print(playercommunitycards)
    for items in playercommunitycards:
        for item in items:
            player.append(item.split("_")[0])
        value.append(player)
        player = []
    # print(value)
    new_value = []
    player = []
    for items in value:
        for value1, value2, value3 in itertools.combinations(items, 3):
            player.append((value1, value2, value3))
        new_value.append(player)
        player = []
    three_of_a_kind = []
    player = []
    for items in new_value:
        for item in items:
            if item[0] == item[1] and item[1] == item[2]:
                player.append((item[0], item[1], item[2]))
        three_of_a_kind.append(player)
        player = []
    # print(three_of_a_kind)
    new_three_of_a_kind = []
    for pos, items in enumerate(three_of_a_kind):
        if len(items) >= 1:
            new_three_of_a_kind.append(pos)
    # print(new_three_of_a_kind)
    rank = ["2", "3", "4", "5", "6", "7", "8", "9",
            "10", "J", "Q", "K", "A"]
    playercommunitycards = a
    playervalue = [[playercommunitycards[0][0], playercommunitycards[0][1]]]
    communityvalue = []
    if len(playercommunitycards) == 5:
        communityvalue = [[playercommunitycards[0][2],
                          playercommunitycards[0][3],
                          playercommunitycards[0][4]]]
    elif len(playercommunitycards) == 6:
        communityvalue = [[playercommunitycards[0][2],
                          playercommunitycards[0][3],
                          playercommunitycards[0][4],
                          playercommunitycards[0][5]]]
    elif len(playercommunitycards) == 7:
        communityvalue = [[playercommunitycards[0][2],
                          playercommunitycards[0][3],
                          playercommunitycards[0][4],
                          playercommunitycards[0][5],
                          playercommunitycards[0][7]]]
    # print(playervalue)
    # print(communityvalue)
    new_value = []
    player = []
    pvalue = []
    cvalue = []
    for items in playervalue:
        for item in items:
            player.append(item.split("_")[0])
        pvalue.append(player)
        player = []
    # print(pvalue)
    for items in communityvalue:
        for item in items:
            cvalue.append(item.split("_")[0])
    # print(cvalue)
    for pos, items in enumerate(pvalue):
        if items[0] == items[1]:
            player.append([pos, items[0]])
        for item in items:
            if item in cvalue:
                player.append([pos, item])
        # print(player)
        new_value.append(player)
        player = []
    # print(new_value)
    pair_rank = []
    player = []
    for items in new_value:
        for item in items:
            for pos, ranking in enumerate(rank):
                if ranking == item[1]:
                    player.append([pos, item])
            pair_rank.append(player)
            player = []
    pair_rank = sorted(pair_rank)
    # print(pair_rank)
    count = 0
    playercount = []
    player = []
    for items in pair_rank:
        for item in new_three_of_a_kind:
            if item == items[0][1][0]:
                count += 1
        player.append(count)
        playercount.append(player)
        player = []
        count = 0
    # print(playercount)
    if len(playercount) != 0:
        for pos, items in enumerate(playercount):
            return pos
    else:
        return None


def straight(a):
    """
     Checks for the value of the cards are according to the straight
     rank and returns the player whose cards matches, to check for a
     STRAIGHT, returns the player if winner else returns None and moves
     to the next check function!
     """
    playercommunitycards = a
    player = []
    value = []
    for items in playercommunitycards:
        for item in items:
            player.append(item.split("_")[0])
        value.append(player)
        player = []
    # print(value)
    rank = ["2", "3", "4", "5", "6", "7", "8", "9",
            "10", "J", "Q", "K", "A"]
    card_position = []
    playerp = []
    for items in value:
        for position, item in enumerate(rank):
            if item in items:
                playerp.append(position)
        card_position.append(playerp)
        playerp = []
    # print(card_position)
    groups = []
    group = []
    for items in card_position:
        value1 = value2 = items[0]
        for item in items[1:]:
            if item == value2 + 1:
                value2 = item
            else:
                groups.append(value1 if value1 == value2 else
                              (value1, value2))
                value1 = value2 = item
        groups.append(value1 if value1 == value2 else (value1, value2))
        group.append(groups)
        groups = []
    # print(group)
    new_group = []
    player = []
    for items in group:
        for item in items:
            if type(item) is tuple:
                player.append(item)
        new_group.append(player)
        player = []
    # print(new_group)
    straightplayer = []
    for pos, items in enumerate(new_group):
        if len(items) != 0:
            if items[0][-1] - items[0][0] == 4:
                straightplayer.append(pos)
    # print(straightplayer)
    if len(straightplayer) == 1:
        return straightplayer[0]
    else:
        return None


def flush(a):
    """
    To check for a flush in the set, Takes the player cards and community
    cards as input, and checks for a flush among the players, and returns
    the players and flush cards value. Does not return any cards if
    multiple flush cards or no flush cards are detected, and is then
    directed to the next check function!
    """
    suit = []
    playercommunitycards = a
    player = []
    flushcount = []
    playercount = []
    flushplayercount = []
    for items in playercommunitycards:
        for item in items:
            player.append(item.split("_")[1])
        suit.append(player)
        player = []
    # print(suit)
    cardclass = ["♣", "♦", "♥", "♠"]
    for items in cardclass:
        for item in suit:
            flushcount.append(item.count(items))
        # print(flushcount)
        for position, item in enumerate(flushcount):
            if item >= 5:
                playercount.append(position)
        # print(playercount)
        flushplayercount.append(playercount)
        playercount = []
        flushcount = []
    # print(flushplayercount)
    finalflush = []
    for items in flushplayercount:
        if len(items) == 1:
            finalflush.append(items)
    # print(finalflush)
    if len(finalflush) != 0:
        if len(finalflush[0]) == 1:
            return finalflush[0][0]
        else:
            return None


def three_of_a_kind(a):
    """
     To check for a three of a kind in the set, Takes the player cards and
     community cards as input, and checks for a three of a kind among the
     players, and returns the players whose cards matches. Does not return
     any cards if multiple or no three of a kinds are detected. Returns the
     player if winner else returns None and moves to the next check
     function!
     """
    value = []
    player = []
    playercommunitycards = a
    player = []
    for items in playercommunitycards:
        for item in items:
            player.append(item.split("_")[0])
        value.append(player)
        player = []
    # print(value)
    new_value = []
    player = []
    for items in value:
        for value1, value2, value3 in itertools.combinations(items, 3):
            player.append((value1, value2, value3))
        new_value.append(player)
        player = []
    three_of_a_kind = []
    player = []
    for items in new_value:
        for item in items:
            if item[0] == item[1] and item[1] == item[2]:
                player.append((item[0], item[1], item[2]))
        three_of_a_kind.append(player)
        player = []
    # print(three_of_a_kind)
    new_three_of_a_kind = []
    for pos, items in enumerate(three_of_a_kind):
        if len(items) >= 1:
            new_three_of_a_kind.append(pos)
    # print(new_three_of_a_kind)
    if len(new_three_of_a_kind) == 1:
        return new_three_of_a_kind[0]
    else:
        return None


def two_pair(a):
    """
    To check for a two pair in the set, Takes the player cards and
    community cards as input, and checks for the two pairs among the
    players and returns the players value. Does not return any cards if
    multiple or no two pair cards are detected, it is then directed to the
    next check function!
    """
    playercommunitycards = a
    playervalue = [[playercommunitycards[0][0], playercommunitycards[0][1]]]
    communityvalue = []
    if len(playercommunitycards) == 5:
        communityvalue = [[playercommunitycards[0][2],
                          playercommunitycards[0][3],
                          playercommunitycards[0][4]]]
    elif len(playercommunitycards) == 6:
        communityvalue = [[playercommunitycards[0][2],
                          playercommunitycards[0][3],
                          playercommunitycards[0][4],
                          playercommunitycards[0][5]]]
    elif len(playercommunitycards) == 7:
        communityvalue = [[playercommunitycards[0][2],
                          playercommunitycards[0][3],
                          playercommunitycards[0][4],
                          playercommunitycards[0][5],
                          playercommunitycards[0][7]]]
    new_value = []
    player = []
    pvalue = []
    cvalue = []
    for items in playervalue:
        for item in items:
            player.append(item.split("_")[0])
        pvalue.append(player)
        player = []
    # print(pvalue)
    for items in communityvalue:
        for item in items:
            cvalue.append(item.split("_")[0])
    # print(cvalue)
    for pos, items in enumerate(pvalue):
        if items[0] == items[1]:
            player.append([pos, items[0]])
        for item in items:
            if item in cvalue:
                player.append([pos, item])
        new_value.append(player)
        player = []
    # print(new_value)
    final_value = []
    for items in new_value:
        if len(items) == 2:
            final_value.append(items[0][0])
    # print(final_value)
    if len(final_value) == 1:
        return final_value[0]
    else:
        return None


def pair(a):
    """
    To check for a highest pair in the set, Takes the player cards and
    community cards as input, and checks for the two pairs among the
    players and returns the players value. Does not return any cards if
    multiple or no two pair cards are detected, it is then directed to the
    next check function!
    """
    rank = ["2", "3", "4", "5", "6", "7", "8", "9",
            "10", "J", "Q", "K", "A"]
    playercommunitycards = a
    playervalue = [[playercommunitycards[0][0], playercommunitycards[0][1]]]
    communityvalue = []
    if len(playercommunitycards) == 5:
        communityvalue = [[playercommunitycards[0][2],
                          playercommunitycards[0][3],
                          playercommunitycards[0][4]]]
    elif len(playercommunitycards) == 6:
        communityvalue = [[playercommunitycards[0][2],
                          playercommunitycards[0][3],
                          playercommunitycards[0][4],
                          playercommunitycards[0][5]]]
    elif len(playercommunitycards) == 7:
        communityvalue = [[playercommunitycards[0][2],
                          playercommunitycards[0][3],
                          playercommunitycards[0][4],
                          playercommunitycards[0][5],
                          playercommunitycards[0][7]]]
    # print(playervalue)
    # print(communityvalue)
    new_value = []
    player = []
    pvalue = []
    cvalue = []
    for items in playervalue:
        for item in items:
            player.append(item.split("_")[0])
        pvalue.append(player)
        player = []
    # print(pvalue)
    for items in communityvalue:
        for item in items:
            cvalue.append(item.split("_")[0])
    # print(cvalue)
    for pos, items in enumerate(pvalue):
        if items[0] == items[1]:
            player.append([pos, items[0]])
        for item in items:
            if item in cvalue:
                player.append([pos, item])
        # print(player)
        new_value.append(player)
        player = []
    # print(new_value)
    pair_rank = []
    player = []
    for items in new_value:
        for item in items:
            for pos, ranking in enumerate(rank):
                if ranking == item[1]:
                    player.append([pos, item])
            pair_rank.append(player)
            player = []
    pair_rank = sorted(pair_rank)
    # print(pair_rank)
    if len(pair_rank) == 1:
        return pair_rank[0][0][0]
    elif len(pair_rank) > 1:
        if pair_rank[-2][0][0] != pair_rank[-1][0][0]:
            return pair_rank[-1][0][0]
        else:
            return None
    else:
        return None


def high_card(a):
    """
    To check the highest card in the set, Takes the player cards as input
    (Just the players cards and excluding the community cards.), and checks
    for the high cards among the players, and returns the players and high
    cards value. Does not return any cards if multiple high cards are
    detected, it is then directed to the second high card function.
    """
    rank = ["2", "3", "4", "5", "6", "7", "8", "9",
            "10", "J", "Q", "K", "A"]
    card_rank = []
    final_card_rank = []
    playercommunitycards = a
    player = []
    # print(playercommunitycards)
    playervalue = [[playercommunitycards[0][0], playercommunitycards[0][1]]]
    # print(playervalue)
    value = []
    for items in playervalue:
        for item in items:
            player.append(item.split("_")[0])
        value.append(player)
        player = []
    # print(value)
    for items in value:
        value1, value2 = items[0], items[1]
        for position, item in enumerate(rank):
            if item == value1:
                player.append((position, value1))
            elif item == value2:
                player.append((position, value2))
        if len(player) > 1:
            if player[0][0] > player[1][0]:
                card_rank.append(player[0])
            elif player[0][0] < player[1][0]:
                card_rank.append(player[1])
        # print(player)
        player = []
    # print(card_rank)
    new_card_rank = sorted(card_rank)
    # print(new_card_rank)
    for position, item in enumerate(card_rank):
        if new_card_rank[-1] == item:
            final_card_rank.append((position, item))
    # print(final_card_rank)
    if len(final_card_rank) == 1:
        return final_card_rank[0][1][0]
    else:
        return None


def flop_turn_river(fullcards):
    new_final_data = []
    score = 0
    for x in fullcards:
        res = royal_flush([list(x)])
        if res is not None:
            score = score + (150)
            new_final_data.append([x, score])
        else:
            new_final_data.append([x, score])
        score = 0
        res = 0
    anew_final_data = []
    for pos, x in enumerate(fullcards):
        res = straight_flush([list(x)])
        if res is not None:
            score = score + (140)
            o = new_final_data[pos][-1]
            score = score + o
            anew_final_data.append([x, score])
        else:
            o = new_final_data[pos][-1]
            score = score + o
            anew_final_data.append([x, score])
        score = 0
        res = 0
    bnew_final_data = []
    for pos, x in enumerate(fullcards):
        res = four_of_a_kind([list(x)])
        if res is not None:
            score = score + (130)
            o = anew_final_data[pos][-1]
            score = score + o
            bnew_final_data.append([x, score])
        else:
            o = anew_final_data[pos][-1]
            score = score + o
            bnew_final_data.append([x, score])
        score = 0
        res = 0
    cnew_final_data = []
    for pos, x in enumerate(fullcards):
        res = full_house([list(x)])
        if res is not None:
            score = score + (120)
            o = bnew_final_data[pos][-1]
            score = score + o
            cnew_final_data.append([x, score])
        else:
            o = bnew_final_data[pos][-1]
            score = score + o
            cnew_final_data.append([x, score])
        score = 0
        res = 0
    dnew_final_data = []
    for pos, x in enumerate(fullcards):
        res = flush([list(x)])
        if res is not None:
            score = score + (110)
            o = cnew_final_data[pos][-1]
            score = score + o
            dnew_final_data.append([x, score])
        else:
            o = cnew_final_data[pos][-1]
            score = score + o
            dnew_final_data.append([x, score])
        score = 0
        res = 0
    enew_final_data = []
    for pos, x in enumerate(fullcards):
        res = straight([list(x)])
        if res is not None:
            score = score + (100)
            o = dnew_final_data[pos][-1]
            score = score + o
            enew_final_data.append([x, score])
        else:
            o = dnew_final_data[pos][-1]
            score = score + o
            enew_final_data.append([x, score])
        score = 0
        res = 0
    fnew_final_data = []
    for pos, x in enumerate(fullcards):
        res = three_of_a_kind([list(x)])
        if res is not None:
            score = score + (90)
            o = enew_final_data[pos][-1]
            score = score + o
            fnew_final_data.append([x, score])
        else:
            o = enew_final_data[pos][-1]
            score = score + o
            fnew_final_data.append([x, score])
        score = 0
        res = 0
    gnew_final_data = []
    for pos, x in enumerate(fullcards):
        res = two_pair([list(x)])
        if res is not None:
            score = score + (80)
            o = fnew_final_data[pos][-1]
            score = score + o
            gnew_final_data.append([x, score])
        else:
            o = fnew_final_data[pos][-1]
            score = score + o
            gnew_final_data.append([x, score])
        score = 0
        res = 0
    hnew_final_data = []
    for pos, x in enumerate(fullcards):
        res = pair([list(x)])
        if res is not None:
            score = score + (res * 5)
            o = gnew_final_data[pos][-1]
            score = score + o
            hnew_final_data.append([x, score])
        else:
            o = gnew_final_data[pos][-1]
            score = score + o
            hnew_final_data.append([x, score])
        score = 0
        res = 0
    inew_final_data = []
    for pos, x in enumerate(fullcards):
        res = high_card([list(x)])
        if res is not None:
            score = score + (res)
            o = hnew_final_data[pos][-1]
            score = score + o
            inew_final_data.append([x, score])
        else:
            o = hnew_final_data[pos][-1]
            score = score + o
            inew_final_data.append([x, score])
        score = 0
        res = 0
        return (inew_final_data[-1]/1000)
