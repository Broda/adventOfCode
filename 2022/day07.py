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

class Directory:
    def __init__(self, name, parent = None) -> None:
        self.name = name
        self.parent = parent
        self.directories = {}
        self.files = {}
    
    def buildPath(self):
        path = self.name
        p = self.parent
        while p != None:
            path = '{}/{}'.format(p.buildPath(), path)
            p = p.parent
        return path
    
    def getSize(self):
        size = 0
        for f in self.files.keys():
            size += int(self.files[f])
        for d in self.directories.keys():
            size += self.directories[d].getSize()
        return size

    def __str__(self) -> str:
        s = '{}\n\tSize: {}'.format(self.buildPath(), self.getSize())
        return s


def buildFileSystem(lines):
    root = Directory("/")
    cd = root

    # build filesystem
    for i in range(1,len(lines)):
        line = lines[i]
        parts = line.split(" ")
        if parts[0] == "$":
            if parts[1] == "cd":
                if parts[2] == "..":
                    if cd.parent is not None: cd = cd.parent
                else:
                    if parts[2] in cd.directories.keys():
                        cd = cd.directories[parts[2]]
        elif parts[0] == "dir":
            cd.directories[parts[1]] = Directory(parts[1], cd)
        else:
            cd.files[parts[1]] = parts[0]
    return root

def getDirectories(dict, curr):
    dict[curr.buildPath()] = curr
    for d in curr.directories.keys():
        dict = getDirectories(dict, curr.directories[d])
    return dict

def getAnswer(input):
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2
    root = buildFileSystem(input)
    #print(root)
    directories = getDirectories({}, root)
    
    total = 70000000
    required = 30000000
    avail = total - root.getSize()
    needed = required - avail
    print('avail: {}, needed: {}'.format(avail, needed))
    curr = None

    for d in directories.keys():
        s = directories[d].getSize()
        if s <= 100000:
            answer[0] += s
        if s >= needed:
            if curr is None:
                curr = directories[d]
                answer[1] = s
            elif s < curr.getSize():
                curr = directories[d]
                answer[1] = s
    
    return answer

while(True):
    ans = getAnswer(menu())
    print(ans)
