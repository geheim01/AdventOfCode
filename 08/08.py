import re
test = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""


def part1():
    with open("input_08.txt", "r") as f:
        operations = f.read().split("\n")

    global_acc = 0
    i = 0
    visited_indices = []
    #operations = test.split("\n")
    while i < len(operations):
        if i in visited_indices:
            break
        else:
            visited_indices.append(i)
            op = operations[i].split(" ")[0]
            count = int(operations[i].split(" ")[1].replace("+", ""))
            if op == "acc":
                global_acc += count
                # print("acc")
            if op == "jmp":
                i += count
                continue
        i += 1
    print(global_acc)


def part2():

    with open("08/input_08.txt", "r") as f:
        operations_test = f.read().split("\n")
    global_acc = 0
    i = 0
    j = 0
    #visited_indices = []
    #operations_test = test.split("\n")
    ops = []

    for o in operations_test:
        ops.append(o.split(" ")[0])

    while j < len(ops):
        visited_indices = []
        #global_acc = 0
        ops_copy = ops.copy()
        if ops_copy[j] == "nop":
            ops_copy[j] = "jmp"
        elif ops_copy[j] == "jmp":
            ops_copy[j] = "nop"
        while i < len(operations_test):
            if i in visited_indices:
                i = 0
                global_acc = 0
                break
            else:
                visited_indices.append(i)
                op = ops_copy[i]
                count = int(operations_test[i].split(" ")[1].replace("+", ""))
                if op == "acc":
                    global_acc += count
                    # print("acc")
                if op == "jmp":
                    i += count
                    continue
                i += 1
        j += 1
    print(global_acc)


part2()
