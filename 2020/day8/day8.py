class CPU:
    def __init__(self, listdata):
        self.initdata = listdata
        self.loadProgram(listdata)

    def resetProgram(self):
        self.loadProgram(self.initdata)

    def loadProgram(self, listdata):
        self.acc = 0
        self.ptr = 0
        self.program = []
        for i in listdata:
            self.program.append(Instruction(i))

    def runProgram(self):
        while self.ptr < len(self.program):
            if self.program[self.ptr].executed:
                print(self.acc)
                return False
            
            self.program[self.ptr].Execute(self)
        print("Complete, {}".format(self.acc))
        return True
        

class Instruction:
    def __init__(self, data):
        self.data = data
        self.inst, self.arg = data.split(" ")
        self.arg = int(self.arg.replace("+", ""))
        self.executed = False
    
    def Execute(self, cpu):
        if self.inst == "nop":
            self.executed = True
            cpu.ptr += 1
            return
        
        if self.inst == "acc":
            cpu.acc += self.arg
            self.executed = True
            cpu.ptr += 1
            return

        if self.inst == "jmp":
            cpu.ptr += self.arg
            self.executed = True
            return
        
        return

f = open("input.txt", "r")
cpu = CPU(f.readlines())

#part 1
print(cpu.runProgram())

#part 2
for i in range(len(cpu.program)):
    if cpu.program[i].inst == "nop":
        cpu.program[i].inst = "jmp"
        if cpu.runProgram():
            print("{} nop to jmp".format(i))
            break
        else:
            cpu.resetProgram()

for i in range(len(cpu.program)):
    if cpu.program[i].inst == "jmp":
        cpu.program[i].inst = "nop"
        if cpu.runProgram():
            print("{} jmp to nop".format(i))
            break
        else:
            cpu.resetProgram()

