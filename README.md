### Poker Environment


The poker game we are building is a traditional texas hold em poker with slightly modified rules. A traditional 52 card deck is used, each player gets 2 cards in his hand and there will be a total of 5 community cards by the end of the game. 

Note: The terms agents and players mean the same, they will used based on the context.

Here is the sequence of events:

1. Hand cards are dealt to each player.
2. Pre-Flop round
3. Flop round
4. Turn round
5. River round
6. Showdown

The player with the best hand+community cards(any 3 of 5 possible) is considered the winner. Each round consists of betting which is added to the 'pot'. The winner gets all the money from the pot. Here is a list of valid hands [citation, wikipedia article of hands].

#### Rounds in Poker

The class PokerEnvironment has methods to control and simulate the rounds of poker and establish and control agents in the environment. It also has methods to render the environment. 


##### 1. Dealing

Each player gets 2 cards from the top of a shuffled deck of 52 cards. Each player is controlled by the 'Agent' class which has methods for making decisions and processing information available. Each agent object is seperate from one another and each agent gets some coins in the beginning of the game(Default:1000).

##### 2. Pre-Flop Round

This is the first betting round before the community cards are shown. Starting from the first player that has entered the game(first in the list), each player has 3 actions available to him, they are: CALL, RAISE, FOLD.

**CALL**: The player has to match the bet of the previous player , if it is the first player, he has to match the minimum bet(Default:10).

**RAISE**: The player can bet a higher amount than the previous player, it can be from double the amount to all-in.
By the end of the round, if all the players dont have the same amount of bets placed, the round is re-run again to make sure they match the highest bet(tracked by minimum_bet variable) or fold.

**FOLD**: A player quits the game, the agent is removed from the environment and any bets he placed will be removed too. The coins it has placed are not given back even if the player folds.

##### 3. Flop Round

3 Community cards are drawn from the deck and placed in front of the agents, the agents use these community cards to make further decisions. Each player has 4 actions available to him: CHECK, BET, RAISE, FOLD.

**CHECK**: Do nothing, the player does not bet and just stays idle. But if some other player has bet, then CHECK is not possible as this player is forced to match their bet.

**BET**: This is similar to CALL from Pre-Flop round. The player bets the minimum_bet or matches the previous player's bet.

**RAISE**: This is the same RAISE as the previous round, the player can bet more than the previous player upto all-in(maximum amount it has).

**FOLD**: The player folds, he quits the game and is removed from the environment. No coins are given back.

The round is re-run again if the player bets are not equal until all player put in the equal amount or fold.

##### 4. Turn Round

1 more community card is drawn from the deck and placed in front of the agents, there are a total of 4 community cards now. Each player has 4 actions available to him: CHECK, BET, RAISE, FOLD.

The actions provided are the same as the ones in the previous round(Flop Round). 

##### 5. River Round

1 more community card is drawn, making it a total of 5 community cards in front of the agents. Each player has 4 actions available: CHECK, BET, RAISE, FOLD.

The actions provided are the same as the ones in the Flop Round.

##### 6. Showdown

Each player's hand is displayed, then they are all classified into flushes based on the legal hands[Wikipedia citation for hands].
The winning player is declared.
The game is done when all rounds are done even if players have coins remaining. This is to ensure simplicity.



















