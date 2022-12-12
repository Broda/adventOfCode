
def calcManhatten(grid, end):
    m = []
    for r in range(len(grid)):
        row = []
        for c in range(len(grid[0])):
            row.append(abs(end[0] - r) + abs(end[1] - c))
        m.append(row)
    return m

def findCell(grid, letter):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == letter: return [r,c]
    return None

def printGrid(g, rev=False):
    if rev:
        for r in reversed(g):
            print(''.join(r))
    else:
        for r in g:
            print(''.join(str(r)))
