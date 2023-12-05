from functools import reduce
import re
import operator

def parseGame(game):
    matches = [re.search('(\d+) (red|green|blue)', draw) for draw in re.split(', ',game)]
    result = {}
    for m in matches:
        [n,colour] = m.groups()
        result[colour] = int(n)
    return result

def parseLine(line):
    [gn, *gs] = re.split(': |; ',line)
    gameNumber = int(re.findall('\d+',gn)[0])
    return (gameNumber, [parseGame(g) for g in gs])

def part1(n,selections):
    rules = {'red':12, 'green':13, 'blue':14}
    return all(rules[k]>=v for s in selections for (k,v) in s.items() )

# input = open('day2/sample1.txt','r')
input = open('day2/input.txt','r')
games = [parseLine(l) for l in input.readlines()]
sum(g[0] for g in filter(lambda g: part1(*g), games))

def findMax(acc,k,v):
    if acc[k]<v: acc[k]=v
    return acc

def part2(n,selections):
    result = reduce(lambda acc,i: findMax(acc,*i), [i for s in selections for i in s.items()], {'blue':1,'red':1,'green':1})
    return reduce(operator.mul, result.values() , 1)    

# input = open('day2/sample1.txt','r')
input = open('day2/input.txt','r')
games = [parseLine(l) for l in input.readlines()]
sum(part2(*g) for g in games)