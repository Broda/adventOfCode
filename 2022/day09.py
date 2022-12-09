import sys
import os
import re

def readFile(path):
    if not os.getcwd().endswith('2022'): os.chdir('2022')
    f = open(path, "r")
    return f.read().strip()

def printGrid(g, rev=False):
    if rev:
        for r in reversed(g):
            print(''.join(r))
    else:
        for r in g:
            print(''.join(r))

def addVector(a, b):
    v = []
    for i in range(len(a)):
        v.append(a[i] + b[i])
    return v

def subVector(a, b):
    v = []
    for i in range(len(a)):
        v.append(a[i] - b[i])
    return v

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

def tailTouching(h, t) -> bool:
    return (abs(h[0]-t[0]) <= 1) and (abs(h[1]-t[1]) <= 1)
    
def tryMove(h, t):
    if tailTouching(h, t): return t
    
    hx, hy = h
    tx, ty = t

    if hx == tx:
        for i in [-1,1]:
            t = [tx,ty + i]
            if tailTouching(h, t): return t
    elif hy == ty:
        for i in [-1,1]:
            t = [tx+i,ty]
            if tailTouching(h, t): return t
    else:
        for i in [-1,1]:
            for j in [-1,1]:
                t = [tx+i,ty+j]
                if tailTouching(h, t): return t
        print('No Touch Diag!')
    print('No Touch!')
    print(h, t)

def getAnswer(input):
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2
    
    dirs = {'L':[-1,0],'R':[1,0],'U':[0,1],'D':[0,-1]}
    s = [0,0]
    Ropes = []
    for i in range(10):
        Ropes.append(s)
    
    v1 = {}
    v1[tuple(Ropes[1])] = 1
    v2 = {}
    v2[tuple(Ropes[-1])] = 1

    for l in input:
        dir, num = l.split(' ')
        dir = dirs[dir]
        num = int(num)

        while num > 0:
            num -= 1
            Ropes[0] = addVector(Ropes[0], dir)
            
            for i in range(1, len(Ropes)):
                Ropes[i] = tryMove(Ropes[i-1], Ropes[i])

            v1[tuple(Ropes[1])] = 1
            v2[tuple(Ropes[-1])] = 1
            
    answer[0] = len(v1.keys())
    answer[1] = len(v2.keys())

    return answer

while(True):
    ans = getAnswer(menu('day09sample.txt','day09input.txt'))
    print('\nanswer: {}'.format(ans))
