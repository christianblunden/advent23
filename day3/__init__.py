import re
from collections import defaultdict
import operator
from functools import reduce

# input = open('day3/sample1.txt','r')
input = open('day3/input.txt','r')
grid = [list(ln) for ln in input.read().splitlines()]

rows = len(grid)
cols = len(grid[0])
neighbours = list(filter(lambda p: p!=(0,0), [(x,y) for x in range(-1,2) for y in range(-1,2)]))

def inBounds(row,col):
    return row>=0 and row<rows and col>=0 and col<cols

def getNeighbours(row,col):
    return list(filter(lambda n: inBounds(*n), [(row+x,col+y) for (x,y) in neighbours]))

def adjacentSymbol(ns):
    return any([re.match('[^0-9.]',grid[x][y]) for (x,y) in set(ns)])

def part1():
    validNumbers = []

    for row in range(0,rows):
        buffer = []
        localNeighbours = []
        for col in range(0,cols):
            current = grid[row][col]
            if current.isnumeric():
                buffer.append(current)
                localNeighbours += getNeighbours(row,col)
            
            if col==(cols-1) or not current.isnumeric():
                if len(buffer)>0 and adjacentSymbol(localNeighbours):
                    validNumbers.append(int("".join(buffer)))
                buffer = []
                localNeighbours = []

    return sum(validNumbers)

part1()

def gears(ns):
    return list(filter(lambda n: grid[n[0]][n[1]]=='*', set(ns)))

def part2():
    numbers = []

    for row in range(0,rows):
        buffer = []
        localNeighbours = []
        for col in range(0,cols):
            current = grid[row][col]
            if current.isnumeric():
                buffer.append(current)
                localNeighbours += getNeighbours(row,col)
            
            if col==(cols-1) or not current.isnumeric():
                if len(buffer)>0:
                    numbers.append((int("".join(buffer)), gears(localNeighbours)))
                buffer = []
                localNeighbours = []

    ratios = defaultdict(list)
    for (n,gs) in numbers:
        for g in gs:
            ratios[g].append(n)
    return sum([reduce(operator.mul,f,1) for f in filter(lambda i: len(i)==2, ratios.values())])

part2()

