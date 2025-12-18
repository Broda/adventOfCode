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
    if not os.getcwd().endswith('2025'): os.chdir('2025')
    f = open(path, "r")
    return f.read().strip()

def writeFile(path, s):
    if not os.getcwd().endswith('2025'): os.chdir('2025')
    f = open(path, 'w')
    f.write(s)
    f.close()

def getHighestJoltageFromBank(bank : str) -> int:
    batteries = list(bank)
    largest = 0
    for i in range(len(batteries)):
        for j in range(i+1, len(batteries)):
            num = int(batteries[i] + batteries[j])
            if num > largest:
                largest = num
    return largest

def getHighestJoltageFromBank12Batteries(bank : str) -> int:
    batteries = [int(item) for item in list(bank)]
    
    while len(batteries) > 12:
        index = -1
        for i in range(len(batteries)-1):
            if batteries[i] < batteries[i+1]:
                index = i
                break
        batteries.pop(index)
    return int("".join([str(item) for item in batteries]))

def getPart1(input : list) -> int:
    total = 0
    for bank in input:
        total += getHighestJoltageFromBank(bank)
    return total

def getPart2(input : list) -> int:
    total = 0
    for bank in input:
        total += getHighestJoltageFromBank12Batteries(bank)
    return total

def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2


    answer[0] = getPart1(input)
    answer[1] = getPart2(input)
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
