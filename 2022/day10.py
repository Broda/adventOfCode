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

def calcPart1(input):
    cost = {'addx':2,'noop':1}

    x = 1
    cycles = 0
    strength = 0

    for l in input:
        cmd = l
        num = 0
        if ' ' in l:
            cmd, num = l.split(' ')
            num = int(num)
        for c in range(cost[cmd]):
            cycles += 1
            if cycles in [20,60,100,140,180,220]:
                strength += cycles * x
        x += num
    return strength

def calcPart2(input):
    s = ''
    crt = ['.' for _ in range(240)]
    cost = {'addx':2,'noop':1}
    
    x = 1
    cycles = 0
    
    for l in input:
        cmd = l
        num = 0
        if ' ' in l:
            cmd, num = l.split(' ')
            num = int(num)
        for c in range(cost[cmd]):
            crtPos = cycles
            cycles += 1

            if crtPos % 40 in [x-1,x,x+1]:
                crt[crtPos] = '#'
        x += num
    
    print('cycles: {}'.format(cycles))

    for r in range(6):
        s += ''.join(crt[r*40:r*40+40]) + '\n'
    
    print(s)
    return s

def getAnswer(input):
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2
    
    answer[0] = calcPart1(input)
    answer[1] = calcPart2(input)

    return answer

while(True):
    ans = getAnswer(menu('day10sample.txt','day10input.txt'))
    print('\nanswer: {}'.format(ans))
