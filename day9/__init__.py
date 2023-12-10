import re
from itertools import pairwise

# input = open('day9/sample.txt','r')
input = open('day9/input.txt','r')
samples = [[int(d) for d in s.split(" ")] for s in input.read().splitlines()]

def buildTree(sample):
    if all(c==0 for c in sample):
        return 0;
    diffs = [b - a for a, b in pairwise(sample)]
    result = buildTree(diffs)
    return sample[-1] + result

# part1
sum([buildTree(s) for s in samples])

# part2 - reverse the samples
sum([buildTree(s[::-1]) for s in samples])