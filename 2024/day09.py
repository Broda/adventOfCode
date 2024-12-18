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

def getPart1(input : list) -> int:
    FileSystem = [None] * sum(input)
    id = 0
    file = True
    index = 0
    for n in input:
        if file:
            for i in range(n):
                FileSystem[index] = id
                index += 1
            id += 1
        else:
            index += n
        file = not file

    lastIndex = len(FileSystem)-1
    index = FileSystem.index(None)
    while index < lastIndex:
        val = FileSystem.pop()
        if val is not None:
            FileSystem[index] = val
            try:
                index = FileSystem.index(None, index+1)
            except ValueError:
                break
        lastIndex = len(FileSystem)-1

    chksum = 0
    for i in range(len(FileSystem)):
        chksum += i * FileSystem[i]
    
    return chksum

class File:
    def __init__(self, index, id, size):
        self.index = index
        self.id = id
        self.size = size

    def checksum(self) -> int:
        chk = 0
        for i in range(self.index, self.index + self.size):
            chk += i * self.id
        return chk
    
class Freespace:
    def __init__(self, index, size):
        self.index = index
        self.size = size

    def addFile(self, file : File):
        self.size -= file.size
        self.index += file.size

def getPart2(input : list) -> int:
    id = 0
    file = True
    index = 0
    freespace = []
    files = []
    for n in input:
        if file:
            files.append(File(index, id, n))
            id += 1
        else:
            freespace.append(Freespace(index, n))
        index += n
        file = not file

    fs : Freespace
    f : File
    for f in files[::-1]:
        for fs in freespace:
            if fs.size >= f.size and fs.index < f.index:
                index = f.index
                f.index = fs.index
                fs.addFile(f)
                freespace.append(Freespace(index, f.size))
                break

    chksum = 0
    for f in files:
        chksum += f.checksum()

    return chksum

def getAnswer(input, isSample) -> list:
    input = [int(x) for x in list(input)]
    answer = [0,0] #part1, part2


    answer[0] = getPart1(input)
    answer[1] = getPart2(input)
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
