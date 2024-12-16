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

def buildEquation(values : list, operators : list) -> str:
    equation = values[0]
    for i in range(1, len(values)):
        equation +=  operators[i-1] + values[i]
    return equation

def padZeros(numStr : str, length : int) -> str:
    return "0" * (length - len(numStr)) + numStr

def buildOps(numOps : int) -> list:
    ops = []
    for i in range(2**numOps):
        binary = padZeros(bin(i).replace("0b", ""), numOps)
        ops.append(list(binary.replace("0", "+").replace("1", "*")))
        
    return ops

def ternary(n : int) -> str:
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))

def buildOps2(numOps : int) -> list:
    ops = []
    for i in range(3**numOps):
        tern = padZeros(ternary(i), numOps)
        o = []
        for c in tern:
            o.append(c.replace("0", "+").replace("1", "*").replace("2", "||"))
        ops.append(o)
        
    return ops

def runEquation(values : list, o : list) -> int:
    val = values[0]
    for v in range(1, len(values)):
        if o[v-1] == "||":
            val = int(str(val) + str(values[v]))
        else:
            val = eval(str(val)+o[v-1]+str(values[v]))
    return val

def validEquation(total : int, values : list, ops : list) -> bool:    
    for o in ops:
        val = runEquation(values, o)
        if val == total:
            return True    
        
    return False

def getPart1(equations : list) -> int:
    sum = 0
    for eq in equations:
        total = int(eq[0])
        values = eq[1].split(" ")
        ops = buildOps(len(values)-1)
        if validEquation(total, values, ops):
            sum += int(eq[0])
    return sum

def getPart2(equations : list) -> int:
    sum = 0
    for eq in equations:
        total = int(eq[0])
        values = eq[1].split(" ")
        ops = buildOps2(len(values)-1)
        if validEquation(total, values, ops):
            sum += int(eq[0])
    return sum

def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2

    equations = [x.split(": ") for x in input]
    answer[0] = getPart1(equations)
    answer[1] = getPart2(equations)
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
