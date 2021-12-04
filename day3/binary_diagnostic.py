# brute force solution for part 1
gamma = []
def part1():
    epsilon = ''
    first_bit_count = 0
    second_bit_count = 0
    third_bit_count = 0
    fourth_bit_count = 0
    fifth_bit_count = 0
    sixth_bit_count = 0
    seventh_bit_count = 0
    eighth_bit_count = 0
    ninth_bit_count = 0
    tenth_bit_count = 0
    eleventh_bit_count = 0
    twelvth_bit_count = 0
    with open("day3/inputs.txt") as file:
        mylist = file.read().splitlines()
        for i in mylist:
            digits = list(map(int, i))
            if(digits[0] == 0):
                first_bit_count += 1
            if(digits[1] == 0):
                second_bit_count += 1
            if(digits[2] == 0):
                third_bit_count += 1
            if(digits[3] == 0):
                fourth_bit_count += 1
            if(digits[4] == 0):
                fifth_bit_count += 1
            if(digits[5] == 0):
                sixth_bit_count += 1
            if(digits[6] == 0):
                seventh_bit_count += 1
            if(digits[7] == 0):
                eighth_bit_count += 1
            if(digits[8] == 0):
                ninth_bit_count += 1
            if(digits[9] == 0):
                tenth_bit_count += 1
            if(digits[10] == 0):
                eleventh_bit_count += 1
            if(digits[11] == 0):
                twelvth_bit_count += 1
        if first_bit_count > 500:
            gamma.append('0')
        else:
            gamma.append('1')
        if second_bit_count > 500:
            gamma.append('0')
        else:
            gamma.append('1')
        if third_bit_count > 500:
            gamma.append('0')
        else:
            gamma.append('1')
        if fourth_bit_count > 500:
            gamma.append('0')
        else:
            gamma.append('1')
        if fifth_bit_count > 500:
            gamma.append('0')
        else:
            gamma.append('1')
        if sixth_bit_count > 500:
            gamma.append('0')
        else:
            gamma.append('1')
        if seventh_bit_count > 500:
            gamma.append('0')
        else:
            gamma.append('1')
        if eighth_bit_count > 500:
            gamma.append('0')
        else:
            gamma.append('1')
        if ninth_bit_count > 500:
            gamma.append('0')
        else:
            gamma.append('1')
        if tenth_bit_count > 500:
            gamma.append('0')
        else:
            gamma.append('1')
        if eleventh_bit_count > 500:
            gamma.append('0')
        else:
            gamma.append('1')
        if twelvth_bit_count > 500:
            gamma.append('0')
        else:
            gamma.append('1')
    print(gamma)
    gammaString = ''
    for i in gamma:
        gammaString += i
    print(int(gammaString, 2))

def part2():
    oxygen_generator_rating = []
    data_list = []
    with open("day3/inputs.txt") as file:
        for line in file:
            data_list.append(line.strip())
        numbers = data_list.copy
        data_size = len(data_list[0])
        for i in range(data_size):
            sorted_nums = []
            zeros = 0
            ones = 0
            for data in numbers:
                if int(data[i]) == 1:
                    ones += 1
                else:
                    zeros +=1
            most_common_oxygen = 0
            most_common_co2 = 0
            if ones >= zeros:
                most_common_oxygen = 1
                most_common_co2 = 0
            else:
                most_common_oxygen = 0
                most_common_co2 = 1
            for data in numbers:
                if int(data[i] == most_common_oxygen):
                    sorted_nums.append(data)
            numbers = sorted_nums.copy()
            if len(numbers) == 1:
                print(strToInt(numbers[0]))


def strToInt(stringNumber):
	value = 0
	posCount = 0
	for s in stringNumber:
		posCount += 1
		value += int(s)*2**(len(stringNumber)-posCount)
	return value
                
            



part2()