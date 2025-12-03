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
    if not os.getcwd().endswith('2023'): os.chdir('2023')
    f = open(path, "r")
    return f.read().strip()

def writeFile(path, s):
    if not os.getcwd().endswith('2023'): os.chdir('2023')
    f = open(path, 'w')
    f.write(s)
    f.close()

class Number():
    def __init__(self, num, row, col) -> None:
        self.num = int(num)
        self.row = row
        self.col = col
        self.length = len(num)
    
    def __str__(self):
        return f'{self.num} ({self.row},{self.col}-{self.col+self.length-1})'

class Grid():
    def __init__(self, input) -> None:
        self.lines = input
        self.numbers = self.findNumbers()
    
    def findNumbers(self):
        numbers = []
        for i in range(len(self.lines)):
            l = self.lines[i]
            n = ''
            start = 0
            for j in range(len(l)):
                c = l[j]
                if c.isnumeric():
                    if len(n) == 0: start = j
                    n += c
                elif len(n) > 0:
                    numbers.append(Number(n, i, start))
                    print(numbers[-1])
                    n = ''
                else:
                    n = ''
        return numbers
    
    def isPartNumber(self, number):
        for r in range(number.row-1,number.row+2):
            if r < 0 or r >= len(self.lines): 
                pass
            else:
                for c in range(number.col-1,number.col+number.length+1):
                    if c < 0 or c >= len(self.lines[r]): 
                        pass
                    else:
                        if not self.lines[r][c].isnumeric() and self.lines[r][c] != '.': 
                            print(f'{number.num} touching \'{self.lines[r][c]}\'')
                            return True
        return False
    
    def getSumOfPartNumbers(self):
        sum = 0
        for n in self.numbers:
            if self.isPartNumber(n):
                sum += n.num
        return sum

def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2

    g = Grid(input)

    answer[0] = g.getSumOfPartNumbers()
    answer[1] = 0
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))


