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

def getProblemString(problems : list, colIndex : int) -> str:
    problem = ""
    operator = problems[-1][colIndex]
    for n in range(len(problems)-1):
        if len(problem) > 0: problem += operator
        problem += problems[n][colIndex]

    return problem

def getProblemString2(problems : list, colIndex : int) -> str:
    return problems[colIndex]

def doMath(probStr : function, problems : list, colIndex : int) -> int:
    problem = probStr(problems, colIndex)
    return eval(problem)

def getPart1(input : list) -> int:
    problems = []
    for line in input:
        problems.append(line.split())
    
    total = 0
    for c in range(len(problems[0])):
        total += doMath(getProblemString, problems, c)

    return total

def getPart2(input : list) -> int:
    # convert lines into character arrays
    for l in range(len(input)):
        input[l] = list(input[l])
    
    # find the operators and save their indices
    operatorIndices = []
    for c in range(len(input[-1])):
        if input[-1][c] != " ":
            operatorIndices.append(c)

    # build problem list
    problems = []
    for i in range(len(operatorIndices)):
        opIndex = operatorIndices[i]
        colWidth = 0
        endRange = 0
        if i == len(operatorIndices) - 1:
            colWidth = len(input[0]) - opIndex
            endRange = len(input[0])
        else:
            colWidth = operatorIndices[i+1] - opIndex
            endRange = opIndex + colWidth - 1

        problem = ""
        for c in range(opIndex, endRange):
            if len(problem) > 0: problem += input[-1][opIndex]
            num = ""
            for r in range(len(input) - 1):
                num += input[r][c]
            problem += num.strip()

        problems.append(problem)

    # doMath on each of the problems
    total = 0
    for c in range(len(problems)):
        total += doMath(getProblemString2, problems, c)

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
