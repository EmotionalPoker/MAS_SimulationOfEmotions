# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 21:37:28 2019

@author: battu
"""

from PokerGame import *


#OpenAI Gym Environment for Poker
class PokerEnvironment(object):
    
    
    def __init__(self,players_list):
        self.n_players = len(players_list)
        self.player_objects = players_list
        
        #Place to delcare or use emotions for dealer, if any.
        self.shuffler_emotion = None
        
        self.deck_object = Deck()
        self.deck_object.build_deck()
        
        for i in range(random.randint(1,5)):
            self.deck_object.shuffle_deck()
        
        self.main_deck = self.deck_object.return_deck()
        
        
        pass
    
    def reset(self):
        #Make each player draw 2 cards from deck, or deal 2 cards to each player.
        for i in range(self.n_players):
            
            self.player_objects[i].player.draw_hand(self.main_deck)
            self.player_objects[i].player.draw_hand(self.main_deck)
            self.player_objects[i].hand = self.player_objects[i].player.return_hand()
            
        pass
    
    def step(self,action):
        pass
    
    def render(self):
        pass
        # We show the flask or html game here, when it is implemented
        #Send all information as json to frontend code, where it is rendered.
        
    def pre_flop(self):
        
        
        
        pass
    def flop(self):
        pass
    def turn(self):
        pass
    def river(self):
        pass
    
    def show(self):
        for i in range(self.n_players):
            print(self.player_objects[i].hand)
            
    







        
class Agent(object):
    
    def __init__(self,player_object,coins):
        self.current_coins = coins
        self.player = player_object
        self.hand = None
        self.P_rp=0
    
    
    
        
    def calculate_probability_of_hand(self,hand):
        self.P_rp = self.P_RoyalFlush(hand)
        
        pass
    
    
    def P_RoyalFlush(self,hand):
        
        ranks,suits = [x.split("_")[0] for x in a.hand],[x.split("_")[1] for x in a.hand]
        if suits[0]!=suits[1]:
            return 0.0
        else:
            if ranks[0] not in ["10", "J", "Q", "K", "A"] or ranks[1] not in ["10", "J", "Q", "K", "A"]:
                return 0.0
            else:
                # This is the standard probability of a royal flush
                return 0.000154
    def P_StraightFlush(self,hand):
        ranks,suits = [x.split("_")[0] for x in a.hand],[x.split("_")[1] for x in a.hand]
        
        pass
    
    #More functions to be written for probability calculation
    
    

        
        
### Testing Area      
players_list = []
for i in range(8):
    p = Player()
    a = Agent(p,1000)
    players_list.append(a)
    
env = PokerEnvironment(players_list)
env.reset()
env.show()




'''
while True:
    deck = Deck()
    deck.build_deck()
    deck.shuffle_deck()
    deck.shuffle_deck()
    deck.shuffle_deck()
    deck.shuffle_deck()
    deck.shuffle_deck()
    shuffle_deck = deck.return_deck()  
    player1 = Player()
    a = Agent(player1)
    a.player.draw_hand(shuffle_deck)
    a.player.draw_hand(shuffle_deck)
    a.hand = a.player.return_hand()
    if a.P_rp!=0.0:
        break
    print(1,)
    
 '''   

    
    


