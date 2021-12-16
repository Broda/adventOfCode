class Bag:
    def __init__(self, color, contents):
        self.color = color
        self.contents = contents

    def __str__(self):
        return "'{}':{}".format(self.color, self.contents)

class Node:
    def __init__(self, parent, bag, count, _rules):
        self.parent = parent
        self.bag = bag
        self.count = count
        self.addChildren(_rules)

    def __str__(self):
        c = ""
        for child in self.children:
            if len(c) > 0:
                c += ", "
            c += "{}x{}".format(child.count,child.bag.color)
        s = "{}, count: {}, children: [{}]".format(str(self.bag), self.count, c)
        return s

    def addChildren(self, _rules):
        self.children = []
        for r in self.bag.contents:
            num = r.split(" ")[0].strip()
            if num == "no":
                num = "0"
            num = int(num)
            color = r.replace(str(num) + " ", "")
            if "no other" in color:
                contents = ""
            else:
                contents = _rules[color]
            self.children.append(Node(self, Bag(color, contents), num, _rules))
    
    def printNode(self, prestring):
        s = prestring + str(self)
        print(s)
        for c in self.children:
            c.printNode(prestring + "-")
    
    def countChildren(self, initCount):
        count = initCount
        for c in self.children:
            count += c.count * c.countChildren(1)
        return count

f = open("input.txt", "r")
ruleText = f.readlines()
rules = {}

for r in ruleText:
    bag = r.split(" bags contain ")[0]
    rules[bag] = r.split(" bags contain ")[1].replace(".\n", "").replace("bags","bag").replace(" bag", "").replace(".","").split(", ")
    if rules[bag] == ['no other']:
        rules[bag] = []
    

def part1():
    find = "shiny gold"
    found = []
    for b in rules.keys():
        for r in rules[b]:
            if find in r:
                found.append(b)

    for f in found:
        for b in rules.keys():
            for r in rules[b]:
                if f in r and b not in found:
                    found.append(b)

    print(len(found))

def part2():
    root = Node(None, Bag("shiny gold", rules["shiny gold"]), 1, rules)

    #root.printNode("")

    print(root.countChildren(0))


part1()
part2()