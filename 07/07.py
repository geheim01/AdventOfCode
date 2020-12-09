import re

example = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags."""

#dark violet bags contain no other bags."""

with open("input_07.txt", "r") as f:
    text = f.read()

#pattern = r'((\w+)\s(\w+)\sbags)\scontain\s((\d)\s(\w+)\s(\w+)\s(bags?)|(no other bags))(\.)?(,\s(\d)\s(\w+)\s(\w+)\s(bags))*'
#pattern = r'(.*)\scontain\s(.+)'
pattern = r'((\w+ ){2})bag'
pattern_inner_bag = r'(\d) ((\w+ ){2})bag'


bag_dict = dict()

for line in example.split("\n"):
    bag = line.split("contain")[0]
    bag_contain = line.split("contain")[1].split(",")
    bag = re.search(pattern, bag).group(1)
    bag_dict[bag] = list()
    for i in bag_contain:
        content_number = re.search(pattern_inner_bag, i).group(1)
        content = re.search(pattern_inner_bag, i).group(2)
        if content is not None:
            bag_dict[bag].append({content:content_number})


for k, v in bag_dict.items():
    if len(v) != 0:
        print(k, v)
        for i in v:
            print(i)
            for ik, iv in i.items():
                print(ik, iv)
                if bag_dict[ik]:
                    print(bag_dict[ik])
                #bag_dict[k].append({ik:iv})

print(bag_dict)

count = 0
my_bag = "shiny gold "
for k, v in bag_dict.items():
    print(v)
    if my_bag in v:
        count += 1

print(count)