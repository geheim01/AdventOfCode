import collections

with open("input_06.txt", "r") as f:
    custom_forms = f.read()

str = """abc

a
b
c

ab
ac

a
a
a
a

b"""

def part1(custom_forms):
    groups_ugly = custom_forms.split("\n\n")
    groups_clean = [x.replace("\n", "") for x in groups_ugly]
    overall_counter = 0

    for report in groups_clean:
        group_counter = 0
        group_letters = []
        for letter in report:
            if letter not in group_letters:
                group_counter += 1
                group_letters.append(letter)
        overall_counter += group_counter
    print(overall_counter)

def part2(custom_forms):
    
    groups = custom_forms.split("\n\n")
    overall_counter = 0
    for report in groups:
        group_size = 1
        group_counter = 0
        group_letters = []
        for person in report:
            for letter in person:
                if letter == "\n":
                    group_size += 1
                group_letters.append(letter)
        frequency = collections.Counter(group_letters)
        for k, v in frequency.items():
            if v == group_size:
                group_counter += 1
        overall_counter += group_counter
    print(overall_counter)

#part1(custom_forms)
#part2(custom_forms)
