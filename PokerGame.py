# coding=utf-8
import random
import itertools
import time


class Card:
    #Card class to create and return a card object.
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def return_card(self):
        #Returns card object in the format CardRank_CardSuit.
        return "{}_{}".format(self.value, self.suit)


class Deck:
    #Deck class builds the deck of cards consisting of card objects in straight and/or shuffle format. 
    def __init__(self):
        self.cards = []

    def build_deck(self):
        #Builds the deck of cards in straight format.
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
        #Shuffles the deck of cards in a random format.
        for _ in range(0, len(self.cards)):
            random_card = random.randint(0, len(self.cards) - 1)
            self.cards[_], self.cards[random_card] = self.cards[random_card], self.cards[_]

    def return_deck(self):
        #Returns the deck of card objects in a list in straight and/or shuffle format.
        return_deck = []
        for _ in self.cards:
            return_deck.append(_.return_card())
        return return_deck


class Player:
    #Class to manually add players to the poker game and draw and returns the players's hand cards.
    def __init__(self):
        self.hand = []

    def draw_hand(self, _):
        #Draw cards from the deck for the player.
        self.hand.append(_.pop())

    def return_hand(self):
        #Returns the player's hand cards.
        return_hand = []
        for _ in self.hand:
            return_hand.append(_)
        return return_hand


