f = open("input.txt", "r")
items = f.readlines()
items.sort()

for i in range(len(items)):
    items[i] = int(items[i])

def part1():
    item1 = 0
    item2 = 0
    for i1 in range(len(items)):
        for i2 in range(i1+1, len(items)):
            if items[i1] + items[i2] == 2020:
                item1 = items[i1]
                item2 = items[i2]
    print("{} + {} = 2020, {} * {} = {}".format(item1, item2, item1, item2, item1*item2))

def part2():
    item1 = 0
    item2 = 0
    item3 = 0

    for i1 in range(len(items)):
        for i2 in range(i1+1, len(items)):
            for i3 in range(i1+2, len(items)):
                if items[i1] + items[i2] + items[i3] == 2020:
                    item1 = items[i1]
                    item2 = items[i2]
                    item3 = items[i3]

    print(str(item1) + ", " + str(item2) + ", " + str(item3))
    print(str(item1*item2*item3))

#part1()
part2()