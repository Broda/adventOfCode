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

class Race:
    def __init__(self, time, record) -> None:
        self.time = int(time)
        self.record = int(record)
        self.winningWays = self.getWinningWays()

    def getWinningWays(self):
        ways = []
        for speed in range(1, self.time):
            timeToMove = self.time - speed
            dist = timeToMove * speed
            if dist > self.record:
                ways.append((speed, dist))
        return ways


def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2

    times = input[0].split()
    records = input[1].split()
    
    races = []
    product = 1
    time = ''
    record = ''
    for r in range(1,len(times)):
        time += times[r]
        record += records[r]
        races.append(Race(times[r], records[r]))
        product *= len(races[-1].winningWays)

    finalRace = Race(time, record)

    answer[0] = product
    answer[1] = len(finalRace.winningWays)
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))


