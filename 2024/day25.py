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
    if not os.getcwd().endswith('2024'): os.chdir('2024')
    f = open(path, "r")
    return f.read().strip()

def writeFile(path, s):
    if not os.getcwd().endswith('2024'): os.chdir('2024')
    f = open(path, 'w')
    f.write(s)
    f.close()

def printData(d : list) -> None:
    for line in d:
        print(line)
    print("\n")
    
def parseInput(input : list) -> list:
    locks = []
    keys = []
    maxPin = 0
    for i in range(len(input)):
        data : list
        data = input[i].split("\n")
        maxPin = len(data)-1
        isLock = data[0] == "#" * len(data[0])
        item = []
        if isLock:
            data.pop(0)
        else:
            data.pop()
        for c in range(len(data[0])):
            num = 0
            for r in range(len(data)):
                if isLock:
                    if data[r][c] == ".":
                        num = r
                        break
                else:
                    if data[r][c] == "#":
                        num = len(data)-r
                        break
                    
            item.append(num)
        if isLock:
            locks.append(item)
        else:
            keys.append(item)
                
    return [locks, keys, maxPin]
            

def getPart1(locks : list, keys : list, maxPin : int) -> int:
    num = 0
    
    for lock in locks:
        for key in keys:
            fits = True
            for i in range(len(lock)):
                if lock[i] + key[i] >= maxPin:
                    fits = False
                    break
            if fits:
                num += 1
                
    return num

def getPart2() -> int:
    return 0

def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n\n")
    answer = [0,0] #part1, part2

    locks, keys, maxPin = parseInput(input)
        
    answer[0] = getPart1(locks, keys, maxPin)
    answer[1] = getPart2()
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
