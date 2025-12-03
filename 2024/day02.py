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

def reportIsSafe(report) -> bool:
    inc = False
    dec = False
    levels = report.split()
    for i in range(len(levels)-1):
        amt = int(levels[i]) - int(levels[i+1])
        if amt == 0:
            return False
        
        if i == 0:
            inc = amt < 0
            dec = not inc
        else:
            if inc and amt > 0:
                return False
            if dec and amt < 0:
                return False
        if abs(amt) > 3:
            return False
            
    return True


def reportIsSafeWithDampener(report: list) -> bool:
    if reportIsSafe(report):
        return True
    
    levels: list = report.split()
    for i in range(len(levels)):
        val = levels.pop(i)
        if reportIsSafe(' '.join(levels)):
            return True
        levels.insert(i, val)
    return False

def getPart1(reports) -> int:
    safeCount = 0
    for report in reports:
        if reportIsSafe(report):
            safeCount += 1

    return safeCount

def getPart2(reports) -> int:
    safeCount = 0
    for report in reports:
        if reportIsSafeWithDampener(report):
            safeCount += 1

    return safeCount

def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2


    answer[0] = getPart1(input)
    answer[1] = getPart2(input)
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))


