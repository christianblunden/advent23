import re
from itertools import cycle
from math import lcm

input = open('day8/sample2.txt','r')
input = open('day8/input.txt','r')

cmds,_,*nodes = input.read().splitlines()
graph = {n:{'L':l,'R':r} for n,l,r in [re.findall('[12A-Z]{3}', n) for n in nodes]}

def traverseGraph(startNode,endFn):
    currentNode = startNode
    steps = 0
    for cmd in cycle(cmds):
        node = graph[currentNode]
        if (currentNode == node['L'] and currentNode == node['R']) or endFn(currentNode):
            break
        steps += 1
        currentNode = node[cmd]
    return steps

# part1
traverseGraph('AAA', lambda n:n=='ZZZ')

def part2():
    startNodes = list(filter(lambda k:k[2]=='A', graph.keys()))
    steps = [traverseGraph(sn,lambda n:n[2]=='Z') for sn in startNodes]
    return lcm(*steps)

part2()