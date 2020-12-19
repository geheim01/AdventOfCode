test = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""


with open("09/09.txt", "r") as f:
    encrypt = f.read().split("\n")


def part1():
    unvalid = []

    for i in range(25, len(encrypt)):
        sumable = False
        sums = encrypt[i-25:i]
        for num1 in sums:
            for num2 in sums:
                num1 = int(num1)
                num2 = int(num2)
                if num1 != num2:
                    if num1 + num2 == int(encrypt[i]):
                        sumable = True
                        break
            if sumable is True:
                break
        if sumable is False:
            unvalid.append(encrypt[i])
            break
    print()
    return unvalid[0]


print(part1())


def part2():
    for i in range(len(encrypt)):
        num_of_sum = 1
        while num_of_sum < 20:
            sums = encrypt[i:i+num_of_sum+1]
            sums = [int(i) for i in sums]
            sum_of_list = sum(sums)
            if sum_of_list != 1721308972:
                num_of_sum += 1
            if sum_of_list == 1721308972:
                sums.sort()
                print(sums[0]+sums[-1])
                print(num_of_sum)
                break


part2()
