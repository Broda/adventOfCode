def initDict():
    _d = {}
    for c in range(65, 65+26):
        _d[chr(c)] = 0
    return _d

def updateDict(_d, answers):
    answers = list(answers.upper())
    for c in answers:
        _d[c] += 1
    return _d

def getCount1(_d):
    count = 0
    for a in _d.keys():
        if _d[a] > 0:
            count += 1
    return count

def getCount2(_d, num):
    count = 0
    for a in _d.keys():
        if _d[a] == num:
            count += 1
    return count


f = open("input.txt", "r")
data = f.read().replace("\r","").split("\n\n")

count1 = 0
count2 = 0

for g in data:
    lines = g.splitlines()
    d = initDict()
    for l in lines:
        d = updateDict(d, l)
    count1 += getCount1(d)
    count2 += getCount2(d, len(lines))

print(count1)
print(count2)