def part1():
    file = open("day2/inputs.txt", "r")
    horizontalPos = 0
    depth = 0
    for line in file:
        command = line.split(" ")[0]
        value = line.split(" ")[1]
        if command == "forward":
            horizontalPos += int(value)
        elif command == "up":
            depth -= int(value)
        elif command == "down":
            depth += int(value)
    print(horizontalPos * depth)

def part2():
    file = open("day2/inputs.txt", "r")
    horizontalPos = 0
    depth = 0
    aim = 0
    for line in file:
        command = line.split(" ")[0]
        value = line.split(" ")[1]
        if command == "forward":
            horizontalPos += int(value)
            depth += (aim * int(value))
        elif command == "up":
            aim -= int(value)
        elif command == "down":
            aim += int(value)
    print(horizontalPos * depth)


part1()
part2()