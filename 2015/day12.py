import sys
import os
import re
import json

def readFile(path):
    if not os.getcwd().endswith('2015'): os.chdir('2015')
    f = open(path, "r")
    return f.read().strip()

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
            return readFile(samplePath)
        case "2":
            return readFile(inputPath)
        case "3":
            return readFile(input("File Name: "))
        case "4":
            return input("Input: ")
        case _:
            print("Invalid option. Try Again.\n")
            return menu()

def part1(input):
    reg = re.compile(r'(-?[\d]+)')
    sum = 0
    for num in re.findall(reg, input):
        sum += int(num)
    return sum

def eval_obj_without_red(match):
    m = match.group()
    if ':"red"' not in m:
        return str(part1(m))
    else:
        return str(0)

def part2(input):
    while ':"red"' in input:
        input = re.sub(r"{[^{}]*}", eval_obj_without_red, input)
    return part1(input)

def getAnswer(input):
    if '\r' in input or '\n' in input:
        input = input.replace("\r", "").split("\n")
        input = ''.join(input)
    answer = ['',''] #part1, part2
    
    answer[0] = part1(input)
    answer[1] = part2(input)
    return answer

while(True):
    ans = getAnswer(menu())
    print(ans)
