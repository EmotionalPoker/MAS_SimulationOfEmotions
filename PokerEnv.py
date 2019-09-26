# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 21:37:28 2019

@author: battu
"""

from PokerGame import *

action_dictionary = {'pre_flop':['CALL','RAISE','FOLD'],'flop':[]}
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
        
        self.stage = None
        self.minimum_bet_amount = 10
        self.bets_placed = []
        self.pointer = 0
        self.folden_indexes = []
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
        
    def set_stage(self):
        for i in range(self.n_players):
            self.player_objects[i].set_stage(self.stage)
            
    def del_folden_index(self,a,b,index):
            del a[index]
            try:
                del b[index]
            except Exceptions as e:
                pass
            return a,b
    def get_player_actions(self):
        
        action_list = action_dictionary[self.stage]
        
        for i in range(self.n_players):
            action = self.player_objects[i].make_decision(self.bets_placed,i,None)
            
            action_str = action_list[action]
            if self.stage == 'pre_flop':
                
                if action_str == 'CALL':
                    
                    if len(self.bets_placed)>0:
                        
                        bet_amount  = self.minimum_bet_amount
                        self.pointer = i
                        try:
                            self.bets_placed[i] = bet_amount
                        except Exception as e:
                            self.bets_placed.append(bet_amount)
                        self.player_objects[i].current_coins -= bet_amount
                        self.minimum_bet_amount = bet_amount
                        
                    else:
                        self.bets_placed.append(self.minimum_bet_amount)
                        self.player_objects[i].current_coins -= self.minimum_bet_amount
                if action_str == "RAISE":
                    if len(self.bets_placed)>0:
                        bet_amount = self.minimum_bet_amount*2
                        self.pointer = i
                        try:
                            self.bets_placed[i] = bet_amount
                        except Exception as e:
                            self.bets_placed.append(bet_amount)
                        self.player_objects[i].current_coins -= bet_amount
                        self.minimum_bet_amount = bet_amount
                        
                    else:
                        self.bets_placed.append(self.minimum_bet_amount*2)
                        self.minimum_bet_amount *= 2
                        self.player_objects[i].current_coins -= self.minimum_bet_amount
                
                if action_str == "FOLD":
                    self.folden_indexes.append(i)
                    #del self.player_objects[i]
                    
        self.n_players -= len(self.folden_indexes)
        
            
        for j in range(len(self.folden_indexes)):
            self.player_objects,self.bets_placed = self.del_folden_index(self.player_objects,self.bets_placed,self.folden_indexes[j])
            
            self.folden_indexes = [x-1 for x in self.folden_indexes]
        self.folden_indexes=[]
        maximum = max(self.bets_placed)
        temp = self.bets_placed
        temp  = [x - maximum for x in temp]
        if sum(temp) != 0:
            self.get_player_actions()
            
                        
                    
                        
                        
                    
        
        
    def pre_flop(self):
        
        self.stage = 'pre_flop'
        self.set_stage()
        self.get_player_actions()
        
        
        
        
        
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
        self.stage = None
        self.P_rp=0
        
        
        self.available_actions = None
        
    def set_stage(self,stage):
        self.stage = stage
        self.available_actions = action_dictionary[self.stage]
        
    def make_decision(self, bets_placed,player_id,community_cards):
        print("Bets Placed")
        print(bets_placed,self.current_coins)
        print("Player ID:",player_id)
        a = input("Input for player:")
        return int(a)
        pass
    
    
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
env.pre_flop()



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

    
    


