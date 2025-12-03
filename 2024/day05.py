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

def buildDict(rules : list) -> dict:
    rulesDB = {}
    for r in rules:
        k, v = r.split("|")
        if k not in rulesDB.keys():
            rulesDB[k] = [v]
        else:
            rulesDB[k].append(v)
    return rulesDB

def updateIsGood(rulesDB : dict, update : str) -> int:
    pages = update.split(",")
    
    for k in rulesDB.keys():
        if k in pages:
            for p in pages:
                if p == k:
                    break
                if p in rulesDB[k]:
                    return None
    return pages[len(pages)//2]

def getPart1(rulesDB : dict, updates : list, badUpdates : list) -> int:
    sum = 0
    for up in updates:
        mid = updateIsGood(rulesDB, up)
        if mid is not None:
            sum += int(mid)
        else:
            badUpdates.append(up.split(","))
    return sum

def addUpdatetoList(rulesDB : dict, updates : list, entry : str) -> None:
    if entry in rulesDB.keys():
        insert = len(updates)
        for i in range(len(updates)):
            if updates[i] in rulesDB[entry]:
                insert = i
                break
        updates.insert(insert, entry)
    else:
        updates.append(entry)
        
def fixUpdate(rulesDB : dict, update : list) -> list:
    fixed = []
    for u in update:
        addUpdatetoList(rulesDB, fixed, u)
    return fixed

def getPart2(rulesDB : dict, badUpdates : list) -> int:
    sum = 0
    for b in badUpdates:
        fixed = fixUpdate(rulesDB, b)
        sum += int(fixed[len(fixed)//2])     
    return sum

def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n\n")
    answer = [0,0] #part1, part2

    rulesDB = buildDict(input[0].split("\n"))
    updates = input[1].split("\n")
    badUpdates = []
    answer[0] = getPart1(rulesDB, updates, badUpdates)
    answer[1] = getPart2(rulesDB, badUpdates)
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
