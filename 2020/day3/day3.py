ROW = 0
COL = 1

class Map:
    def __init__(self, rows):
        self.currPos = [0,0]
        self.rows = rows
        self.rowCount = len(rows)
        self.colCount = len(rows[0])-1
        #print("Rows: " + str(self.rowCount) + ", Cols: " + str(self.colCount))
        
    def countTrees(self, run, rise):
        count = 0
        self.currPos = [0,0]
        while (self.currPos[ROW]<self.rowCount):
            self.currPos[ROW] += rise
            self.currPos[COL] += run
            #print(self.printCurrPos())

            if self.currPos[ROW] >= self.rowCount:
                break

            col = self.currPos[COL] % self.colCount
            #print("Col: " + str(col))
            spot = self.rows[self.currPos[ROW]][col]
            #print(self.printCurrPos() + " = " + spot)
            if spot == "#":
                count += 1
        return count

    def printCurrPos(self):
        return str(self.currPos[ROW]) + ", " + str(self.currPos[COL])

def part1():
    print(map.countTrees(3, 1))
    
def part2():
    print(map.countTrees(1, 1) *
    map.countTrees(3, 1) *
    map.countTrees(5, 1) *
    map.countTrees(7, 1) *
    map.countTrees(1, 2))

f = open("input.txt", "r")
map = Map(f.readlines())

#part1()
part2()