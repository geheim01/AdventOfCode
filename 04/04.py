# Day 4
import re
import time

start_time = time.time()


with open("/Users/Nils/Projekte/AdventOfCode/04/input_04.txt", "r") as f:
    f = f.read()

byr = 'byr:(19[2-8][0-9]|199[0-9]|200[0-2])'
iyr = 'iyr:(201[0-9]|2020)'
eyr = 'eyr:(202[0-9]|2030)'
hgt = 'hgt:((1[5-8][0-9]|19[0-3])cm)|((59|6[0-9]|7[0-6])in)'
hcl = 'hcl:#[0-9a-f]{6}'
ecl = 'ecl:(amb|blu|brn|gry|grn|hzl|oth)'
pid = 'pid:[0-9]{9}\\b'
cid = 'cid:\d{3}'

passport = f.split("\n\n")
counter = 0

for i in passport:
    if re.search(byr, i) is None:
        continue
    if re.search(iyr, i) is None:
        continue
    if re.search(eyr, i) is None:
        continue
    if re.search(hgt, i) is None:
        continue
    if re.search(hcl, i) is None:
        continue
    if re.search(ecl, i) is None:
        continue
    if re.search(pid, i) is None:
        continue
    counter += 1

print(counter)

print("--- %s seconds ---" % (time.time() - start_time))