
f = open("input.txt", "r")
data = f.read().strip()
data = data.replace("\r", "").split("\n")

board = []
for l in data:
    row = list(l)
    row = [int(x) for x in row]
    board.append(row)

def getUpVal(board, row, col):
    if row == 0:
        return 999
    else:
        return board[row-1][col]

def getDownVal(board, row, col):
    if row == len(board)-1:
        return 999
    else:
        return board[row+1][col]

def getLeftVal(board, row, col):
    if col == 0:
        return 999
    else:
        return board[row][col-1]

def getRightVal(board, row, col):
    if col == len(board[0])-1:
        return 999
    else:
        return board[row][col+1]

def isLowPoint(board, row, col):
    curr = board[row][col]
    return (curr < getUpVal(board, row, col) and curr < getDownVal(board, row, col) and curr < getLeftVal(board, row, col) and curr < getRightVal(board, row, col))

lowpoints = []
for row in range(len(board)):
    for col in range(len(board[0])):
        if isLowPoint(board, row, col):
            low = [row, col]
            if low not in lowpoints:
                lowpoints.append(low)

risk = 0
for p in lowpoints:
    risk += int(board[p[0]][p[1]])+1

print("{} lowpoints found with risk of {}".format(len(lowpoints), risk))
