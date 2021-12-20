def print_paper(p):
    for row in range(len(p)):
        line = ""
        for col in range(len(p[0])):
            line += p[row][col]
        print(line)

def fold_paper(p, fold):
    if fold[0] not in ['x','y']:
        return
    if fold[1] <= 0 or fold[1] >= len(p) - 1:
        return
    if fold[0] == 'x':
        for row in range(len(p)):
            for col in range(fold[1]+1, len(p[0])):
                if p[row][col] != '#':
                    continue
                f_col = fold[1] - col - fold[1]
                p[row][f_col] = '#'
        for row in range(len(p)):
            p[row] = p[row][:fold[1]]

    if fold[0] == 'y':
        for col in range(len(p[0])):
            for row in range(fold[1]+1, len(p)):
                if p[row][col] != '#':
                    continue
                f_row = fold[1] - row - fold[1]
                p[f_row][col] = '#'
        p = p[:fold[1]]

    

f = open("sample.txt", "r")
data = f.read().strip()
data = data.replace("\r", "").split("\n")

dots = []
folds = []
for line in data:
    if len(line) > 0:
        if 'fold' in line:
            f = line.replace('fold along ','')
            f = f.split('=')
            f[1] = int(f[1])
            folds.append(f)
        else:
            dots.append(line.split(','))

max_x = 0
max_y = 0
for i in range(len(dots)):
    dots[i][0] = int(dots[i][0])
    dots[i][1] = int(dots[i][1])
    if dots[i][0] > max_x:
        max_x = dots[i][0]
    if dots[i][1] > max_y:
        max_y = dots[i][1]

paper = [['.' for x in range(max_x+1)] for y in range(max_y+1)]
for d in dots:
    paper[d[1]][d[0]] = '#'

#print(dots)
#print(folds)
#print("max: ({},{})".format(max_x,max_y))
#print_paper(paper)

fold_paper(paper, folds[0])
print_paper(paper)