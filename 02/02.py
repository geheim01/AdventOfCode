# Part 1
def part1(input_file):
    overall_counter = 0
    for line in input_file:
        policy = line.split(":")[0]
        password = line.split(": ")[1][:-1]
        num = policy.split(" ")[0]
        constraint_letter = policy.split(" ")[1]
        left_bound = int(num.split("-")[0])
        right_bound = int(num.split("-")[1])
        counter = 0
        for letter in password:
            if letter == constraint_letter:
                counter += 1
        if counter in range(left_bound, right_bound+1):
            print(
                f'{password} is a valid password, because the constraint {policy} is matched.')
            overall_counter += 1
    print(f'{overall_counter} Passwords are valid!')


# Part 2
def part2(input_file):
    overall_counter = 0
    for line in input_file:
        policy = line.split(":")[0]
        password = line.split(": ")[1][:-1]
        num = policy.split(" ")[0]
        constraint_letter = policy.split(" ")[1]
        left_num = int(num.split("-")[0]) - 1
        right_num = int(num.split("-")[1]) - 1
        if (password[left_num] == constraint_letter) ^ (password[right_num] == constraint_letter):
            overall_counter += 1
            print(
                f'{password} is a valid password, because the constraint {policy} is matched.')
            print(line[left_num], line[right_num])
    print(overall_counter)


with open("02_input.txt", "r") as f:
    input_file = f.readlines()
    part2(input_file)
