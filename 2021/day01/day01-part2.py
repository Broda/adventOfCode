f = open("input.txt", "r")
data = f.read().strip()
data = [int(d) for d in data.replace("\r", "").split("\n")]

groups = []
for i in range(len(data)-2):
    groups.append(data[i] + data[i+1] + data[i+2])

count = 0    
for i in range(len(groups)-1):
    if groups[i+1] > groups[i]:
        count += 1
print(count)