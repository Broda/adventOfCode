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

class Computer:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C
        self.InstPtr = 0
        self.Output = ""
        self.OpCodes = {0:self.adv,
           1:self.bxl,
           2:self.bst,
           3:self.jnz,
           4:self.bxc,
           5:self.out,
           6:self.bdv,
           7:self.cdv}
        
    def runProg(self, prog : list) -> str:
        while self.InstPtr < len(prog):
            opcode = prog[self.InstPtr]
            operand = prog[self.InstPtr+1]
            self.OpCodes[opcode](operand)
        return self.Output
    
    def getOperandVal(self, operand : int) -> int:
        match operand:
            case 0 | 1 | 2 | 3 | 7:
                return operand
            case 4:
                return self.A
            case 5:
                return self.B
            case 6:
                return self.C
                
    def div(self, operand : int) -> int:
        den = 2 ** self.getOperandVal(operand)
        return self.A // den

    def adv(self, operand : int):
        self.A = self.div(operand)
        self.InstPtr += 2

    def bxl(self, operand : int):
        self.B = self.B ^ operand
        self.InstPtr += 2
        
    def bst(self, operand : int):
        self.B = self.getOperandVal(operand) % 8
        self.InstPtr += 2
        
    def jnz(self, operand : int):
        if self.A == 0: 
            self.InstPtr += 2
        else:
            self.InstPtr = operand
        
    def bxc(self, operand : int):
        self.B = self.B ^ self.C
        self.InstPtr += 2
        
    def out(self, operand : int):
        val = self.getOperandVal(operand) % 8
            
        if len(self.Output) > 0:
            self.Output += ","
        self.Output += str(val)
        self.InstPtr += 2
        
    def bdv(self, operand : int):
        self.B = self.div(operand)
        self.InstPtr += 2

    def cdv(self, operand : int):
        self.C = self.div(operand)
        self.InstPtr += 2


def getPart1(A : int, B : int, C: int, prog : list) -> int:
    comp = Computer(A, B, C)
    
    print(comp.runProg(prog))
    return 0

def getPart2(A : int, B : int, C: int, prog : list) -> int:
    progStr = ','.join(map(str, prog))
    
    #comp = Computer()
    return 0

def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n\n")
    answer = [0,0] #part1, part2

    temp = input[0].split("\n")
    A = int(temp[0].split(": ")[1])
    B = int(temp[1].split(": ")[1])
    C = int(temp[2].split(": ")[1])

    prog = [int(x) for x in input[1].split(": ")[1].split(",")]
    answer[0] = getPart1(A, B, C, prog)
    answer[1] = getPart2(A, B, C, prog)
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
