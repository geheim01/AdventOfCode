import itertools

adapters = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""

adapters1 = """16
10
15
5
1
11
7
19
6
12
4"""

#with open('input_10.txt', 'r') as f:
#    adapters = [int(i) for i in f.readlines()]

def part1():
    dev_adapter = max(adapters) + 3
    adapters.append(0)
    adapters.append(dev_adapter)
    adapters.sort()

    one_jolt = 0
    two_jolt = 0
    three_jolt = 0
    for i in range(1, len(adapters)):
        if adapters[i-1] + 1 == adapters[i]:
            one_jolt += 1
        elif adapters[i-1] + 2 == adapters[i]:
            two_jolt += 1
        elif adapters[i-1] + 3 == adapters[i]:
            three_jolt += 1

    solution = one_jolt * three_jolt
    print(one_jolt, three_jolt, solution)


adapters = [int(i) for i in adapters.splitlines()]
dev_adapter = max(adapters) + 3
adapters.append(0)
adapters.append(dev_adapter)
adapters.sort()
combinations = set()

for num in range(len(adapters)//3, len(adapters)+1):
    adapters_combinations = itertools.combinations(adapters, num)
    for c in adapters_combinations:
        combinations.add(c)


unvalid_combinations = set()

for combination in combinations:
    for i in range(1, len(combination)):
        prior_adapter = combination[i-1]
        current_adapter = combination[i]
        if prior_adapter + 1 != current_adapter and prior_adapter + 2 != current_adapter and prior_adapter + 3 != current_adapter:
            unvalid_combinations.add(combination)
            break
        if  dev_adapter not in combination:
            unvalid_combinations.add(combination)
            break
        if  0 not in combination:
            unvalid_combinations.add(combination)
            break

valid_combinations = combinations - unvalid_combinations

print(len(valid_combinations))