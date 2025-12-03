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
    if not os.getcwd().endswith('2017'): os.chdir('2017')
    f = open(path, "r")
    return f.read().strip()

def writeFile(path, s):
    if not os.getcwd().endswith('2017'): os.chdir('2017')
    f = open(path, 'w')
    f.write(s)
    f.close()

def getPart1(input : list) -> int:
    csum = 0
    for line in input:
        numbers = [int(x) for x in line.split()]
        csum += max(numbers)-min(numbers)

    return csum

def getPart2(input : list) -> int:
    csum = 0
    for line in input:
        numbers = [int(x) for x in line.split()]
        numbers.sort(reverse=True)
        for i in range(len(numbers)-1):
            for j in range(1, len(numbers)):
                if i == j: continue
                if numbers[i] % numbers[j] == 0: csum += numbers[i] // numbers[j]
    return csum

def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2


    answer[0] = getPart1(input)
    answer[1] = getPart2(input)
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
