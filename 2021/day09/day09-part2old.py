
f = open("sample.txt", "r")
data = f.read().strip()
data = data.replace("\r", "").split("\n")

class Point:
    def __init__(self, row, col, value, maxrow, maxcol):
        self.row = row
        self.col = col
        self.value = value
        self.maxrow = maxrow
        self.maxcol = maxcol
        self.point = (row, col)

        self.left = col - 1
        if self.left < 0:
            self.left = None
        self.right = col + 1
        if self.right > maxcol:
            self.right = None
        self.up = row - 1
        if self.up < 0:
            self.up = None
        self.down = row + 1
        if self.down > maxrow:
            self.down = None

    def __str__(self):
        return "{}".format(self.point)

    def updateNeighbors(self, points):
        self.leftp = None
        self.rightp = None
        self.upp = None
        self.downp = None

        for p in points:
            if p.col == self.col and p.row == self.left:
                self.leftp = p
            elif p.col == self.col and p.row == self.right:
                self.rightp = p
            elif p.col == self.up and p.row == self.row:
                self.upp = p
            elif p.col == self.down and p.row == self.row:
                self.downp = p
    
    def isLowPoint(self):
        if self.leftp is not None:
            if self.value > self.leftp.value:
                return False
        if self.rightp is not None:
            if self.value > self.rightp.value:
                return False
        if self.upp is not None:
            if self.value > self.upp.value:
                return False
        if self.downp is not None:
            if self.value > self.downp.value:
                return False
        
        return True
        
                
class Board:
    def __init__(self, data):
        self.data = data
        self.raw_board = []
        for l in data:
            row = list(l)
            row = [int(x) for x in row]
            self.raw_board.append(row)
        self.points = []
        for row in range(len(self.raw_board)):
            for col in range(len(self.raw_board[0])):
                self.points.append(Point(row, col, self.raw_board[row][col], len(self.raw_board)-1, len(self.raw_board[0])-1))
        for p in self.points:
            p.updateNeighbors(self.points)
    
    def print(self):
        for p in self.points:
            print(p)

    def findLowPoints(self):
        lowpoints = []
        for p in self.points:
            if p.isLowPoint() and p not in lowpoints:
                lowpoints.append(p)
        return lowpoints
        # for row in range(len(self.raw_board)):
        #     for col in range(len(self.raw_board[0])):
        #         if isLowPoint(self.raw_board, row, col):
        #             low = (row, col)
        #             if low not in lowpoints:
        #                 lowpoints.append(low)

def getUpPos(board, point):
    if point[0] <= 0:
        return None
    else:
        return (point[0]-1, point[1])

def getDownPos(board, point):
    if point[0] >= len(board)-1:
        return None
    else:
        return (point[0]+1, point[1])

def getLeftPos(board, point):
    if point[1] <= 0:
        return None
    else:
        return (point[0], point[1]-1)

def getRightPos(board, point):
    if point[1] >= len(board[0])-1:
        return None
    else:
        return (point[0], point[1]+1)

def getUpVal(board, row, col):
    if row <= 0:
        return 999
    else:
        return board[row-1][col]

def getDownVal(board, row, col):
    if row >= len(board)-1:
        return 999
    else:
        return board[row+1][col]

def getLeftVal(board, row, col):
    if col <= 0:
        return 999
    else:
        return board[row][col-1]

def getRightVal(board, row, col):
    if col >= len(board[0])-1:
        return 999
    else:
        return board[row][col+1]

def isLowPoint(board, row, col):
    curr = board[row][col]
    return (curr < getUpVal(board, row, col) and curr < getDownVal(board, row, col) and curr < getLeftVal(board, row, col) and curr < getRightVal(board, row, col))

def getBasinNeighbors(board, basin, point):
    up = getUpVal(board, point[0], point[1])
    down = getDownVal(board, point[0], point[1])
    left = getLeftVal(board, point[0], point[1])
    right = getRightVal(board, point[0], point[1])
    if up < 9:
        upPos = getUpPos(board, point[0], point[1])
        if upPos not in basin:
            basin.append(upPos)
        #getBasinNeighbors(board, basin, upPos)
    if down < 9:
        dnPos = getDownPos(board, point[0], point[1])
        if dnPos not in basin:
            basin.append(dnPos)
        #getBasinNeighbors(board, basin, dnPos)
    if left < 9:
        ltPos = getLeftPos(board, point[0], point[1])
        if ltPos not in basin:
            basin.append(ltPos)
        #getBasinNeighbors(board, basin, ltPos)
    if right < 9:
        rtPos = getRightPos(board, point[0], point[1])
        if rtPos not in basin:
            basin.append(rtPos)
        #getBasinNeighbors(board, basin, rtPos)
    
b = Board(data)
#b.print()

lowpoints = b.findLowPoints()
for p in lowpoints:
    print(p)

# for row in range(len(board)):
#     for col in range(len(board[0])):
#         if isLowPoint(board, row, col):
#             low = (row, col)
#             if low not in lowpoints:
#                 lowpoints.append(low)

# risk = 0
# for p in lowpoints:
#     risk += int(board[p[0]][p[1]])+1

# print("{} lowpoints found with risk of {}".format(len(lowpoints), risk))

# basins = []

# #for i in range(len(lowpoints)):
# b = []
# getBasinNeighbors(board, b, lowpoints[0])
# basins.append(b)

# print(basins)