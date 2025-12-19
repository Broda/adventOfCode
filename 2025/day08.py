from ..Libraries.AdventOfCode import menu
import math

# returns index of containing circuit, or -1
def getContainingCircuit(circuits : list, node : tuple) -> int:
    for cIndex in range(len(circuits)):
        if node in circuits[cIndex]: return cIndex
    
    return -1

def addNodesToCircuit(circuits : list, nodes : tuple):
    n1, n2 = nodes
    n1c = getContainingCircuit(circuits, n1)
    n2c = getContainingCircuit(circuits, n2)
    if n1c == -1 and n2c == -1:
        circuits.append([n1, n2])
    elif n1c >= 0 and n2c >= 0 and n1c != n2c:
        circuits[n1c] = list(set(circuits[n1c] + circuits[n2c]))
        circuits.pop(n2c)
    elif n1c >= 0 and n2c == -1:
        circuits[n1c].append(n2)
    elif n1c == -1 and n2c >= 0:
        circuits[n2c].append(n1)
    else:
        pass # n1c == n2c so nodes already in same circuit, do nothing

def getPart1(nodes : list, numConnections : int) -> int:
    circuits = []
    connections = {}
    for n1 in nodes:
        for n2 in nodes:
            if n1 == n2: continue
            if (n2, n1) in connections.keys(): continue
            connections[(n1, n2)] = math.dist(n1, n2)
    connections = dict(sorted(connections.items(), key=lambda item: item[1]))
    keys = list(connections.keys())
    for i in range(numConnections):
        addNodesToCircuit(circuits, keys[i])
    
    circuits.sort(key=len)
    
    return len(circuits[-1]) * len(circuits[-2]) * len(circuits[-3])

def getPart2(nodes : list) -> int:
    circuits = []
    connections = {}
    for n1 in nodes:
        circuits.append([n1]) # create a circuit for each individual node first
        for n2 in nodes:
            if n1 == n2: continue
            if (n2, n1) in connections.keys(): continue
            connections[(n1, n2)] = math.dist(n1, n2)
    connections = dict(sorted(connections.items(), key=lambda item: item[1]))
    keys = list(connections.keys())

    currConnIndex = 0
    while len(circuits) > 1:
        addNodesToCircuit(circuits, keys[currConnIndex])
        if len(circuits) == 1:
            break
        currConnIndex += 1
    n1, n2 = keys[currConnIndex]
    return n1[0] * n2[0]

def getNodes(lines : list) -> list:
    return [tuple(map(int, l.split(','))) for l in lines]
    
def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2

    nodes = getNodes(input)
    numConnections = 10 if isSample else 1000
    answer[0] = getPart1(nodes, numConnections)
    answer[1] = getPart2(nodes)
    return answer

while(True):
    ans = getAnswer(*menu("\\2025\\day08.py"))
    print('\nanswer: {}'.format(ans))
