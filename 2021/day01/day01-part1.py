f = open("input-part1.txt", "r")
data = f.read().strip()
data = data.replace("\r", "").split("\n")

count = 0
for i in range(len(data)-1):
    if int(data[i+1]) > int(data[i]):
        print("{} > {}".format(data[i+1], data[i]))
        count += 1

print(count)