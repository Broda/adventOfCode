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
        self.cmds = {'cpy': self.cpy, 'inc': self.inc, 'dec': self.dec, 'jnz': self.jnz}

    def runProgram(self, prog : list) -> None:
        self.pointer = 0
        self.cmdCnt = 0
        while True:
            if self.pointer >= len(prog): break

            self.exec(prog[self.pointer])

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
        self.registers[y] = self.getRegVal(x)
        self.pointer += 1

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

def getPart1(input : list) -> int:
    c : Computer = Computer()
    c.runProgram(input)
    
    return c.registers["a"]

def getPart2(input : list) -> int:
    c : Computer = Computer()
    c.registers["c"] = 1
    c.runProgram(input)
    
    return c.registers["a"]

def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2


    answer[0] = getPart1(input)
    answer[1] = getPart2(input)
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
