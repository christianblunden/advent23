from operator import add

# input = open('day10/sample.txt','r')
input = open('day10/input.txt','r')
grid = [[c for c in s] for s in input.read().splitlines()]
north = [-1,0]
south = [1,0]
east = [0,1]
west = [0,-1]

rows = len(grid)
cols = len(grid[0])

def connectedNeighbours(point,pipe):
    connectors = {'.':[], '|':[north,south], '-':[east,west], 'L':[north,east], 'J':[north,west], '7':[south,west], 'F':[south,east]}
    connectedNeighbours = [(point[0]+y,point[1]+x) for y,x in connectors[pipe]]
    return list(filter(lambda p:p[0]>=0 and p[0]<rows and p[1]>=0 and p[1]<cols, connectedNeighbours))

def startNeighbours(start, graph):
    neighbours = [(start[0]+x,start[1]+y) for x,y in [north,south,east,west]]
    return list(filter(lambda n:any(x==start for x in graph.get(n,[])), neighbours))

def buildGraph():
    graph={}
    start=(0,0)
    for y,row in enumerate(grid):
        for x,pipe in enumerate(row):
            if pipe=='S':
                start=(y,x)
                continue
            graph[(y,x)] = connectedNeighbours((y,x),pipe)
    graph[start] = startNeighbours(start, graph)
    return (start, graph)

def dijkstra(start,graph):
    unvisited = {node: None for node in graph.keys()} #using None as +inf
    visited = {}
    current = start
    currentDistance = 0
    unvisited[current] = currentDistance

    while True:
        for neighbour in graph[current]:
            if neighbour not in unvisited: continue
            newDistance = currentDistance + 1
            if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
                unvisited[neighbour] = newDistance
        visited[current] = currentDistance
        del unvisited[current]
        if not unvisited: break
        candidates = [node for node in unvisited.items() if node[1]]
        if not candidates: break
        current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]
    return visited

start,graph = buildGraph()
dijkstra(start,graph)

