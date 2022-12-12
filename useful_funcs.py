import heapq

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

print(dijkstra(graph, 0, 3))
print(dijkstra(graph, 0, 2))
print(dijkstra(graph, 0, 1))

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
