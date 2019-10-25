# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 21:37:28 2019

@author: battu
"""


# The code for implementing the Cards, decks and flushes.
from PokerGame import *
import numpy as np
# from PokerScore import *
# Defined Player Attributes that help in decision making
#Each score ranges from 0-100
default_attributes = {'caution':50,'greed':50,'bluff':50}

#List of actions available to players each round
action_dictionary = {'pre_flop':['CALL','RAISE','FOLD'],'flop':['CHECK','BET','RAISE','FOLD'],'turn':['CHECK','BET','RAISE','FOLD'],'river':['CHECK','BET','RAISE','FOLD']}

emotion_dictionary = {0:'fear',1:'happy',2:'no-emotion',3:'anger',4:'contempt',5:'normal'}
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
        self.player_emotions = []
        
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
            print("The player has:",action_str)
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
            
            if len(self.bets_placed) > 0 and (sum(self.bets_placed)/self.n_players) == self.bets_placed[0]:
                break
                    
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
    def __init__(self,player_object,coins,emotion,power):
        self.current_coins = coins
        self.player = player_object
        self.hand = None
        self.stage = None
        
        #Not implemented yet.
        self.P_rp=0
        
        #The actions for each player
        self.available_actions = None
        self.emotion_power = power
        
        self.emotion = emotion
        self.player_attributes = default_attributes.copy()
        self.set_attributes()
    #Sets the stage and available actions of the agent. Received from the environment.
    def set_stage(self,stage):
        self.stage = stage
        self.available_actions = action_dictionary[self.stage]
    
    #Here the attributes of each player are set based on their state of emotion.
    def set_attributes(self):
        base_value = 50
        if emotion_dictionary[self.emotion] == 'fear':
                    self.player_attributes['caution'] += self.emotion_power*base_value
                    self.player_attributes['greed'] -= self.emotion_power*(base_value/2)            
        if emotion_dictionary[self.emotion] == 'happy':
                    self.player_attributes['bluff'] += self.emotion_power*base_value
                    self.player_attributes['greed'] += self.emotion_power*(base_value/2)
                    self.player_attributes['caution'] -= self.emotion_power*(base_value/2)
        if emotion_dictionary[self.emotion] == 'no_emotion':
                    self.player_attributes['caution'] = 0
                    self.player_attributes['greed'] = 0
                    self.player_attributes['bluff'] = 0
        if emotion_dictionary[self.emotion] == 'anger':
                    self.player_attributes['greed'] += self.emotion_power*base_value
                    self.player_attributes['bluff'] += self.emotion_power*(base_value/2)
                    self.player_attributes['caution'] -= self.emotion_power*base_value
        if emotion_dictionary[self.emotion] == 'contempt':
                    self.player_attributes['greed'] -= self.emotion_power*base_value
                    self.player_attributes['caution'] += self.emotion_power*(base_value/2)
        
        
        
        
    #This is where the agent makes decisions based on the parameters given to it from the environment. Right now random decisions are made.    
    def make_decision(self, bets_placed,player_id,community_cards,minimum_bet_amount):
        print("All the bets placed:")
        print(bets_placed)
        
        print("Player ",player_id," Turn")
        print("Controls Available:",self.available_actions)
        print("Community Cards:",community_cards)
        print("Player Attributes:",self.player_attributes)
        score = float(input("HandScore:"))
        #score = self.calculate_score_of_hand(self.hand,community_cards)
        #score = score/50 #Here 50 is the max score possible.
        print("Player Score:",score)
        # Probablistic agent starts here
        probabilities_actions = {}
        
        for i in range(len(self.available_actions)):
                probabilities_actions[i] = 0
        
        
        # Effect of bets on attributes
        
        
        try:
           previous_bet = bets_placed[player_id]
        except:
            previous_bet = minimum_bet_amount
        mean_bet = np.mean(bets_placed)        
        
        caution_effect = 0
        greed_effect = 0
        bluff_effect = 0
        
        if minimum_bet_amount>previous_bet:
            caution_effect += 1
            greed_effect -= 1
        else:
            caution_effect -= 1
            greed_effect +=1
            bluff_effect += 1
        if mean_bet > previous_bet:
            caution_effect += 2
            greed_effect -= 1
            
        else:
            caution_effect -= 2
            greed_effect += 1
            bluff_effect += 1


        
        self.player_attributes['caution'] += caution_effect
        self.player_attributes['greed'] += greed_effect
        self.player_attributes['bluff'] += bluff_effect
        
        
        
        
        if self.stage == 'pre_flop':
            
            #Initialize probabilities based on attributes
            probabilities_actions[0] += self.player_attributes['caution']*(score/1.5)  + self.player_attributes['greed']*(score/3) + self.player_attributes['bluff']*(score/3)
            
            probabilities_actions[1] += -self.player_attributes['caution']*((1-score)/2) + self.player_attributes['greed']*(score/(1.2)) + self.player_attributes['bluff']*score
            
            probabilities_actions[2] += self.player_attributes['caution']*(1-score)/2
            
            
            
        else:
            
            probabilities_actions[0] += self.player_attributes['caution']*(score) + self.player_attributes['bluff']*(score)
            
            
            probabilities_actions[1] += self.player_attributes['caution']*(score/1.5)  + self.player_attributes['greed']*(score/3) + self.player_attributes['bluff']*(score/3)
            
            probabilities_actions[2] += -self.player_attributes['caution']*((1-score)/2) + self.player_attributes['greed']*(score/(1.2)) + self.player_attributes['bluff']*score
            
            probabilities_actions[3] += self.player_attributes['caution']*(1-score)/2
            
        
            
        
        
        
        
        
        
        
        print(probabilities_actions)
        prob_array = [x[1] for x in probabilities_actions.items()]
        #Each agent makes a random decision.
        a = np.argmax(prob_array)
        print(a)
        return int(a),minimum_bet_amount*2
        pass
    
    
    #Not implemented yet, extra information needed for decision making for agents.
    #Returns the score of hand+community card to aid in decision making
    
    def calculate_score_of_hand(self,hand,community=None):
        if community==None:
            community=[]
        
        
        # return Pscore(self.stage,hand,community)
        #For now hand scores are random.
        self.rp = 1 * random.randint(0,5)
        self.sf = 0.9 * random.randint(0,5)
        self.fo = 0.8 * random.randint(0,5)
        self.fh = 0.7 * random.randint(0,5)
        self.f = 0.6 * random.randint(0,5)
        self.s = 0.5 * random.randint(0,5)
        self.tk = 0.4 * random.randint(0,5)
        self.tp = 0.3 *random.randint(0,5)
        self.op = 0.2 * random.randint(0,5)
        self.hc = 0.1 * random.randint(0,5)
        
        return self.rp+self.sf+self.fo+self.fh+self.f+self.s+self.tk+self.tp+self.op+self.hc
        
        pass
    
            
        
    
    
    
    
    
    

        
        
### Testing Area     
#8 Players are created, each are given 1000 coins and a standard poker game is run.
print("Welcome to Emotional Poker!")

players_list = []
for i in range(8):
    p = Player()
    emotion = int(input("Emotion:"))
    power = float(input("Power:"))
    a = Agent(p,1000,emotion,power)
    players_list.append(a)

count=0
print("Here is a list of Players, along with their emotions and the power of their emotions")
for i in players_list:
    print("Player ID:",count,", Emotion:",emotion_dictionary[i.emotion],", Emotion Power:",i.emotion_power)
    count+=1
env = PokerEnvironment(players_list)
env.reset()

env.show()

env.pre_flop()

env.flop()
env.turn()
env.river()
env.show()





