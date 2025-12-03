def printGrid(grid):
    for r in range(len(grid)):
        print(grid[r])
    print('-----------------')

def replace_char(s, index, new_char):
    return s[:index] + new_char + s[index + 1:]

def move_east(d):
    d2 = d.copy()
    change = False
    for i in range(len(d)):
        row = d[i]
        newrow = row
        for j in range(len(row)):
            next_index = j+1
            if next_index >= len(row):
                next_index = 0

            curr = row[j]
            next = row[next_index]

            if curr == '>' and next == '.':
                d2[i] = replace_char(d2[i], j, '.')
                d2[i] = replace_char(d2[i], next_index, '>')
                change = True

    return [change, d2]

def move_down(d):
    d2 = d.copy()
    change = False
    for i in range(len(d)):
        next_i = i+1
        if next_i >= len(d):
            next_i = 0
        
        row = d[i]
        nextrow = d[next_i]
        newrow = row
        newnextrow = nextrow
        
        for j in range(len(row)):
            curr = row[j]
            next = nextrow[j]
            
            if curr == 'v' and next == '.':
                d2[i] = replace_char(d2[i], j, '.')
                d2[next_i] = replace_char(d2[next_i], j, 'v')
                change = True
        
    return [change, d2]


f = open("input.txt", "r")
data = f.read().strip()
data = data.replace("\r", "").split("\n")
# printGrid(data)

round = 0
change = True
while (change):
    round += 1
    eastmoved, data = move_east(data)
    southmoved, data = move_down(data)
    change = eastmoved or southmoved

print(round)