class Poker:
    #Class defining poker rules.
    def high_card(self, _):
        #To check the highest card in the set, Takes the player cards as input(Just the players cards and excluding the community cards.) and returs the highest card in the set.
        rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        value = []
        card_rank = []
        for item in _:
            value.append(item.split("_")[0])
        value1, value2 = value[0], value[1]
        for position, item in enumerate(rank):
            if item == value1:
                card_rank.append((position, value1))
            elif item == value2:
                card_rank.append((position, value2))
        if len(card_rank) > 1:
            if card_rank[0][0] >= card_rank[1][0]:
                return card_rank[0][1]
            else:
                return card_rank[1][1]
        else:
            return card_rank[0][1]

    def flush(self, _):
        #To check for a FLUSH(cards belonging to same deck.), Takes the player + community cards as inputs and checks for FLUSH, Returns the card suit if suit matches, Else return NONE.
        suit = []
        for item in _:
            suit.append(item.split("_")[1])
        club = "♣"
        diamond = "♦"
        heart = "♥"
        spade = "♠"
        cflush = True
        dflush = True
        hflush = True
        sflush = True
        for item in suit:
            if club != item:
                cflush = False
                break
        for item in suit:
            if diamond != item:
                dflush = False
                break
        for item in suit:
            if heart != item:
                hflush = False
                break
        for item in suit:
            if spade != item:
                sflush = False
                break
        if cflush:
            return suit
        elif dflush:
            return suit
        elif hflush:
            return suit
        elif sflush:
            return suit
        else:
            return None

    def pair(self, _):
        #To check for a pair, Takes the player + community cards as input and returns the value of the pair if there is a match, Else returns NONE.
        value = []
        for item in _:
            value.append(item.split("_")[0])
        player_cards = [value[0], value[1]]
        community_cards = [value[2], value[3], value[4]]
        new_value = []
        for value1 in player_cards:
            for value2 in community_cards:
                new_value.append((value1, value2))
        new_value.append(player_cards)
        pair = []
        for item in new_value:
            if item[0] == item[1]:
                pair.append((item[0], item[1]))
        if len(pair) == 1:
            return pair
        else:
            return None

    def two_pair(self, _):
        #To check for a two sets of pair, Takes the player + community cards as input and returns the value of the two sets of pair if there is a match, Else returns NONE.
        value = []
        for item in _:
            value.append(item.split("_")[0])
        player_cards = [value[0], value[1]]
        community_cards = [value[2], value[3], value[4]]
        new_value = []
        for value1 in player_cards:
            for value2 in community_cards:
                new_value.append((value1, value2))
        new_value.append(player_cards)
        two_pair = []
        for item in new_value:
            if item[0] == item[1]:
                two_pair.append((item[0], item[1]))
        if len(two_pair) > 1:
            return two_pair
        else:
            return None

    def three_of_a_kind(self, _):
        #To check for a triplet, Takes the player + community cards as input and returns the value of the triplet if there is a match, Else returns NONE.
        value = []
        for item in _:
            value.append(item.split("_")[0])
        new_value = []
        for value1, value2, value3 in itertools.combinations(value, 3):
            new_value.append((value1, value2, value3))
        triplet = []
        for item in new_value:
            if item[0] == item[1] and item[1] == item[2]:
                triplet.append((item[0], item[1], item[2]))
        if len(triplet) != 0:
            return triplet
        else:
            return None

    def four_of_a_kind(self, _):
        #To check for four of the same card values, Takes the player + community cards as input and returns the value of the four cards if there is a match, Else returns NONE.
        value = []
        for item in _:
            value.append(item.split("_")[0])
        new_value = []
        for value1, value2, value3, value4 in itertools.combinations(value, 4):
            new_value.append((value1, value2, value3, value4))
        four_of_a_kind = []
        for item in new_value:
            if item[0] == item[1] and item[1] == item[2] and item[2] == item[3]:
                four_of_a_kind.append((item[0], item[1], item[2], item[3]))
        if len(four_of_a_kind) != 0:
            return four_of_a_kind
        else:
            return None

    def full_house(self, _):
        #To check for a FullHouse(Pair + Triplet), Takes the player + community cards as input and returns the value of the pair and triplet if there is a match, Else returns NONE.
        value = []
        for item in _:
            value.append(item.split("_")[0])
        player_cards = [value[0], value[1]]
        community_cards = [value[2], value[3], value[4]]
        new_value = []
        for value1 in player_cards:
            for value2 in community_cards:
                new_value.append((value1, value2))
        new_value.append(player_cards)
        pair = []
        for item in new_value:
            if item[0] == item[1]:
                pair.append((item[0], item[1]))
        value = []
        for item in _:
            value.append(item.split("_")[0])
        new_value = []
        for value1, value2, value3 in itertools.combinations(value, 3):
            new_value.append((value1, value2, value3))
        triplet = []
        for item in new_value:
            if item[0] == item[1] and item[1] == item[2]:
                triplet.append((item[0], item[1], item[2]))
        if len(triplet) == 1 and len(pair) == 1:
            return (triplet, pair)
        else:
            return None, None

    def straight(self, _):
        #To check for a straight set of values, Takes the player + community cards as input and returns the straight values if there is a match, Else returns NONE.
        value = []
        for item in _:
            value.append(item.split("_")[0])
        rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        card_position = []
        card_value = []
        for position, item in enumerate(rank):
            if item in value:
                card_position.append(position)
                card_value.append(item)
        groups = []
        value1 = value2 = card_position[0]
        for item in card_position[1:]:
            if item == value2 + 1:
                value2 = item
            else:
                groups.append(value1 if value1 == value2 else (value1, value2))
                value1 = value2 = item
        groups.append(value1 if value1 == value2 else (value1, value2))
        if len(groups) == 1:
            return card_value
        else:
            return None

    def straight_flush(self, _):
         #To check for a straight set of values, Takes the player + community cards as input and returns the straight values if there is a match, Else returns NONE.
         #To check for a FLUSH(cards belonging to same deck.), Takes the player + community cards as inputs and checks for FLUSH, Returns the card suit if suit matches, Else return NONE.
        suit = []
        for item in _:
            suit.append(item.split("_")[1])
        club = "♣"
        diamond = "♦"
        heart = "♥"
        spade = "♠"
        cflush = True
        dflush = True
        hflush = True
        sflush = True
        for item in suit:
            if club != item:
                cflush = False
                break
        for item in suit:
            if diamond != item:
                dflush = False
                break
        for item in suit:
            if heart != item:
                hflush = False
                break
        for item in suit:
            if spade != item:
                sflush = False
                break
        value = []
        for item in _:
            value.append(item.split("_")[0])
        rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        card_position = []
        card_value = []
        for position, item in enumerate(rank):
            if item in value:
                card_position.append(position)
                card_value.append(item)
        groups = []
        value1 = value2 = card_position[0]
        for item in card_position[1:]:
            if item == value2 + 1:
                value2 = item
            else:
                groups.append(value1 if value1 == value2 else (value1, value2))
                value1 = value2 = item
        groups.append(value1 if value1 == value2 else (value1, value2))
        if len(groups) and cflush:
            return card_value, suit
        elif len(groups) and dflush:
            return card_value, suit
        elif len(groups) and hflush:
            return card_value, suit
        elif len(groups) and sflush:
            return card_value, suit
        else:
            return None, None

    def royal_flush(self, _):
        #To check for a FLUSH(cards belonging to same deck.), Takes the player + community cards as inputs and checks for FLUSH, Returns the card suit if suit matches, Else return NONE.
        #To check if the value of the cards are according to the rank ["10", "J", "Q", "K", "A"]
        suit = []
        for item in _:
            suit.append(item.split("_")[1])
        club = "♣"
        diamond = "♦"
        heart = "♥"
        spade = "♠"
        cflush = True
        dflush = True
        hflush = True
        sflush = True
        for item in suit:
            if club != item:
                cflush = False
                break
        for item in suit:
            if diamond != item:
                dflush = False
                break
        for item in suit:
            if heart != item:
                hflush = False
                break
        for item in suit:
            if spade != item:
                sflush = False
                break
        rank = ["10", "J", "Q", "K", "A"]
        value = []
        count = 0
        for item in _:
            value.append(item.split("_")[0])
        for item in value:
            if item in rank:
                count += 1
        if count == 5 and cflush:
            return count
        elif count == 5 and dflush:
            return count
        elif count == 5 and hflush:
            return count
        elif count == 5 and sflush:
            return count
        else:
            return None, None


