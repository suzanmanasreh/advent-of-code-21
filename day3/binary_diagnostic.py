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
    # i'm not writing code to conver binary to decimal
    # just use an online calculator

def part2():
    oxygen_generator_rating = []
    with open("day3/inputs.txt") as file:
        mylist = file.read().splitlines()
        for i in mylist:
            n = 0
            match = False
            digits = list(map(int, i))
            for num in gamma:
                if n == 10:
                    break
                    match = True
                if digits[n] == num:
                    n += 1
                    continue
                else:
                    break
            if match == True:
                oxygen_generator_rating = digits
                print(digits)
            print(match)
            """ if int(digits[0]) == int(gamma[0]):
                if digits[1] == gamma[1]:
                    if digits[2] == gamma[2]:
                        if digits[3] == gamma[3]:
                            if digits[4] == gamma[4]:
                                if digits[5] == gamma[5]:
                                    if digits[6] == gamma[6]:
                                        if digits[7] == gamma[7]:
                                            if digits[8] == gamma[8]:
                                                if digits[9] == gamma[9]:
                                                    if digits[10] == gamma[10]:
                                                        if digits[11] == gamma[11]:
                                                            if digits[12] == gamma[12]:
                                                                print(digits)
 """
        print(oxygen_generator_rating)


part2()