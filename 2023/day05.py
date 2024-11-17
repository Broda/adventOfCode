import os
import sys
import functools

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

class Map():
    def __init__(self, lines) -> None:
        self.lines = lines
        self.name = lines[0].replace(' map:', '')
        self.ranges = [x.split() for x in lines[1::]]
        for i in range(len(self.ranges)):
            for j in range(len(self.ranges[i])):
                self.ranges[i][j] = int(self.ranges[i][j])
        #print(f'{self.name}: {self.ranges}')

    @functools.lru_cache
    def getDestination(self, src):
        for r in self.ranges:
            if src >= r[1] and src < r[1]+r[2]:
                offset = src - r[1]
                return r[0] + offset
        return src

def getMaps(input):
    maps = []
    mStart = -1
    for i in range(1, len(input)):
        if len(input[i]) == 0 or i == len(input)-1:
            if mStart > 0:
                m = Map(input[mStart:i])
                maps.append(m)
                mStart = -1
        elif input[i].endswith('map:'):
            mStart = i
    return maps

def getSeedLocation(maps, seed):
    dest = seed
    for m in maps:
        dest = m.getDestination(dest)
    return dest

def getMinSeedLocation(seeds, maps):
    minLoc = sys.maxsize
    for s in seeds:
        loc = getSeedLocation(maps,int(s))
        if loc < minLoc:
            minLoc = loc
    return minLoc

def getSeeds2(seeds):
    seeds2 = []
    for i in range(0,len(seeds),2):
        seeds2 += getSeeds(int(seeds[i]), int(seeds[i+1]))
        
    return seeds2

@functools.lru_cache
def getSeeds(start, num):
    return [i for i in range(start, start+num)]
    
def getAnswer(input, isSample) -> list:
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2

    seeds = input[0].split(': ')[1].split()
    maps = getMaps(input)    

    print('getting seeds2')
    seeds2 = getSeeds2(seeds)
    print('got seeds2')

    answer[0] = getMinSeedLocation(seeds, maps)
    answer[1] = getMinSeedLocation(seeds2, maps)
    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))


