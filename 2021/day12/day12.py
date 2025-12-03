f = open("sample.txt", "r")
data = f.read().strip()
data = data.replace("\r", "").split("\n")

map = {}

def tryAddNode(node, connNode):
    if node not in map.keys():
        map[node] = [connNode]
    elif connNode not in map[node]:
        map[node] += [connNode]

def find_all_paths(start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in map.keys():
        return []
    paths = []
    for node in map[start]:
        if node not in path:
            newpaths = find_all_paths(node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths
    
def print_path(p):
    line = ""
    for n in p:
        if len(line)>0:
            line += ','
        line += n
    print(line)

for line in data:
    nodes = line.split('-')
    tryAddNode(nodes[0],nodes[1])
    tryAddNode(nodes[1],nodes[0])

paths = find_all_paths('start', 'end')
# for p in paths:
#     print(p)
    
smalls = []
for n in map.keys():
    if n.islower():
        smalls.append(n)

visitable_smalls = []
for s in smalls:
    for n in map[s]:
        if n.isupper() and s not in visitable_smalls:
            visitable_smalls.append(s)

small_paths = []
for s in visitable_smalls:
    if s == 'start':
        continue
    lst = find_all_paths('start', s)
    for p in lst:
        ok = True
        for i in range(len(p)):
            if p[i] == 'end' and i < len(p)-1:
                ok = False
                break
        if ok and p not in small_paths:
            small_paths.append(p)

smalls_to_end = []
for p in small_paths:
    last = p[len(p)-1]
    if last != 'end':
        lst = find_all_paths(last, 'end')
        for l in lst:
            ok = True
            for i in range(len(l)):
                if l[i] == 'start':
                    ok = False
                    break
            if ok and l not in smalls_to_end:
                smalls_to_end.append(l)

final_paths = []
for s in small_paths:
    last = s[len(s)-1]
    if last == 'end':
        if s not in final_paths:
            final_paths.append(s)
        continue
    
    for e in smalls_to_end:
        if last == e[0]:
            l = s + e[1:]
            if l not in final_paths:
                final_paths.append(l)

new_final = []
for p in final_paths:
    t = []
    ok = True
    for n in p:
        if n in t and n.islower():
            ok = False
            break
        else:
            t.append(n)
    if ok and p not in new_final:
        new_final.append(p)

for p in new_final:
    print_path(p)

#print("map: {}".format(map))
#print("smalls: {}".format(smalls))
#print("visitable smalls: {}".format(visitable_smalls))

# for p in small_paths:
#     print(p)
# for p in smalls_to_end:
#     print(p)

### just need to figure out how to visit the nodes with doublebacks.... useless paths
        