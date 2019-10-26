def score_hand(cards):
    hand = cards[0:2]
    try:
        community = cards[2:]
    except:
        community=None
    if community==None:
            community=[]
    score = 0
    frequence_suit = {"♣":0, "♦":0, "♥":0, "♠":0 }
    cumilative_ranks = ranks.copy()
    suits = [hand[0].split('_')[1],hand[1].split('_')[1]]
    for i in community:
        suits.append(i.split('_')[1])
    for i in suits:
        frequence_suit[i]+=1
    count=0
    for i in frequence_suit.keys():
        if frequence_suit[i]==0:
            count+=1
    if count>=3:
        score += 0.4
        
    suit_score = max(frequence_suit.items(),key=lambda x: x[1])[1]
    score += math.exp(suit_score)/1500

    score += ((len(hand)+len(community))/7)*0.1
    ranking = [hand[0].split('_')[0],hand[1].split('_')[0]]
    for i in community:
        ranking.append(i.split('_')[0])
    rank_score = 0
    df = ranks.copy()
    rank_v = [math.log(df[i])/2.7 for i in ranking]
    mean_rank = np.mean(rank_v)
    distance_metric = [abs(i-mean_rank) for i in rank_v]
    rank_score = sum(distance_metric)
    if rank_score!=0:
        rank_score+=1/rank_score
    else:
        rank_score+=50
    rank_r = [df[i] for i in ranking]
    rank_score += sum(rank_r)
    score+=rank_score/100
    return score/1.5
