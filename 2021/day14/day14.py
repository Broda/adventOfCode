
from functools import lru_cache
from collections import Counter

f = open("input.txt", "r")
data = f.read().strip()
data = data.replace("\r", "").split("\n")

template = data[0]
rules = dict(map(lambda r: r.split(' -> '), data[2:]))

def test(polymer, steps):
    @lru_cache(maxsize=None)
    def count(pair, step):
        if step == steps or pair not in rules:
            return Counter()
        step += 1
        ctr = Counter(rules[pair])
        ctr.update(count(pair[0] + rules[pair], step))
        ctr.update(count(rules[pair] + pair[1], step))
        return ctr
    
    counter = Counter(polymer)
    for letter1, letter2 in zip(polymer, polymer[1:]):
        counter.update(count(letter1+letter2, 0))
    return counter

def getPart1Answer(polymer):
    ctr = test(polymer, 10)
    ctr_sorted = ctr.most_common()
    return ctr_sorted[0][1] - ctr_sorted[-1][1]

def getPart2Answer(polymer):
    ctr = test(polymer, 40)
    ctr_sorted = ctr.most_common()
    return ctr_sorted[0][1] - ctr_sorted[-1][1]

poly = template

print(getPart1Answer(poly))
print(getPart2Answer(poly))