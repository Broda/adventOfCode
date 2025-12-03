f = open("input.txt", "r")
data = f.read().strip()
data = data.replace("\r", "").split("\n")

gamma = ""
epsilon = ""

for b in range(len(data[0])):
    zeros = 0
    ones = 0
    for i in range(len(data)):
        if data[i][b] == '0':
            zeros += 1
        else:
            ones += 1

    if zeros > ones:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

print("gamma: {} = {}".format(gamma, int(gamma, 2)))
print("epislon: {} = {}".format(epsilon, int(epsilon, 2)))
print("power = {}".format(int(gamma, 2) * int(epsilon,2)))

