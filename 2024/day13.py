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

def getButtonMoves(line : str) -> tuple:
    #Button A: X+94, Y+34
    temp = line.replace(",", "").split()
    return (int(temp[2].split("+")[1]), int(temp[3].split("+")[1]))
    
def getPrizePos(line : str) -> list:
    #Prize: X=8400, Y=5400
    temp = line.replace(",", "").split()
    return [int(temp[1].split("=")[1]), int(temp[2].split("=")[1])]

def getPart1(input : list, AButtonCost : int, BButtonCost : int) -> int:
    tokens = 0
    for game in input:
        rules = game.split("\n")
        buttonA = getButtonMoves(rules[0])
        buttonB = getButtonMoves(rules[1])
        prizePos = getPrizePos(rules[2])
        
        #numA * buttonA[0] + numB * buttonB[0] = prize[0]
        #numA * buttonA[1] + numB * buttonB[1] = prize[1]
        den = buttonA[0] * buttonB[1] - buttonA[1] * buttonB[0]
        A = (prizePos[0] * buttonB[1] - prizePos[1] * buttonB[0]) // den
        B = (buttonA[0] * prizePos[1] - buttonA[1] * prizePos[0]) // den
        if (buttonA[0] * A + buttonB[0] * B, buttonA[1] * A + buttonB[1] * B) == (prizePos[0], prizePos[1]):
            tokens += A * AButtonCost + B * BButtonCost        
    
    return tokens

def getPart2(input : list, AButtonCost : int, BButtonCost : int) -> int:
    #10000000000000
    tokens = 0
    for game in input:
        rules = game.split("\n")
        buttonA = getButtonMoves(rules[0])
        buttonB = getButtonMoves(rules[1])
        prizePos = getPrizePos(rules[2])
        prizePos[0] += 10000000000000
        prizePos[1] += 10000000000000
        
        #numA * buttonA[0] + numB * buttonB[0] = prize[0]
        #numA * buttonA[1] + numB * buttonB[1] = prize[1]
        den = buttonA[0] * buttonB[1] - buttonA[1] * buttonB[0]
        A = (prizePos[0] * buttonB[1] - prizePos[1] * buttonB[0]) // den
        B = (buttonA[0] * prizePos[1] - buttonA[1] * prizePos[0]) // den
        if (buttonA[0] * A + buttonB[0] * B, buttonA[1] * A + buttonB[1] * B) == (prizePos[0], prizePos[1]):
            tokens += A * AButtonCost + B * BButtonCost        
    
    
    return tokens

def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n\n")
    answer = [0,0] #part1, part2


    answer[0] = getPart1(input, 3, 1)
    answer[1] = getPart2(input, 3, 1)
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
