f = open("input.txt", "r")
data = f.read().strip()
data = data.replace("\r", "").split("\n")

closing = {'[':']','{':'}','(':')','<':'>'}
points = {')':3,']':57,'}':1197,'>':25137}
comp_points = {')':1,']':2,'}':3,'>':4}

score = 0
comp_scores = []
closings = []
for i in range(len(data)):
    line = list(data[i])
    open = [line[0]]
    corrupted = False

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
                #print("line {} corrupted @ {}: {}".format(i, j, line[j]))
                score += points[line[j]]
                corrupted = True
                break
    if len(open) > 0 and not corrupted:
        close = ''
        comp_score = 0
        for j in reversed(open):
            close += closing[j]
            comp_score *= 5
            comp_score += comp_points[closing[j]]
        closings.append(close)
        comp_scores.append(comp_score)

def median(lst):
    sortedLst = sorted(lst)
    lstLen = len(lst)
    index = (lstLen - 1) // 2
   
    if (lstLen % 2):
        return sortedLst[index]
    else:
        return (sortedLst[index] + sortedLst[index + 1])/2.0

print("Corrupted Score: {}".format(score))
print("Completion Score: {}".format(median(comp_scores)))