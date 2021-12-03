def part1():
    file = open("day2/inputs.txt", "r")
    horizontalPos = 0
    depth = 0
    for line in file:
        parts = line.split(" ")
        if parts[0] == "forward":
            horizontalPos += int(parts[1])
        elif parts[0] == "up":
            depth -= int(parts[1])
        elif parts[0] == "down":
            depth += int(parts[1])
    print(horizontalPos * depth)

def part2():
    file = open("day2/inputs.txt", "r")
    horizontalPos = 0
    depth = 0
    aim = 0
    for line in file:
        parts = line.split(" ")
        if parts[0] == "forward":
            horizontalPos += int(parts[1])
            depth += (aim * int(parts[1]))
        elif parts[0] == "up":
            aim -= int(parts[1])
        elif parts[0] == "down":
            aim += int(parts[1])
    print(horizontalPos * depth)


part1()
part2()