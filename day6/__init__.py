import re
import operator

# input = open('day6/sample.txt','r')
input = open('day6/input.txt','r')
(times,distances) = [[d for d in re.findall('\d+', l)] for l in input.read().splitlines()]

def winningWays(race):
    (time,distance) = race
    results = {t:t*(time-t) for t in range(0, time+1)}
    return len(list(filter(lambda d: d>distance, results.values())))

# part1
reduce(operator.mul, map(winningWays, zip(map(int,times), map(int,distances))),1)

# part2
winningWays((int(''.join(times)),int(''.join(distances))))