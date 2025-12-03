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
    if not os.getcwd().endswith('2016'): os.chdir('2016')
    f = open(path, "r")
    return f.read().strip()

def writeFile(path, s):
    if not os.getcwd().endswith('2016'): os.chdir('2016')
    f = open(path, 'w')
    f.write(s)
    f.close()

def printPad(pad : list) -> None:
    padStr = ""
    for r in range(len(pad)):
        row = ""
        for c in range(len(pad[0])):
            row += pad[r][c]
        padStr += row + "\n"
    print(padStr)

def getPart1(input : list, size : tuple) -> int:
    pad = [["." for _ in range(size[0])] for _ in range(size[1])]
    printPad(pad)
    inst : str
    for inst in input:
        if inst.startswith("rect"):
            cols, rows = [int(v) for v in inst.split(" ")[1].split("x")]
            for r in range(rows):
                for c in range(cols):
                    pad[r][c] = "#"
            print(inst)
            printPad(pad)
            continue
        
        loc, amt = [int(v) for v in inst.split("=")[1].split(" by ")]
        if "column" in inst:
            for _ in range(amt):
                bottom = pad[size[1]-1][loc]
                for r in range(size[1]-2, -1, -1):
                    pad[r+1][loc] = pad[r][loc]
                pad[0][loc] = bottom
            print(inst)
            printPad(pad)
            continue
        if "row" in inst:
            for _ in range(amt):
                right = pad[loc][size[0]-1]
                for c in range(size[0]-2, -1, -1):
                    pad[loc][c+1] = pad[loc][c]
                pad[loc][0] = right
            print(inst)
            printPad(pad)
            continue
        
    on = 0
    for r in range(size[1]):
        for c in range(size[0]):
            if pad[r][c] == "#":
                on += 1
    return on

def getPart2(input : list, size : tuple) -> int:
    return 0

def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2

    size = (50, 6)
    if isSample:
        size = (7,3)
    answer[0] = getPart1(input, size)
    answer[1] = getPart2(input, size)
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
