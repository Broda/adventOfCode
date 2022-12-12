import sys
import os
import re
from copy import deepcopy

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


def readFile(path):
    if not os.getcwd().endswith('2015'): os.chdir('2015')
    f = open(path, "r")
    return f.read().strip()

def menu(samplePath, inputPath):
    main = "\nPlease choose an input option:\n"
    main += "1. Sample File\n"
    main += "2. Input File\n"
    main += "3. Other File\n"
    main += "4. Prompt\n"
    main += "5. Quit\n"
    main += ">> "
    
    match input(main):
        case "5":
            sys.exit(0)
        case "1":
            return readFile(samplePath)
        case "2":
            return readFile(inputPath)
        case "3":
            return readFile(input("File Name: "))
        case "4":
            return input("Input: ")
        case _:
            print("Invalid option. Try Again.\n")
            return menu()

def findPath(g, n1, n2):
    p = [n1]

    for n in g.nodes[n1].neighbors.keys():
        if n == n2:
            p.append(n2)
            return p
    
    neighbors = list(g.nodes[n1].neighbors.keys())
    for n in g.nodes[n1].neighbors.keys():
        if n not in p:
            p = findPath(g, n, n2)
        
    

def getAnswer(input):
    answer = [0,0] #part1, part2

    input = input.replace("\r", "").split("\n")
    # input format:
    # PlaceA to PlaceB = 464
    # PlaceA to PlaceC = 518
    # PlaceB to PlaceC = 141

    g = Graph(input)
    print(g)
    print()
    keys = list(g.nodes.keys())
    p, pCost = findPath(g, keys[0], keys[1])
    print(p, pCost)

    return answer

while(True):
    ans = getAnswer(menu('day09sample.txt','day09input.txt'))
    print('\nanswer: {}'.format(ans))