def test():
    #To test the above classes and functions, just for testing purpose.
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
    #A sample of the game, Two primitive bots playing a game of poker and a winner is decided at the end of 10 rounds.
    time.sleep(1)
    ranking = ["Royal Flush", "Straight Flush", "Four of a Kind", "Full House", "Flush", "Straight",
               "Three of a Kind", "Two Pairs", "Pair", "High Card"]
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
        if royal1 != None and flush1 != None:
            player1_rank.append("Royal Flush")
        royal2, flush2 = win_condition.royal_flush(player2_cHand)
        if royal2 != None and flush2 != None:
            player2_rank.append("Royal Flush")
        straight1, flush1 = win_condition.straight_flush(player1_cHand)
        if straight1 != None and flush1 != None:
            player1_rank.append("Straight Flush")
        straight2, flush2 = win_condition.straight_flush(player2_cHand)
        if straight2 != None and flush2 != None:
            player2_rank.append("Straight Flush")
        four_of_a_kind1 = win_condition.four_of_a_kind(player1_cHand)
        if four_of_a_kind1 != None:
            player1_rank.append("Four of a Kind")
        four_of_a_kind2 = win_condition.four_of_a_kind(player2_cHand)
        if four_of_a_kind2 != None:
            player2_rank.append("Four of a Kind")
        straight1 = win_condition.straight(player1_cHand)
        if straight1 != None:
            player1_rank.append("Straight")
        straight2 = win_condition.straight(player2_cHand)
        if straight2 != None:
            player2_rank.append("Straight")
        full_house1_triplet, full_house1_pair = win_condition.full_house(player1_cHand)
        if full_house1_triplet != None and full_house1_pair != None:
            player1_rank.append("Full House")
        full_house2_triplet, full_house2_pair = win_condition.full_house(player2_cHand)
        if full_house2_triplet != None and full_house2_pair != None:
            player2_rank.append("Full House")
        flush1 = win_condition.flush(player1_cHand)
        if flush1 != None:
            player1_rank.append("Flush")
        flush2 = win_condition.flush(player2_cHand)
        if flush2 != None:
            player2_rank.append("Flush")
        triplet1 = win_condition.triplet(player1_cHand)
        if triplet1 != None:
            player1_rank.append("Three of a Kind")
        triplet2 = win_condition.triplet(player2_cHand)
        if triplet2 != None:
            player2_rank.append("Three of a Kind")
        two_pair1 = win_condition.two_pair(player1_cHand)
        if two_pair1 != None:
            player1_rank.append("Two Pairs")
        two_pair2 = win_condition.two_pair(player2_cHand)
        if two_pair2 != None:
            player2_rank.append("Two Pairs")
        pair1 = win_condition.pair(player1_cHand)
        if pair1 != None:
            player1_rank.append("Pair")
        pair2 = win_condition.pair(player2_cHand)
        if pair2 != None:
            player2_rank.append("Pair")
        high_card1 = win_condition.high_card(player1_cHand)
        if high_card1 != None:
            player1_rank.append("High Card")
        high_card2 = win_condition.high_card(player2_cHand)
        if high_card2 != None:
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
        if len(position1) != 0 and len(position2) != 0 and position1[0][0] < position2[0][0]:
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
        elif len(position1) != 0 and len(position2) != 0 and position2[0][0] < position1[0][0]:
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


if __name__ == "__main__":
    # test()
    hello_world_bot()
