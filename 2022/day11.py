import sys
import os
import re
from functools import lru_cache

#sys.set_int_max_str_digits(sys.get_int_max_str_digits()*3)

def readFile(path):
    if not os.getcwd().endswith('2022'): os.chdir('2022')
    f = open(path, "r")
    return f.read().strip()

def printGrid(g, rev=False):
    if rev:
        for r in reversed(g):
            print(''.join(r))
    else:
        for r in g:
            print(''.join(r))

def addVector(a, b):
    v = []
    for i in range(len(a)):
        v.append(a[i] + b[i])
    return v

def subVector(a, b):
    v = []
    for i in range(len(a)):
        v.append(a[i] - b[i])
    return v

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

class Monkey():
    def __init__(self, input, printSteps = False) -> None:
        #Monkey #:
        #\tStarting items: #, #
        #\tOperation: new = old * num, new = old + num, new = old * old
        #\tTest: divisible by num
        #\t\tIf true: throw to monkey #
        #\t\tIf false: throw to monkey #
        lines = input.split('\n')
        self.id = int(lines[0].split(' ')[1][0:1])
        self.items = lines[1].split(': ')[1].split(', ')
        for i in range(len(self.items)):
            self.items[i] = int(self.items[i])
        op = lines[2].split(': ')[1].split('= old ')[1]
        op, num = op.split(' ')
        match op:
            case '*':
                if num == 'old':
                    self.op = self.square
                else:
                    self.op = self.multiply
                    self.opNum = int(num)
            case '+':
                self.op = self.add
                self.opNum = int(num)
            case _:
                self.op = None
        self.testNum = int(lines[3].split(' by ')[1])
        self.trueTest = int(lines[4][-1])
        self.falseTest = int(lines[5][-1])
        self.inspected = 0
        self.printSteps = printSteps
        
    def inspectItems(self, monkeys, lcm):
        if self.printSteps: print('Monkey {}:'.format(self.id))
        while len(self.items) > 0:
            if self.printSteps: print('  Monkey inspects an item with a worry level of {}.'.format(self.items[0]))
            self.op()
            self.items[0] %= lcm
            self.inspected += 1
            newMonkey = self.runTest()
            if self.printSteps: print('    Item with worry level {} is thrown to monkey {}.'.format(self.items[0], newMonkey))
            monkeys[newMonkey].items.append(self.items.pop(0))
    
    def multiply(self):
        self.items[0] *= self.opNum
        if self.printSteps: print('    Worry level is multiplied by {} to {}.'.format(self.opNum, self.items[0]))

    def add(self):
        self.items[0] += self.opNum
        if self.printSteps: print('    Worry level increases by {} to {}.'.format(self.opNum, self.items[0]))

    def square(self):
        self.items[0] *= self.items[0]
        if self.printSteps: print('    Worry level is multiplied by itself to {}.'.format(self.items[0]))

    def runTest(self):
        #self.items[0] //= 3
        if self.printSteps: print('    Monkey gets bored with item. Worry level is divided by 3 to {}.'.format(self.items[0]))
        if self.items[0] % self.testNum == 0:
            if self.printSteps: print('    Worry level is divisible by {}.'.format(self.testNum))
            return self.trueTest
        else:
            if self.printSteps: print('    Worry level is not divisible by {}.'.format(self.testNum))
            return self.falseTest

    def __str__(self) -> str:
        return '[{}]: {}'.format(self.id, self.inspected)

    def printWithItems(self):
        print('Monkey {}: {}'.format(self.id, len(self.items)))
        
def getAnswer(input):
    input = input.replace("\r", "").split("\n\n")
    answer = [0,0] #part1, part2
    
    monkeys = []
    for m in input:
        monkeys.append(Monkey(m, False))
    
    print('Initial Items:')
    for m in monkeys:
        m.printWithItems()

    lcm = 1
    for m in monkeys:
        lcm *= m.testNum

    for r in range(10000):
        for m in range(len(monkeys)):
            monkeys[m].inspectItems(monkeys, lcm)
        if r % 1000 == 0:
            print('Round {}'.format(r))
        if r % 2000 == 0:
            for m in monkeys:
                m.printWithItems()

    order = sorted(monkeys, key=lambda m: m.inspected, reverse=True)
    for m in order:
        print(m)    

    answer[0] = order[0].inspected * order[1].inspected
    answer[1] = 0

    return answer

while(True):
    ans = getAnswer(menu())
    print('\nanswer: {}'.format(ans))
