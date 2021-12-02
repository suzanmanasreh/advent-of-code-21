def part1():
    sub_file = open("day1/inputs.txt", 'r')
    depth = 0
    count = -1
    for line in sub_file:
        if int(line) > depth:
            count += 1
        depth = int(line)

    print("part 1: %d" %count)

def part2():
    count = -1
    previous = -1
    with open('day1/inputs.txt') as file:
        measurements = [int(i) for i in file.readlines()]
    for j, depth in enumerate(measurements[0:-2]):
        sum = depth + measurements[j + 1] + measurements[j + 2]
        if sum > previous:
            count += 1
        previous = sum
    print("part 2: %d " %count)


part1()
part2()