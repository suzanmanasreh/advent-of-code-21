def part1():
    file = open("day3/binary_diagnostic.py", "r")
    for line in file:
        digits = line.split()
        map_object = map(int, digits)
        list_of_digits = list(map_object)


        print(list_of_digits[0])

part1()