#part 1 = 80 days
#part 2 = 256 days
DAYS = 256

f = open("input.txt", "r")
data = f.read().strip()
data = data.replace("\r", "").split("\n")

fish = data[0].split(',')
fish = [int(x) for x in fish]

days = [0 for x in range(9)]
for f in fish:
    days[f] += 1

for i in range(DAYS):
    newdays = [0 for x in range(9)]
    for d in range(8,0,-1):
        newdays[d-1] = days[d]
    newdays[6] += days[0]
    newdays[8] = days[0]
    days = newdays.copy()

sum = 0
for d in days:
    sum += d

print(sum)
