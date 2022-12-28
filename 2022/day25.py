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
    if not os.getcwd().endswith('2022'): os.chdir('2022')
    f = open(path, "r")
    return f.read().strip()

def writeFile(path, s):
    if not os.getcwd().endswith('2022'): os.chdir('2022')
    f = open(path, 'w')
    f.write(s)
    f.close()

SNAFU_VALUES = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2, 2:"2", 1:"1", 0:"0", -1:"-", -2: "="}

def getDecimal(snafu):
    rev = snafu[::-1] # reverse string
    val = 0

    for power, c in enumerate(rev):
        val += 5 ** power * SNAFU_VALUES[c]

    return val

def padSnafu(n, amt):
    return ['0'] * amt + list(n)

def addSnafu(n1, n2):
    new = []
    extra = 0

    if len(n1) > len(n2):
        n2 = padSnafu(n2, len(n1) - len(n2))
    else:
        n1 = padSnafu(n1, len(n2) - len(n1))
    
    for n1, n2 in zip(n1[::-1], n2[::-1]):
        num = SNAFU_VALUES[n1] + SNAFU_VALUES[n2] + extra
        if num > 2:
            new.append(SNAFU_VALUES[num-5])
            extra = 1
        elif num < -2:
            new.append(SNAFU_VALUES[num+5])
            extra = -1
        else:
            new.append(SNAFU_VALUES[num])
            extra = 0
    
    if extra:
        new.append(str(extra))

    return list(reversed(new))

def getSnafu(decimal):
    curr = ['1','0']
    nums = ['1','2','1-','1=']
    while True:
        if getDecimal(curr) < decimal:
            curr.append('0')
        else:
            curr.pop()
            break
    
    flag = True
    while flag:
        for i, lead in enumerate(nums):
            curr[0] = lead
            if getDecimal(''.join(curr)) > decimal:
                curr[0] = nums[i-1]
                flag = False
                break
            elif i == 3:
                flag = False
                break
    
    newCurr = []
    for n in curr:
        newCurr.extend(list(n))
    curr = newCurr

    remain = decimal - getDecimal(''.join(curr))
    if remain == 0:
        return ''.join(curr)
    return ''.join(addSnafu(curr, getSnafu(remain)))

def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2

    sum = 0
    for l in input:
        sum += getDecimal(l)
    
    answer[0] = getSnafu(sum)

    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))



