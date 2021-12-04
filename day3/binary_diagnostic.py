def part1():
    file = open("day3/binary_diagnostic.py", "r")
    for line in file:
        A = 1
        # create a digits list
        digits = []
        for i in range(0, len(line), A):
            # convert to int, after the slicing process
            digits.append(int(line[i : i + A]))
        print(digits[0])

part1()