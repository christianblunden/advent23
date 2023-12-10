import re
from collections import Counter

# input = open('day7/sample.txt','r')
input = open('day7/input.txt','r')
games = [l.split(' ') for l in input.read().splitlines()]

def cardScore(card, jValue=11):
    return {'A':14, 'K':13, 'Q':12, 'J':jValue, 'T':10}.get(card) or int(card)

def handScore(hand):
    counts = list(Counter(hand).values())
    counts.sort(reverse=True)
    if counts[0]==5:
        return 7
    if counts[0]==4:
        return 6
    if counts[0]==3 and counts[1]==2:
        return 5
    if counts[0]==3:
        return 4
    if counts[0]==2 and counts[1]==2:
        return 3
    return 2 if counts[0]==2 else 1

def compareHands(hand):
    return [handScore(hand[0])]+[cardScore(c) for c in hand[0]]

# part1
sum([int(g[1])*(i+1) for i,g in enumerate(sorted(games, key=compareHands))])

# part2
def swapJokers(hand):
    if hand=='JJJJJ':
        return hand
    sortedHand = sorted(hand.replace('J',''),key=cardScore)
    counts = Counter(list(sortedHand))
    return hand.replace('J',counts.most_common(1)[0][0])

def compareWithJokers(hand):
    return [handScore(swapJokers(hand[0]))]+[cardScore(c,1) for c in hand[0]]

sum([int(g[1])*(i+1) for i,g in enumerate(sorted(games, key=compareWithJokers))])