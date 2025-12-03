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

ROCK_TYPES = {
    'HORIZ_LINE': ['@@@@', (4, 1)],
    'PLUS': ['.@.\n@@@\n.@.', (3, 3)],
    'BACKWARDS_L': ['..@\n..@\n@@@', (3, 3)],
    'VERT_LINE': ['@\n@\n@\n@', (1, 4)],
    'BLOCK': ['@@\n@@', (2, 2)]
}

class Rock:
    def __init__(self, typ, loc) -> None:
        self.typ = typ
        self.shape = None
        self.size = None
        self.loc = loc # bottom left of rock
        self.hitbox = None
        if self.typ in ROCK_TYPES.keys():
            self.shape = ROCK_TYPES[self.typ][0].split('\n')
            self.size = ROCK_TYPES[self.typ][1]
            self.hitbox = self.getHitBox()
    
    def getHitBox(self):
        hb = [[False for x in len(self.shape[0])] for y in len(self.shape)]
        for y in range(len(self.shape)):
            for x in range(len(self.shape[y])):
                if self.shape[y][x] == '@' or self.shape[y][x] == '#':
                    hb[y][x] = True
        return hb

    def moveLeft(self):
        if self.loc[0] == 0: return
        self.loc[0] -= 1

    def moveRight(self, grid):
        if self.loc[0] + self.size[0] >= len(grid[0]): return
        self.loc[0] += 1

    def moveDown(self, grid):
        bottom = self.loc[1] + self.size[1]
        if bottom >= len(grid): return
        for x_offs in range(self.size[0]):
            x = self.loc[0] + x_offs
            if not self.hitbox[self.size[1]-1][x_offs]: continue
            if grid[bottom][x] == '#': return
        self.loc[1] -= 1

def getAnswer(input, isSample):
    input = input.replace("\r", "").split("\n")
    answer = [0,0] #part1, part2

    rocks = []

    

    return answer

while(True):
    ans = getAnswer(*menu())
    print('\nanswer: {}'.format(ans))
