def print_paper(p):
    for row in range(len(p)):
        line = ""
        for col in range(len(p[0])):
            line += p[row][col]
        print(line)

def parse_fold(line):
    l = line.split(' ')
    l = l[len(l)-1].split('=')
    l[1] = int(l[1])
    return l

def fold_paper(p, axis, num):
    if axis == 'y':
        num_rows = num - 1
        diff = len(p) - num - 1
        if diff - num > 0:
            num_rows += (diff - num)

        new_paper = [['.' for col in range(len(p[0]))] for row in range(num_rows+1)]
        for row in range(len(p)):
            curr_row = row
            if row == num:
                continue
            if row > num:
                curr_row = num - (row - num)
            for col in range(len(p[0])):
                if p[row][col] == '#':
                    new_paper[curr_row][col] = '#'
    if axis == 'x':
        num_cols = num - 1
        diff = len(p[0]) - num - 1
        if diff - num > 0:
            num_cols += (diff - num)

        new_paper = [['.' for col in range(num_cols+1)] for row in range(len(p))]
        for row in range(len(p)):
            for col in range(len(p[0])):
                curr_col = col
                if col == num:
                    continue
                if col > num:
                    curr_col = num - (col - num)
                if p[row][col] == '#':
                    new_paper[row][curr_col] = '#'
    return new_paper

def count_dots(p):
    count = 0
    for row in range(len(p)):
        for col in range(len(p[0])):
            if p[row][col] == '#':
                count += 1
    return count

f = open("input.txt", "r")
data = f.read().strip()
data = data.replace("\r", "").split("\n")

points = []
folds = []
num_rows = 0
num_cols = 0

for line in data:
    if ',' in line:
        p = line.split(',')
        p[0] = int(p[0])
        p[1] = int(p[1])
        points.append(p)
        if p[0] > num_cols:
            num_cols = p[0]
        if p[1] > num_rows:
            num_rows = p[1]
    elif '=' in line:
        folds.append(parse_fold(line))

num_cols = num_cols + 1
num_rows = num_rows + 1
paper = [['.' for col in range(num_cols)] for row in range(num_rows)]

for p in points:
    paper[p[1]][p[0]] = '#'

#print_paper(paper)

for f in folds:
    #print("fold: {}".format(f))
    paper = fold_paper(paper, f[0], f[1])
    #break #part 1

print_paper(paper)
#print("")
#print(count_dots(paper))