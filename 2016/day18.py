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

def isTrap(row : str, index : int) -> bool:
    chkStr = ""
    if index == 0: 
        chkStr = "." + row[index:index+2]
    elif index == len(row)-1: 
        chkStr = row[len(row)-2:] + "."
    else:
        chkStr = row[index-1:index+2]
    
    if chkStr[0] == "^" and chkStr[1] == "^" and chkStr[2] == ".": return True
    if chkStr[0] == "." and chkStr[1] == "^" and chkStr[2] == "^": return True
    if chkStr[0] == "^" and chkStr[1] == "." and chkStr[2] == ".": return True
    if chkStr[0] == "." and chkStr[1] == "." and chkStr[2] == "^": return True
    return False

def getPart1(input : str, numRows : int) -> int:
    numRows -= 1
    safeCount = input.count(".")
    currRow = input
    
    for _ in range(numRows):
        nextRow = ""
        for i in range(len(currRow)):
            if isTrap(currRow, i):
                nextRow += "^"
            else:
                nextRow += "."
        safeCount += nextRow.count(".")
        currRow = nextRow
        
    return safeCount

def getPart2(input :str, numRows : int) -> int:
    return getPart1(input, numRows)

def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n")[0]
    answer = [0,0] #part1, part2

    numRows = 40
    if isSample:
        numRows = 3

    answer[0] = getPart1(input, numRows)
    answer[1] = getPart2(input, 400000)
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
