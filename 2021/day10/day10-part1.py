f = open("input.txt", "r")
data = f.read().strip()
data = data.replace("\r", "").split("\n")

closing = {'[':']','{':'}','(':')','<':'>'}
points = {')':3,']':57,'}':1197,'>':25137}

score = 0

for i in range(len(data)):
    line = list(data[i])
    open = [line[0]]
    
    for j in range(1,len(line)):
        if len(open)==0:
            last_open = ''
        else:
            last_open = open[len(open)-1]
        if line[j] in closing.keys():
            open.append(line[j])
            continue
        if last_open in closing.keys():
            if line[j] == closing[last_open]:
                open.pop()
            else:
                print("line {} corrupted @ {}: {}".format(i, j, line[j]))
                score += points[line[j]]
                break
print(score)