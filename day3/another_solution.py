with open("day3/inputs.txt") as f:
    data = [x for x in f.read().split()]

gamma = ""
epsilon = ""

for b in range(0, len(data[0])):
    one = 0
    zero = 0
    for c in range(0, len(data)):
        if data[c][b] == '0':
            zero += 1
        else:
            one += 1
    if zero > one: 
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

g = int(gamma, 2)
e = int(epsilon, 2)
print("part 1: ", g*e)


data2 = data.copy()
index = 0
while len(data) > 1:
    one = 0
    zero = 0
    ones = []
    zeroes = []
    for c in range(0, len(data)):
        if data[c][index] == '0':
            zero += 1
            zeroes.append(data[c])
        else:
            one += 1
            ones.append(data[c])
    if zero > one: 
        data = zeroes
    else:
        data = ones
    index += 1

oxygen = int(data[0], 2)

data = data2
index = 0
while len(data) > 1:
    one = 0
    zero = 0
    ones = []
    zeroes = []
    for c in range(0, len(data)):
        if data[c][index] == '0':
            zero += 1
            zeroes.append(data[c])
        else:
            one += 1
            ones.append(data[c])
    if one < zero: 
        data = ones
    else:
        data = zeroes
    index += 1

co2 = int(data[0], 2)
print("part 2:", oxygen * co2)
