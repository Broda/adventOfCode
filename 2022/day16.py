import os
import sys

def menu():
    main = "\nPlease choose an input option:\n"
    main += "1. Sample File\n"
    main += "2. Input File\n"
    main += "3. Other File\n"
    main += "4. Prompt\n"
    main += "5. Quit\n"
    main += ">> "
    
    filename = os.path.basename(__file__)
    samplePath = filename.replace('.py', 'sample.txt')
    inputPath = filename.replace('.py', 'input.txt')
    
    match input(main):
        case "5":
            sys.exit(0)
        case "1":
            isSample = True
            return readFile(samplePath), True
        case "2":
            return readFile(inputPath), False
        case "3":
            return readFile(input("File Name: ")), False
        case "4":
            return input("Input: "), False
        case _:
            print("Invalid option. Try Again.\n")
            return menu()

def readFile(path):
    if not os.getcwd().endswith('2022'): os.chdir('2022')
    f = open(path, "r")
    return f.read().strip()

class Node:
    def __init__(self, data) -> None:
        self.data = data
        _, self.name, _, _, rate, _, _, _, _, *self.valves = data.split()
        self.rate = int(rate.split('=')[1][:-1])
        for v in range(len(self.valves)):
            self.valves[v] = self.valves[v].replace(',','')

    def __str__(self) -> str:
        return 'Node {}, Rate = {}, Connected Valves: {}'.format(self.name, self.rate, self.valves)

def buildGraph(input):
    g = {}
    for l in input:
        n = Node(l)
        g[n.name] = n

    return g

# visitedList = [[]]

# def depthFirst(graph, currNode, visited):
#     visited.append(currNode)
#     for node in graph[currNode].valves:
#         if node not in visited:
#             depthFirst(graph, node, visited.copy())
#     visitedList.append(visited)


def floid_warshall(graph):
    dist = {v: {u: sys.maxsize for u in graph.keys()} for v in graph.keys()}
 
    keys = graph.keys()
    for v in keys:
        dist[v][v] = 0
        for u in graph[v].valves:
            dist[v][u] = 1
 
    for k in keys:
        for i in keys:
            for j in keys:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
 
    return dist


def getAnswer(input, isSample):
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2

    g = buildGraph(input)
    # depthFirst(g, 'AA', [])
    #print(visitedList)
    dist = floid_warshall(g)
    print(dist)
    

    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
