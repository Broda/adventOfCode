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
    if not os.getcwd().endswith('2016'): os.chdir('2016')
    f = open(path, "r")
    return f.read().strip()

def writeFile(path, s):
    if not os.getcwd().endswith('2016'): os.chdir('2016')
    f = open(path, 'w')
    f.write(s)
    f.close()

class Computer:
    def __init__(self):
        self.registers = {'a':0, 'b':0, 'c':0, 'd':0}
        self.pointer : int = 0
        self.cmds = {'cpy': self.cpy, 'inc': self.inc, 'dec': self.dec, 'jnz': self.jnz, 'tgl': self.tgl}
        self.program = []

    def runProgram(self, prog : list) -> None:
        self.program = prog.copy()
        self.pointer = 0
        self.cmdCnt = 0
        while True:
            if self.pointer >= len(self.program): break

            self.exec(self.program[self.pointer])

    def exec(self, cmd : str) -> None:
        sCmd = cmd.split(" ")
        if len(sCmd) < 3:
            self.cmds[sCmd[0]](sCmd[1])
        else:
            self.cmds[sCmd[0]](sCmd[1], sCmd[2])     

    def getRegVal(self, x : str) -> int:
        try: 
            return int(x)
        except:
            return self.registers[x]
        
    def cpy(self, x : str, y : str) -> None:
        self.pointer += 1
        if y not in self.registers: return
        self.registers[y] = self.getRegVal(x)

    def inc(self, x : str) -> None:
        self.registers[x] += 1
        self.pointer += 1

    def dec(self, x : str) -> None:
        self.registers[x] -= 1
        self.pointer += 1

    def jnz(self, x : str, y : str) -> None:
        if self.getRegVal(x) == 0:
            self.pointer += 1
            return
        
        self.pointer += self.getRegVal(y)

    def tgl(self, x : str) -> None:
        cmdIndex : int = self.pointer + self.getRegVal(x)
        self.pointer += 1
        if cmdIndex < 0 or cmdIndex >= len(self.program): return
        
        awayCmdSplit : list = self.program[cmdIndex].split(" ")
        match awayCmdSplit[0]:
            case "inc":
                self.program[cmdIndex] = self.program[cmdIndex].replace("inc ", "dec ")
            case "jnz":
                self.program[cmdIndex] = self.program[cmdIndex].replace("jnz ", "cpy ")
            case _:
                if len(awayCmdSplit) > 2:
                    self.program[cmdIndex] = f"jnz {awayCmdSplit[1]} {awayCmdSplit[2]}"
                else:
                    self.program[cmdIndex] = f"inc {awayCmdSplit[1]}"     
                    

def getPart1(input : list, initA : int) -> int:
    c : Computer = Computer()
    c.registers["a"] = initA
    print(f"registers: {c.registers}")
    c.runProgram(input)

    return c.registers["a"]

def getPart2(input : list, initA : int) -> int:
    return getPart1(input, initA)

def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2

    answer[0] = getPart1(input, 7)
    answer[1] = getPart2(input, 12)
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
