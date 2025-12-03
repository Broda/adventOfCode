import sys
import heapq
import collections

def dijkstra(graph, start_node, end_node):
    best = [float('+Inf')] * len(graph)
    
    heap = []
    heapq.heappush(heap, (0, start_node, [start_node]))
    while len(heap):
        distance, node, path = heapq.heappop(heap)
        if distance >= best[node]: continue
        if node == end_node: 
            return distance, path
        best[node] = distance

        for neighbor, cost in graph[node]:
            if distance + cost >= best[neighbor]: continue
            heapq.heappush(heap, (distance+cost, neighbor, path + [neighbor]))

graph = [
    [(1, 5), (2, 15), (3, 16)],
    [(2, 13), (3, 1)],
    [(3, 1)],
    [(2, 1)],
]

# print(dijkstra(graph, 0, 3))
# print(dijkstra(graph, 0, 2))
# print(dijkstra(graph, 0, 1))

def floid_warshall(valves):
    dist = {v: {u: sys.maxsize for u in valves} for v in valves}
 
    for v in valves:
        dist[v][v] = 0
        for u in valves[v].children:
            dist[v][u] = 1
 
    for k in valves:
        for i in valves:
            for j in valves:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
 
    return dist

visitedList = [[]]

def depthFirst(graph, currNode, visited):
    visited.append(currNode)
    for node in graph[currNode]:
        if node not in visited:
            depthFirst(graph, node, visited.copy())
    visitedList.append(visited)

depthFirst(graph, 0, [])
print(visitedList)

def bfs(grid, *start):
    
    q = collections.deque((row, col, 0, 'a') for row in range(len(grid))
        for col in range(len(grid[0]))
        if grid[row][col] in start)

    visited = set((row, col) for row, col, count, char in q)

    def push(row, col, count, curr):
        if not (0 <= row < len(grid)) or not (0 <= col < len(grid[0])): return
        if (row, col) in visited: return

        next = grid[row][col].replace('E', 'z') # replace E if we're checking the end
        if ord(next) > ord(curr) + 1: return
        
        visited.add((row, col))
        q.append((row, col, count + 1, next))

    while len(q):
        row, col, count, char = q.popleft()
        if grid[row][col] == 'E': return count
        
        push(row + 1, col, count, char)
        push(row - 1, col, count, char)
        push(row, col + 1, count, char)
        push(row, col - 1, count, char)

def prim():
    print('=== Prim ===')
    grid = [[ 0, 19,  5,  0,  0],
            [19,  0,  5,  9,  2],
            [ 5,  5,  0,  1,  6],
            [ 0,  9,  1,  0,  1],
            [ 0,  2,  6,  1,  0]]
    for r in grid:
        print(r)

    N = len(grid)

    sel_node = [False]*N
    no_edge = 0
    sel_node[0] = True

    print('Edge : Weight')
    while no_edge < N - 1:
        minimum = sys.maxsize
        a = 0
        b = 0
        for m in range(N):
            if sel_node[m]:
                for n in range(N):
                    if not sel_node[n] and grid[m][n]:
                        # not in sel and there is an edge
                        if minimum > grid[m][n]:
                            minimum = grid[m][n]
                            a = m
                            b = n
        print('{}-{}:{}'.format(a, b, grid[a][b]))
        sel_node[b] = True
        no_edge += 1

prim()

def calcManhatten(grid, end):
    m = []
    for r in range(len(grid)):
        row = []
        for c in range(len(grid[0])):
            row.append(abs(end[0] - r) + abs(end[1] - c))
        m.append(row)
    return m

def findCell(grid, letter):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == letter: return [r,c]
    return None

def printGrid(g, rev=False):
    if rev:
        for r in reversed(g):
            print(''.join(r))
    else:
        for r in g:
            print(''.join(str(r)))

class Node:
    def __init__(self, name) -> None:
        self.name = name
        self.visited = False
        self.neighbors = {}
    
    def __str__(self):
        ns = ''
        for n in self.neighbors.keys():
            if len(ns) > 0:
                ns += '\n\t\t-> '
            ns += '{}:{}'.format(n, self.neighbors[n])
        return '{}\t-> {}'.format(self.name, ns)

class Edge:
    def __init__(self, edge) -> None:
        aSplit = edge.split(' ')
        a = aSplit[0]
        b = aSplit[2]
        c = aSplit[4]
        self.id = a + "<->" + b
        self.cost = int(c)
    
    def __str__(self):
        return "{}: {}".format(self.id,self.cost)

class Graph:
    def __init__(self, edges) -> None:
        self.nodes = {}
        self.edges = []
        for e in edges:
            self.edges.append(Edge(e))
        for e in self.edges:
            a, b = e.id.split('<->')
            if a not in self.nodes.keys():
                self.nodes[a] = Node(a)
            if b not in self.nodes.keys():
                self.nodes[b] = Node(b)
            self.nodes[a].neighbors[b] = e.cost
            self.nodes[b].neighbors[a] = e.cost
        
    def __str__(self):
        nodes = ''
        edges = ''
        for e in self.edges:
            if len(edges) > 0:
                edges += "\n"
            edges += "\t{}".format(e)
        
        for n in self.nodes.keys():
            if len(nodes) > 0:
                nodes += "\n"
            nodes += "\t{}".format(self.nodes[n])
        s = "Nodes:\n{}\nEdges:\n{}\n".format(nodes, edges)
        return s
