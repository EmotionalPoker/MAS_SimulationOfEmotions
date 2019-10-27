# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 21:37:28 2019

@author: Hari Vidharth
"""

import random
import itertools
import time


class Card:
    """
    Card class to create and return a card object.
    """
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def return_card(self):
        """
        Returns card object in the format CardRank_CardSuit.
        """
        return "{}_{}".format(self.value, self.suit)


class Deck:
    """
    Deck class builds the deck of cards consisting of card objects in straight
    and/or shuffle format.
    """
    def __init__(self):
        self.cards = []

    def build_deck(self):
        """
        Builds the deck of cards in straight format.
        """
        for suit in ["♣", "♦", "♥", "♠"]:
            for value in range(2, 15):
                if value == 11:
                    value = "J"
                elif value == 12:
                    value = "Q"
                elif value == 13:
                    value = "K"
                elif value == 14:
                    value = "A"
                self.cards.append(Card(value, suit))

    def shuffle_deck(self):
        """
        Shuffles the deck of cards in a random format.
        """
        for _ in range(0, len(self.cards)):
            random_card = random.randint(0, len(self.cards) - 1)
            (self.cards[_], self.cards[random_card]) = (
                                        self.cards[random_card], self.cards[_])

    def return_deck(self):
        """
        Returns the deck of card objects in a list in straight and/or shuffle
        format.
        """
        return_deck = []
        for _ in self.cards:
            return_deck.append(_.return_card())
        return return_deck


class Player:
    """
    Class to manually add players to the poker game and draw and returns the
    players's hand cards.
    """
    def __init__(self):
        self.hand = []

    def draw_hand(self, _):
        """
        Draw cards from the deck for the player.
        """
        self.hand.append(_.pop())

    def return_hand(self):
        """
        Returns the player's hand cards.
        """
        return_hand = []
        for _ in self.hand:
            return_hand.append(_)
        return return_hand


class Poker:
    """
    Class defining poker rules, takes the player cards and the community cards
    as input for the class to be used by the individual check functions!
    """
    def __init__(self, communitycards, *player_cards):
        self.playercards = []
        self.communitycards = communitycards
        for items in player_cards:
            for item in items:
                self.playercards.append(item)
        print(self.playercards)
        print(self.communitycards)

    def royal_flush(self):
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
        playercommunitycards = []
        player = []
        flushcount = []
        playercount = []
        flushplayercount = []
        for item in self.playercards:
            playercommunitycards.append(item+self.communitycards)
        # print(playercommunitycards)
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
        for items in new_royal:
            return items

    def straight_flush(self):
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
        playercommunitycards = []
        player = []
        flushcount = []
        playercount = []
        flushplayercount = []
        for item in self.playercards:
            playercommunitycards.append(item+self.communitycards)
        # print(playercommunitycards)
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
            if items[0][-1] - items[0][0] == 4:
                straightplayer.append(pos)
        # print(straightplayer)
        for item in straightplayer:
            for items in flushplayercount:
                if item in items:
                    return item
                else:
                    return None

    def four_of_a_kind(self):
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
        playercommunitycards = []
        player = []
        for item in self.playercards:
            playercommunitycards.append(item+self.communitycards)
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

    def full_house(self):
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
        playercommunitycards = []
        player = []
        for item in self.playercards:
            playercommunitycards.append(item+self.communitycards)
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
        playervalue = []
        communityvalue = []
        player = []
        for items in self.playercards:
            for item in items:
                player.append(item.split("_")[0])
            playervalue.append(player)
            player = []
        for item in self.communitycards:
            communityvalue.append(item.split("_")[0])
        # print(playervalue)
        # print(communityvalue)
        new_value = []
        player = []
        for pos, items in enumerate(playervalue):
            if items[0] == items[1]:
                player.append([pos, items[0]])
            for item in items:
                if item in communityvalue:
                    player.append([pos, item])
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
        if len(playercount) == 1:
            for pos, items in enumerate(playercount):
                return pos
        else:
            return None

    def straight(self):
        """
         Checks for the value of the cards are according to the straight
         rank and returns the player whose cards matches, to check for a
         STRAIGHT, returns the player if winner else returns None and moves
         to the next check function!
         """
        playercommunitycards = []
        player = []
        for item in self.playercards:
            playercommunitycards.append(item+self.communitycards)
        # print(playercommunitycards)
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
            if items[0][-1] - items[0][0] == 4:
                straightplayer.append(pos)
        # print(straightplayer)
        if len(straightplayer) == 1:
            return straightplayer[0]
        else:
            return None

    def flush(self):
        """
        To check for a flush in the set, Takes the player cards and community
        cards as input, and checks for a flush among the players, and returns
        the players and flush cards value. Does not return any cards if
        multiple flush cards or no flush cards are detected, and is then
        directed to the next check function!
        """
        suit = []
        playercommunitycards = []
        player = []
        flushcount = []
        playercount = []
        flushplayercount = []
        for item in self.playercards:
            playercommunitycards.append(item+self.communitycards)
        # print(playercommunitycards)
        for items in playercommunitycards:
            for item in items:
                player.append(item.split("_")[1])
            suit.append(player)
            player = []
        print(suit)
        cardclass = ["♣", "♦", "♥", "♠"]
        for items in cardclass:
            for item in suit:
                flushcount.append(item.count(items))
            # print(flushcount)
            for position, item in enumerate(flushcount):
                if item > 5:
                    playercount.append(position)
            # print(playercount)
            flushplayercount.append(playercount)
            playercount = []
            flushcount = []
        print(flushplayercount)
        finalflush = []
        for items in flushplayercount:
            if len(items) == 1:
                finalflush.append(items)
        print(finalflush)
        if len(finalflush) != 0:
            for items in finalflush:
                if len(items) == 1:
                    return items[0]
                else:
                    return None

    def three_of_a_kind(self):
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
        playercommunitycards = []
        player = []
        for item in self.playercards:
            playercommunitycards.append(item+self.communitycards)
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
        if len(new_three_of_a_kind) == 1:
            return new_three_of_a_kind[0]
        else:
            return None

    def two_pair(self):
        """
        To check for a two pair in the set, Takes the player cards and
        community cards as input, and checks for the two pairs among the
        players and returns the players value. Does not return any cards if
        multiple or no two pair cards are detected, it is then directed to the
        next check function!
        """
        playervalue = []
        communityvalue = []
        player = []
        for items in self.playercards:
            for item in items:
                player.append(item.split("_")[0])
            playervalue.append(player)
            player = []
        for item in self.communitycards:
            communityvalue.append(item.split("_")[0])
        # print(playervalue)
        # print(communityvalue)
        new_value = []
        player = []
        for pos, items in enumerate(playervalue):
            if items[0] == items[1]:
                player.append([pos, items[0]])
            for item in items:
                if item in communityvalue:
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

    def pair(self):
        """
        To check for a highest pair in the set, Takes the player cards and
        community cards as input, and checks for the two pairs among the
        players and returns the players value. Does not return any cards if
        multiple or no two pair cards are detected, it is then directed to the
        next check function!
        """
        rank = ["2", "3", "4", "5", "6", "7", "8", "9",
                "10", "J", "Q", "K", "A"]
        playervalue = []
        communityvalue = []
        player = []
        for items in self.playercards:
            for item in items:
                player.append(item.split("_")[0])
            playervalue.append(player)
            player = []
        for item in self.communitycards:
            communityvalue.append(item.split("_")[0])
        # print(playervalue)
        # print(communityvalue)
        new_value = []
        player = []
        for pos, items in enumerate(playervalue):
            if items[0] == items[1]:
                player.append([pos, items[0]])
            for item in items:
                if item in communityvalue:
                    player.append([pos, item])
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
            return pair_rank[0][0][1][0]
        elif len(pair_rank) > 1:
            if pair_rank[-2][0][0] != pair_rank[-1][0][0]:
                return pair_rank[-1][0][1][0]
            else:
                return None
        else:
            return None

    def high_card(self):
        """
        To check the highest card in the set, Takes the player cards as input
        (Just the players cards and excluding the community cards.), and checks
        for the high cards among the players, and returns the players and high
        cards value. Does not return any cards if multiple high cards are
        detected, it is then directed to the second high card function.
        """
        rank = ["2", "3", "4", "5", "6", "7", "8", "9",
                "10", "J", "Q", "K", "A"]
        player = []
        value = []
        card_rank = []
        final_card_rank = []
        for items in self.playercards:
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
            else:
                card_rank.append(player[0])
            player = []
        # print(card_rank)
        new_card_rank = sorted(card_rank)
        # print(new_card_rank)
        for position, item in enumerate(card_rank):
            if new_card_rank[-1] == item:
                final_card_rank.append((position, item))
        # print(final_card_rank)
        if len(final_card_rank) == 1:
            return final_card_rank[0][0]
        else:
            return None


class WinnerCheck:
    pass


def test():
    """
    To test the above classes and functions, just for testing purpose.
    """
    card = Card(10, "♠")
    my_card = card.return_card()
    print(my_card)
    deck = Deck()
    deck.build_deck()
    straight_deck = deck.return_deck()
    print(straight_deck)
    deck.shuffle_deck()
    deck.shuffle_deck()
    shuffle_deck = deck.return_deck()
    print(shuffle_deck)
    player1 = Player()
    player1.draw_hand(shuffle_deck)
    player1.draw_hand(shuffle_deck)
    player1_hand = player1.return_hand()
    print(player1_hand)
    player2 = Player()
    player2.draw_hand(shuffle_deck)
    player2.draw_hand(shuffle_deck)
    player2_hand = player2.return_hand()
    print(player2_hand)
    community_cards = Player()
    community_cards.draw_hand(shuffle_deck)
    community_cards.draw_hand(shuffle_deck)
    community_cards.draw_hand(shuffle_deck)
    community_cards.draw_hand(shuffle_deck)
    community_cards.draw_hand(shuffle_deck)
    community_cards_hand = community_cards.return_hand()
    print(community_cards_hand)
    player1_hand = player1_hand + community_cards_hand
    print(player1_hand)
    player2_hand = player2_hand + community_cards_hand
    print(player2_hand)
    print(shuffle_deck)
    win_condition = Poker()
    high_card1 = win_condition.high_card(player1_hand)
    print(high_card1)
    high_card2 = win_condition.high_card(player2_hand)
    print(high_card2)
    flush1 = win_condition.flush(player1_hand)
    print(flush1)
    flush2 = win_condition.flush(player2_hand)
    print(flush2)
    pair1 = win_condition.pair_two_pair(player1_hand)
    print(pair1)
    pair2 = win_condition.pair_two_pair(player2_hand)
    print(pair2)
    triplet1 = win_condition.triplet(player1_hand)
    print(triplet1)
    triplet2 = win_condition.triplet(player2_hand)
    print(triplet2)
    four_of_a_kind1 = win_condition.four_of_a_kind(player1_hand)
    print(four_of_a_kind1)
    four_of_a_kind2 = win_condition.four_of_a_kind(player2_hand)
    print(four_of_a_kind2)
    straight1 = win_condition.straight(player1_hand)
    print(straight1)
    straight2 = win_condition.straight(player2_hand)
    print(straight2)


def hello_world_bot():
    """
    A sample of the game, Two primitive bots playing a game of poker and a
    winner is decided at the end of 10 rounds.
    """
    time.sleep(1)
    ranking = ["Royal Flush", "Straight Flush", "Four of a Kind", "Full House",
               "Flush", "Straight", "Three of a Kind", "Two Pairs", "Pair",
               "High Card"]
    print("Welcome to Poker Game!")
    print("♣ ♦ ♥ ♠")
    print(" ")
    win_condition = Poker()
    print("Player1 has joined the game!")
    print("Player2 has joined the game!")
    print(" ")
    rounds = 1
    player1_points = 0
    player2_points = 0
    while True:
        time.sleep(1)
        player1_rank = []
        player2_rank = []
        deck = Deck()
        deck.build_deck()
        deck.shuffle_deck()
        deck.shuffle_deck()
        deck.shuffle_deck()
        deck.shuffle_deck()
        deck.shuffle_deck()
        shuffle_deck = deck.return_deck()
        print("Round " + str(rounds) + "!")
        print(" ")
        print("Shuffled Deck!")
        print(shuffle_deck)
        print(" ")
        player1 = Player()
        player2 = Player()
        player1.draw_hand(shuffle_deck)
        player1.draw_hand(shuffle_deck)
        player1_hand = player1.return_hand()
        print("Player1 Hand!")
        print(player1_hand)
        player2.draw_hand(shuffle_deck)
        player2.draw_hand(shuffle_deck)
        player2_hand = player2.return_hand()
        print("Player2 Hand!")
        print(player2_hand)
        community_cards = Player()
        community_cards.draw_hand(shuffle_deck)
        community_cards.draw_hand(shuffle_deck)
        community_cards.draw_hand(shuffle_deck)
        community_cards.draw_hand(shuffle_deck)
        community_cards.draw_hand(shuffle_deck)
        community_cards_hand = community_cards.return_hand()
        print("Community Cards!")
        print(community_cards_hand)
        print(" ")
        player1_cHand = player1_hand + community_cards_hand
        player2_cHand = player2_hand + community_cards_hand
        royal1, flush1 = win_condition.royal_flush(player1_cHand)
        if royal1 is not None and flush1 is not None:
            player1_rank.append("Royal Flush")
        royal2, flush2 = win_condition.royal_flush(player2_cHand)
        if royal2 is not None and flush2 is not None:
            player2_rank.append("Royal Flush")
        straight1, flush1 = win_condition.straight_flush(player1_cHand)
        if straight1 is not None and flush1 is not None:
            player1_rank.append("Straight Flush")
        straight2, flush2 = win_condition.straight_flush(player2_cHand)
        if straight2 is not None and flush2 is not None:
            player2_rank.append("Straight Flush")
        four_of_a_kind1 = win_condition.four_of_a_kind(player1_cHand)
        if four_of_a_kind1 is not None:
            player1_rank.append("Four of a Kind")
        four_of_a_kind2 = win_condition.four_of_a_kind(player2_cHand)
        if four_of_a_kind2 is not None:
            player2_rank.append("Four of a Kind")
        straight1 = win_condition.straight(player1_cHand)
        if straight1 is not None:
            player1_rank.append("Straight")
        straight2 = win_condition.straight(player2_cHand)
        if straight2 is not None:
            player2_rank.append("Straight")
        full_house1_triplet, full_house1_pair = win_condition.full_house(
            player1_cHand)
        if full_house1_triplet is not None and full_house1_pair is not None:
            player1_rank.append("Full House")
        full_house2_triplet, full_house2_pair = win_condition.full_house(
            player2_cHand)
        if full_house2_triplet is not None and full_house2_pair is not None:
            player2_rank.append("Full House")
        flush1 = win_condition.flush(player1_cHand)
        if flush1 is not None:
            player1_rank.append("Flush")
        flush2 = win_condition.flush(player2_cHand)
        if flush2 is not None:
            player2_rank.append("Flush")
        triplet1 = win_condition.triplet(player1_cHand)
        if triplet1 is not None:
            player1_rank.append("Three of a Kind")
        triplet2 = win_condition.triplet(player2_cHand)
        if triplet2 is not None:
            player2_rank.append("Three of a Kind")
        two_pair1 = win_condition.two_pair(player1_cHand)
        if two_pair1 is not None:
            player1_rank.append("Two Pairs")
        two_pair2 = win_condition.two_pair(player2_cHand)
        if two_pair2 is not None:
            player2_rank.append("Two Pairs")
        pair1 = win_condition.pair(player1_cHand)
        if pair1 is not None:
            player1_rank.append("Pair")
        pair2 = win_condition.pair(player2_cHand)
        if pair2 is not None:
            player2_rank.append("Pair")
        high_card1 = win_condition.high_card(player1_cHand)
        if high_card1 is not None:
            player1_rank.append("High Card")
        high_card2 = win_condition.high_card(player2_cHand)
        if high_card2 is not None:
            player2_rank.append("High Card")
        rounds += 1
        position1 = []
        position2 = []
        for position, item in enumerate(ranking):
            if item in player1_rank:
                position1.append((position, item))
        for position, item in enumerate(ranking):
            if item in player2_rank:
                position2.append((position, item))
        if len(position1) != 0:
            print(position1[0][1])
        if len(position2) != 0:
            print(position2[0][1])
        print(" ")
        if (len(position1) != 0 and len(position2) != 0 and position1[0][0] <
                position2[0][0]):
            if position1[0][1] == "Royal Flush":
                player1_points += 100
            elif position1[0][1] == "Straight Flush":
                player1_points += 90
            elif position1[0][1] == "Four of a Kind":
                player1_points += 80
            elif position1[0][1] == "Full House":
                player1_points += 70
            elif position1[0][1] == "Flush":
                player1_points += 60
            elif position1[0][1] == "Straight":
                player1_points += 50
            elif position1[0][1] == "Three of a Kind":
                player1_points += 40
            elif position1[0][1] == "Two Pairs":
                player1_points += 30
            elif position1[0][1] == "Pair":
                player1_points += 20
            elif position1[0][1] == "High Card":
                player1_points += 10
            elif position[0][1] is None:
                player1_points += 0
            else:
                player1_points += 0
        elif (len(position1) != 0 and len(position2) != 0 and position2[0][0] <
                position1[0][0]):
            if position2[0][1] == "Royal Flush":
                player2_points += 100
            elif position2[0][1] == "Straight Flush":
                player2_points += 90
            elif position2[0][1] == "Four of a Kind":
                player2_points += 80
            elif position2[0][1] == "Full House":
                player2_points += 70
            elif position2[0][1] == "Flush":
                player2_points += 60
            elif position2[0][1] == "Straight":
                player2_points += 50
            elif position2[0][1] == "Three of a Kind":
                player2_points += 40
            elif position2[0][1] == "Two Pairs":
                player2_points += 30
            elif position2[0][1] == "Pair":
                player2_points += 20
            elif position2[0][1] == "High Card":
                player2_points += 10
            elif position[0][1] is None:
                player2_points += 0
            else:
                player2_points += 0
        elif len(position1) != 0:
            if position1[0][1] == "Royal Flush":
                player1_points += 100
            elif position1[0][1] == "Straight Flush":
                player1_points += 90
            elif position1[0][1] == "Four of a Kind":
                player1_points += 80
            elif position1[0][1] == "Full House":
                player1_points += 70
            elif position1[0][1] == "Flush":
                player1_points += 60
            elif position1[0][1] == "Straight":
                player1_points += 50
            elif position1[0][1] == "Three of a Kind":
                player1_points += 40
            elif position1[0][1] == "Two Pairs":
                player1_points += 30
            elif position1[0][1] == "Pair":
                player1_points += 20
            elif position1[0][1] == "High Card":
                player1_points += 10
            elif position[0][1] is None:
                player1_points += 0
            else:
                player1_points += 0
        elif len(position1) != 0:
            if position2[0][1] == "Royal Flush":
                player2_points += 100
            elif position2[0][1] == "Straight Flush":
                player2_points += 90
            elif position2[0][1] == "Four of a Kind":
                player2_points += 80
            elif position2[0][1] == "Full House":
                player2_points += 70
            elif position2[0][1] == "Flush":
                player2_points += 60
            elif position2[0][1] == "Straight":
                player2_points += 50
            elif position2[0][1] == "Three of a Kind":
                player2_points += 40
            elif position2[0][1] == "Two Pairs":
                player2_points += 30
            elif position2[0][1] == "Pair":
                player2_points += 20
            elif position2[0][1] == "High Card":
                player2_points += 10
            elif position[0][1] is None:
                player2_points += 0
            else:
                player2_points += 0
        else:
            player1_points += 0
            player2_points += 0
        print("Player1: " + str(player1_points))
        print("Player2: " + str(player2_points))
        print(" ")
        time.sleep(1)
        if rounds > 10:
            if int(player1_points) > int(player2_points):
                print("Player1 is the winner")
            elif int(player2_points) > int(player1_points):
                print("Player2 is the winner")
            else:
                print("The Poker game is a draw")
            print(" ")
            print("Player1 has left the game!")
            print("Player2 has left the game!")
            print(" ")
            print("Thank you for playing!")
            print("Exiting...!!!")
            time.sleep(1)
            break


def test2():
    """
    To test the above classes and functions, just for testing purpose.
    """
    deck = Deck()
    deck.build_deck()
    deck.shuffle_deck()
    deck.shuffle_deck()
    deck.shuffle_deck()
    deck.shuffle_deck()
    deck.shuffle_deck()
    shuffle_deck = deck.return_deck()
    print(" ")
    print("Shuffled Deck!")
    print(shuffle_deck)
    print(" ")
    player1 = Player()
    player2 = Player()
    player3 = Player()
    player4 = Player()
    player5 = Player()
    player1.draw_hand(shuffle_deck)
    player1.draw_hand(shuffle_deck)
    player1_hand = player1.return_hand()
    print("Player1 Hand!")
    print(player1_hand)
    player2.draw_hand(shuffle_deck)
    player2.draw_hand(shuffle_deck)
    player2_hand = player2.return_hand()
    print("Player2 Hand!")
    print(player2_hand)
    player3.draw_hand(shuffle_deck)
    player3.draw_hand(shuffle_deck)
    player3_hand = player3.return_hand()
    print("Player3 Hand!")
    print(player3_hand)
    player4.draw_hand(shuffle_deck)
    player4.draw_hand(shuffle_deck)
    player4_hand = player4.return_hand()
    print("Player4 Hand!")
    print(player4_hand)
    player5.draw_hand(shuffle_deck)
    player5.draw_hand(shuffle_deck)
    player5_hand = player5.return_hand()
    print("Player5 Hand!")
    print(player5_hand)
    community_cards = Player()
    community_cards.draw_hand(shuffle_deck)
    community_cards.draw_hand(shuffle_deck)
    community_cards.draw_hand(shuffle_deck)
    community_cards.draw_hand(shuffle_deck)
    community_cards.draw_hand(shuffle_deck)
    community_cards_hand = community_cards.return_hand()
    print("Community Cards!")
    print(community_cards_hand)
    print(" ")


if __name__ == "__main__":
    # test()
    # hello_world_bot()
    test2()
