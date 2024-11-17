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
    print(os.getcwd())
    if not os.getcwd().endswith('2023'): os.chdir('2023')
    f = open(path, "r")
    return f.read().strip()

def writeFile(path, s):
    if not os.getcwd().endswith('2023'): os.chdir('2023')
    f = open(path, 'w')
    f.write(s)
    f.close()

def getFirstNumber(line):
    for c in line:
        if c.isnumeric():
            return int(c)
    return 0

def getLastNumber(line):
    for c in line[::-1]:
        if c.isnumeric():
            return int(c)
    return 0

def getSum(lines):
    sum = 0
    for l in lines:
        n1 = getFirstNumber(l)
        n2 = getLastNumber(l)
        sum += int(str(n1)+str(n2))
    return sum

def swapNumbers(lines, numbers):
    for i in range(len(lines)):
        for k in numbers.keys():
            lines[i] = lines[i].replace(k, numbers[k])
    return lines

def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2

    numbers = {'one':'o1ne','two':'t2wo','three':'t3hree','four':'f4our','five':'f5ive','six':'s6ix','seven':'s7even','eight':'e8ight','nine':'n9ine'}

    answer[0] = getSum(input)
    answer[1] = getSum(swapNumbers(input,numbers))
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))


