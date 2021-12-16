f = open("input.txt", "r")
adapters = f.readlines()

for i in range(len(adapters)):
    adapters[i] = int(adapters[i])

adapters = sorted(adapters)
device = adapters[len(adapters)-1] + 3

def part1():
    counts = {1:0, 2:0, 3:1}
    counts[adapters[0]] += 1

    for i in range(len(adapters)-1):
        diff = adapters[i+1] - adapters[i]
        counts[diff] += 1

    print(counts)
    print(counts[1] * counts[3])

class Node:
    def __init__(self, alist, index):
        self.index = index
        self.value = alist[index]
        self.children = []
    
    def load_children(self, nodes):
        for i in range(self.index+1, self.index+4):
            if i > len(nodes)-1:
                break
            if nodes[i].value - self.value <= 3:
                self.children.append(nodes[i])

    def paths(self):
        if not self.children:
            return [[self.value]]  # one path: only contains self.value
        paths = []
        for child in self.children:
            for path in child.paths():
                paths.append([self.value] + path)
        return paths

    def parent_counts(self, nodes):
        count = 0
        for n in nodes:
            for c in n.children:
                if self.value == c.value:
                    count += 1
        return count
    
    def get_nodes(self, nodes):
        if self not in nodes:
            nodes.append(self)
        for c in self.children:
            if c not in nodes:
                c.get_nodes(nodes)

nodes = []

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:            
            memo[x] = f(x)
        return memo[x]
    return helper

@memoize
def path_counts(node):
    if not node.children:
        return node.parent_counts(nodes)
    count = 0
    for c in node.children:
        count += path_counts(c)
    return count

def part2():
    adapters.insert(0, 0)
    adapters.append(device)
    
    for a in range(len(adapters)):
        nodes.append(Node(adapters, a))
    for n in nodes:
        n.load_children(nodes)

    root = nodes[0]
    #print(len(nodes))
    #print(root.path_counts(nodes))
    print(path_counts(root))
    #print(len(root.paths()))

    return

#part1()
part2()