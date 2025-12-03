def checkIndex(_data, _pre, _index):
    num = int(_data[_index])
    start = _index - _pre
    #print("index = {}, num = {}, start = {}".format(_index, num, start))
    for i in range(start, _index):
        for j in range(start, _index):
            if i != j and int(_data[i]) != int(_data[j]):
                if int(_data[i]) + int(_data[j]) == num:
                    #print("{} + {} == {}".format(_data[i], _data[j], num))
                    return True
    
    return False
    
def findSum(_data, _invalid, _start_index, _end_index):
    numbers = []
    for i in range(_start_index, _end_index):
        numbers.append(int(_data[i]))
        if len(numbers) < 2:
            continue
        s = sum(numbers)
        if s == _invalid:
            return (True, numbers)

        if s < _invalid:
            continue

        if s > _invalid:
            while (len(numbers) >= 2):
                numbers.pop(0)
                s = sum(numbers)
                if s == _invalid:
                    return (True, numbers)
                if s < _invalid:
                    break

    if sum(numbers) == _invalid:
        return (True, numbers)
    else:
        return (False, None)

f = open("input.txt", "r")
data = f.read().strip()
data = data.replace("\r", "").split("\n")
preamble = 25

invalid = -1
invalid_index = -1

for i in range(preamble, len(data)):
    if not checkIndex(data, preamble, i):
        invalid = int(data[i])
        invalid_index = i
        break

print("{}: {}".format(invalid_index, invalid))
nums = findSum(data, invalid, 0, invalid_index)
blah = []
if nums[0]:
    blah = nums[1]
else:
    nums = findSum(data, invalid, invalid_index+1, len(data))
    if nums[0]:
        blah = nums[1]

blah.sort()
print(blah)
if len(blah) > 0:
    first = int(blah[0])
    last = len(blah)-1
    last = int(blah[last])
    print(first+last)
else:
    print("empty list")
