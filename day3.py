import re

expr = "mul\((\d{1,3}),(\d{1,3})\)"

example = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

z = re.findall(expr, example)

total = 0
for x, y in z:
    total += int(x) * int(y)
print(total)


def find_total(s: str):
    expr = "mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(expr, s)
    total = 0
    for x, y in matches:
        total += int(x)*int(y)
    return total


with open('./inputs/day3', 'r') as f:
    s = f.read()
    print(find_total(s))


def complex_total(s: str):
    expr = "mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\)"
    matches = re.finditer(expr, s)
    do = True
    total = 0
    for match in matches:
        if do:
            if match.group(0).startswith("mul"):
                total += int(match.group(1))*int(match.group(2))
            elif match.group(0) == "don\'t()":
                do = False
        else:
            if match.group(0) == 'do()':
                do = True
    return total


with open('./inputs/day3', 'r') as f:
    s = f.read()
    print(complex_total(s))
