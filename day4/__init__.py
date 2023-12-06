import re
from collections import defaultdict

def parseGame(line):
    [_, *ns] = re.split(': | \| ', line)
    return [set(re.findall('\d+', n)) for n in ns]

# input = open('day4/sample1.txt','r')
input = open('day4/input.txt','r')

def part1():
    games = [parseGame(l) for l in input.readlines()]
    results = [len(winners.intersection(hand)) for (winners, hand) in games]
    return sum(2**(r-1) if r>2 else r for r in results)

part1()

def parseGame2(line):
    [card, *ns] = re.split(': | \| ', line)
    cardNumber = int(re.findall('\d+',card)[0])
    return (cardNumber, [set(re.findall('\d+', n)) for n in ns])

# input = open('day4/sample1.txt','r')
input = open('day4/input.txt','r')

def part2():
    games = [parseGame2(l) for l in input.readlines()]
    results = {n:len(winners.intersection(hand)) for (n, (winners, hand)) in games}
    numberOfGames = len(results)
    scratchies = defaultdict(int)
    for (game,wins) in results.items():
        scratchies[game]+=1
        for n in range(1,wins+1):
            if game+n <= numberOfGames:
                scratchies[game+n]+=scratchies[game]
    return sum(scratchies.values())

part2()