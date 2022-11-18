
f = open("sample.txt", "r")
data = f.read().strip()
data = data.replace("\r", "").split("\n")

costs = {'A':1,'B':10,'C':100,'D':1000}
moves = []
