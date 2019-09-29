# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 21:37:28 2019

@author: battu
"""


# The code for implementing the Cards, decks and flushes.
from PokerGame import *



#List of actions available to players each round
action_dictionary = {'pre_flop':['CALL','RAISE','FOLD'],'flop':['CHECK','BET','RAISE','FOLD'],'turn':['CHECK','BET','RAISE','FOLD'],'river':['CHECK','BET','RAISE','FOLD']}


#Gym Environment for Poker
class PokerEnvironment(object):
    '''
    A list of 'agents' is given to the environment as the game begins.
    A deck is built and randomly shuffled.
    Rest are initialization variables
    
    self.stage tells which round the game is currently in
    self.minimum_bet_amount is the minimum amount of bet a player has to place if he wants to bet.
    self.bets_placed is the array of bets placed by the player.
    self.folden_indexs tells which players have folded.
    self.pot is the total amount of bets placed by all players till the current round.
    self.community_cards is the community cards visible to agents till the current round.
    
    
    '''
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
        self.pot = 0
        self.community_cards = []
        pass
    
    def reset(self):
        #Make each player draw 2 cards from deck, or deal 2 cards to each player.
        for i in range(self.n_players):
            
            self.player_objects[i].player.draw_hand(self.main_deck)
            self.player_objects[i].player.draw_hand(self.main_deck)
            self.player_objects[i].hand = self.player_objects[i].player.return_hand()
            
        pass
    
    
    #Not implemented, can be inherited and implemented later on(This mimics a gym environment)
    def step(self,action):
        pass
    
    
    
    def render(self):
        pass
        # We show the flask or html game here, when it is implemented
        #Send all information as json to frontend code, where it is rendered.
      
        
        
    #Tell each agent object the current stage of the game, this is a simple message function
    def set_stage(self):
        for i in range(self.n_players):
            self.player_objects[i].set_stage(self.stage)
            
    
    #Remove folden players form list
    def del_folden_index(self,a,b,index):
            del a[index]
            try:
                del b[index]
            except Exception as e:
                pass
            return a,b
        
    # This function interacts with agent for each round depending on the decision they make. 
    def get_player_actions(self):
        
        action_list = action_dictionary[self.stage]
        
        for i in range(self.n_players):
            if self.stage == 'pre_flop':
                action,raise_amount = self.player_objects[i].make_decision(self.bets_placed,i,None,self.minimum_bet_amount)
            else:
                action,raise_amount = self.player_objects[i].make_decision(self.bets_placed,i,self.community_cards,self.minimum_bet_amount)
            
            
            action_str = action_list[action]
            if self.stage == 'flop' or self.stage == 'turn' or self.stage == 'river':
                if action_str == "CHECK":
                    try:
                        if self.bets_placed[i-1] > self.bets_placed[i]:
                            i=i-1
                            continue
                        else:
                            pass
                    except Exception as e:
                        if self.bets_placed[-1] > self.bets_placed[i]:
                            i=len(self.bets_placed)-1
                            continue
                        else:
                            pass
                        
                        
                if action_str == "BET":
                    
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
                        bet_amount = raise_amount
                        self.pointer = i
                        try:
                            self.bets_placed[i] = bet_amount
                        except Exception as e:
                            self.bets_placed.append(bet_amount)
                        self.player_objects[i].current_coins -= bet_amount
                        self.minimum_bet_amount = bet_amount
                        
                    else:
                        self.bets_placed.append(raise_amount)
                        self.minimum_bet_amount = raise_amount 
                        self.player_objects[i].current_coins -= self.minimum_bet_amount
                
                if action_str == "FOLD":
                    self.folden_indexes.append(i)
                
                
                
                
                
                
                
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
                        bet_amount = raise_amount
                        self.pointer = i
                        try:
                            self.bets_placed[i] = bet_amount
                        except Exception as e:
                            self.bets_placed.append(bet_amount)
                        self.player_objects[i].current_coins -= bet_amount
                        self.minimum_bet_amount = bet_amount
                        
                    else:
                        self.bets_placed.append(raise_amount)
                        self.minimum_bet_amount = raise_amount 
                        self.player_objects[i].current_coins -= self.minimum_bet_amount
                
                if action_str == "FOLD":
                    self.folden_indexes.append(i)
                    #del self.player_objects[i]
                    
        self.n_players -= len(self.folden_indexes)
        
        
        
        #Remove folded players from the game here.
            
        for j in range(len(self.folden_indexes)):
            self.player_objects,self.bets_placed = self.del_folden_index(self.player_objects,self.bets_placed,self.folden_indexes[j])
            
            self.folden_indexes = [x-1 for x in self.folden_indexes]
        self.folden_indexes=[]
        try:
            maximum = max(self.bets_placed)
        except:
            print("all folded")
            return
        temp = self.bets_placed
        temp  = [x - maximum for x in temp]
        if sum(temp) != 0:
            self.get_player_actions()
            
                        
                    
                        
                        
                    
        
    # High level implementation of pre flop round. 
    def pre_flop(self):
        
        self.stage = 'pre_flop'
        self.set_stage()
        self.get_player_actions()
        self.pot += sum(self.bets_placed)
        for i in range(len(self.bets_placed)):
            self.bets_placed[i] = 0
             
        self.minimum_bet_amount = 10
        
        print('PreFlop Done')
        
        
        
        pass
    #High level implementation of Flop round.
    def flop(self):
        self.dealer = Player()
        self.dealer.draw_hand(self.main_deck)
        self.dealer.draw_hand(self.main_deck)
        self.dealer.draw_hand(self.main_deck)
        self.dealer.hand = self.dealer.return_hand()
        self.community_cards = self.dealer.hand
        
        self.stage = 'flop'
        self.set_stage()
        self.get_player_actions()
        self.pot += sum(self.bets_placed)
        for i in range(len(self.bets_placed)):
            self.bets_placed[i] = 0
             
        self.minimum_bet_amount = 10
        print('Flop Done')
        pass
    
    #High level implementation of Turn round
    def turn(self):
        self.dealer.draw_hand(self.main_deck)
        self.community_cards = self.dealer.hand
        
        self.stage = 'turn'
        self.set_stage()
        self.get_player_actions()
        self.pot += sum(self.bets_placed)
        for i in range(len(self.bets_placed)):
            self.bets_placed[i] = 0
             
        self.minimum_bet_amount = 10
        print('Turn Done')
        pass
    
    
    #High level implementation of River round.
    def river(self):
        self.dealer.draw_hand(self.main_deck)
        self.community_cards = self.dealer.hand
        
        self.stage = 'river'
        self.set_stage()
        self.get_player_actions()
        self.pot += sum(self.bets_placed)
        for i in range(len(self.bets_placed)):
            self.bets_placed[i] = 0
             
        self.minimum_bet_amount = 10
        pass
    
    
    #The showdown where player hands are displayed.
    def show(self):
        for i in range(self.n_players):
            print(self.player_objects[i].hand)
            
    







        
class Agent(object):
    #Each agent takes in the player object from PokerGame package and the amount of coins he has in the beginning.
    def __init__(self,player_object,coins):
        self.current_coins = coins
        self.player = player_object
        self.hand = None
        self.stage = None
        
        #Not implemented yet.
        self.P_rp=0
        
        #The actions for each player
        self.available_actions = None
    
    #Sets the stage and available actions of the agent. Received from the environment.
    def set_stage(self,stage):
        self.stage = stage
        self.available_actions = action_dictionary[self.stage]
    

    #This is where the agent makes decisions based on the parameters given to it from the environment. Right now random decisions are made.    
    def make_decision(self, bets_placed,player_id,community_cards,minimum_bet_amount):
        print("Bets Placed")
        print(bets_placed,self.current_coins)
        print("Player ID:",player_id, "Controls:",self.available_actions)
        print("Community Cards:",community_cards)
        #a = input("Input for player:")
        #print(self.available_actions)
        a = random.randint(0,len(self.available_actions)-1)
        return int(a),minimum_bet_amount*2
        pass
    
    
    #Not implemented yet, extra information needed for decision making for agents.
    def calculate_probability_of_hand(self,hand):
        self.P_rp = self.P_RoyalFlush(hand)
        
        pass
    
    #Calculate the probability of a royal flush, more flushes to be implemented.
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
#8 Players are created, each are given 1000 coins and a standard poker game is run.
players_list = []
for i in range(8):
    p = Player()
    a = Agent(p,1000)
    players_list.append(a)
    
env = PokerEnvironment(players_list)
env.reset()
env.show()
env.pre_flop()
env.flop()
env.turn()
env.river()
env.show()





