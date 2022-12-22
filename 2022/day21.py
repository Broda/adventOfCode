import os
import sys
from sympy.solvers import solve

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
    if not os.getcwd().endswith('2022'): os.chdir('2022')
    f = open(path, "r")
    return f.read().strip()

def getPart1(input):
    monkeys = {}
    value_monkeys = {}
    for l in input:
        m, v = l.split(': ')
        if v.isnumeric():
            value_monkeys[m] = int(v)
        else:
            monkeys[m] = v.split(' ')

    while len(monkeys) > 0:
        lastlen = len(monkeys)
        keys = list(monkeys.keys())
        for m in keys:
            for i in [0,2]:
                if monkeys[m][i] in value_monkeys.keys():
                    monkeys[m][i] = value_monkeys[monkeys[m][i]]
            if type(monkeys[m][0]) is int and type(monkeys[m][2]) is int:
                value_monkeys[m] = int(eval('{}{}{}'.format(monkeys[m][0],monkeys[m][1],monkeys[m][2])))
                monkeys.pop(m)

        if len(monkeys) == lastlen: 
            print('BREAK')
            break
    return value_monkeys['root']

def unwindExp(monkeys, curr):
    if type(monkeys[curr]) is list:
        return '({} {} {})'.format(unwindExp(monkeys, monkeys[curr][0]), monkeys[curr][1], unwindExp(monkeys, monkeys[curr][2]))
    return monkeys[curr]

def getPart2(input):
    monkeys = {}
    for l in input:
        m, v = l.split(': ')
        if v.isnumeric():
            monkeys[m] = int(v)
        else:
            monkeys[m] = v.split(' ')
    monkeys['root'][1] = '-'
    monkeys['humn'] = 'x'
    return solve(unwindExp(monkeys, 'root'))[0]
    

def getAnswer(input, isSample):
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2

    answer[0] = getPart1(input)
    answer[1] = getPart2(input)

    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
