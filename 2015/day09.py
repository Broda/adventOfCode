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
                ns += ', '
            ns += '->{}:{}'.format(n, self.neighbors[n])
        return '{} => {}'.format(self.name, ns)

class Edge:
    def __init__(self, edge) -> None:
        aSplit = edge.split(' ')
        a = aSplit[0]
        b = aSplit[2]
        c = aSplit[4]
        self.id = a + "->" + b
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
            a, b = e.id.split('->')
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
                edges += ", "
            edges += "{}".format(e)
        
        for n in self.nodes.keys():
            if len(nodes) > 0:
                nodes += ", "
            nodes += "{}".format(self.nodes[n])
        s = "Nodes:\n{}\nEdges:\n{}\n".format(nodes, edges)
        return s

def readFile(path):
    f = open(path, "r")
    return f.read().strip()

def menu():
    main = "\nPlease choose an input option:\n"
    main += "1. Text File\n"
    main += "2. Prompt\n"
    main += "3. Quit\n"
    main += ">> "
    choice = input(main)
    if choice == "3":
        sys.exit(0)
    if choice not in ["1","2"]:
        print("Invalid option. Try Again.\n")
        return menu()
    else:
        if choice == "1":
            return readFile(input("File Name: "))
        else:
            return input("Input: ")

def getAnswer(input):
    answer = [0,0] #part1, part2

    input = input.replace("\r", "").split("\n")
    # input format:
    # PlaceA to PlaceB = 464
    # PlaceA to PlaceC = 518
    # PlaceB to PlaceC = 141

    g = Graph(input)
    print(g)

    return answer

while(True):
    ans = getAnswer(menu())
    print(ans)
