import sys
import os
import re

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

class Node:
    def __init__(self, name) -> None:
        self.name = name
        self.neighbors = {}

    def __str__(self) -> str:
        return self.name
    
class Edge:
    def __init__(self, startNodeName, endNodeName, cost) -> None:
        self.id = '{}->{}'.format(startNodeName, endNodeName)
        self.startNodeName = startNodeName
        self.endNodeName = endNodeName
        self.cost = cost
    
    def __str__(self) -> str:
        return self.id + ': {}'.format(self.cost)

class Graph:
    def __init__(self, dataArray) -> None:
        self.dataArray = dataArray
        self.nodes = {}
        self.edges = {}

    def getNodesString(self):
        s = ''
        for n in self.nodes:
            if len(s) > 0: s += ', '
            s += str(n)
        return s

    def getEdgesString(self):
        s = ''
        for e in self.edges:
            if len(s) > 0: s += ', '
            s += str(e)
        return s

    def __str__(self) -> str:
        return ''

def getAnswer(input):
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2
    for l in input:
        answer[0] += 0
        answer[1] += 0
    return answer

while(True):
    ans = getAnswer(menu())
    print(ans)
