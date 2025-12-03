def GetMostCommonBit(data, bitNum):
    zeros = 0
    ones = 0
    for i in range(len(data)):
        if data[i][bitNum] == '0':
            zeros += 1
        else:
            ones += 1
    
    if zeros > ones:
        return 0
    elif ones > zeros:
        return 1
    else:
        return -1

def GetLeastCommonBit(data, bitNum):
    zeros = 0
    ones = 0
    for i in range(len(data)):
        if data[i][bitNum] == '0':
            zeros += 1
        else:
            ones += 1
    
    if zeros < ones:
        return 0
    elif ones < zeros:
        return 1
    else:
        return -1

def FilterList(data, bitNum, bitValue):
    newlist = []
    for d in data:
        if d[bitNum] == str(bitValue):
            newlist.append(d)
    return newlist

f = open("input.txt", "r")
data = f.read().strip()
data = data.replace("\r", "").split("\n")

Life = 0
O2data = data.copy()
CO2data = data.copy()

for b in range(len(data[0])):
    if len(O2data) > 1:
        common = GetMostCommonBit(O2data, b)
        if common == -1:
            common = 1
        print("filtering O2data: {}".format(O2data))
        O2data = FilterList(O2data, b, common)
        print("O2data = {}".format(O2data))
    if len(CO2data) > 1:
        common = GetLeastCommonBit(CO2data, b)
        if common == -1:
            common = 0
        CO2data = FilterList(CO2data, b, common)

print("{} -> {}".format(O2data[0], int(O2data[0], 2)))
print("{} -> {}".format(CO2data[0], int(CO2data[0], 2)))

print("{}".format(int(O2data[0], 2)*int(CO2data[0], 2)))
