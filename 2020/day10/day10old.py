
class Node:
    def __init__(self, val, _adapters):
        self.val = val
        self.children = []
        for a in _adapters:
            if a - self.val >= 1 and a - self.val <= 3:
                self.children.append(Node(a, _adapters))
        
    def __str__(self) -> str:
        return "{}: [{}]".format(self.val, self.getChildrenString())

    def getChildrenString(self):
        s = ""
        for c in self.children:
            if len(s) > 0:
                s += ","
            s += str(c.val)
        return s

    def printNode(self):
        print(self)
        for c in self.children:
            c.printNode()

f = open("sample.txt", "r")
adapters = f.readlines()
for i in range(len(adapters)):
    adapters[i] = int(adapters[i].strip())
adapters.sort()

root = Node(0, adapters)

root.printNode()