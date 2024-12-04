
file = "./inputs/day2"


def parse_input(input: str):
    output = []
    for line in input.splitlines():
        output.append([int(x) for x in line.split()])
    return output


with open(file, 'r') as f:
    s = f.read()
    data = parse_input(s)


def safety_check(levels: list[int]):
    diffs = [j - i for i, j in zip(levels, levels[1:])]
    pos = None
    for diff in diffs:
        if abs(diff) < 1 or abs(diff) > 3:
            return False
        if diff == 0:
            return False
        elif diff > 0:
            if pos == None:
                pos = True
            elif pos == False:
                return False
        else:
            if pos == None:
                pos = False
            elif pos == True:
                return False
    return True


def total_safety(reports: list[list[int]]):
    safe_reports = 0
    for r in reports:
        safe_reports += safety_check(r)
    return safe_reports


print(total_safety(data))


def safety_damped(levels: list[int]):
    if safety_check(levels) == True:
        return True
    for i in range(0, len(levels)):
        brute = levels[:i] + levels[(i+1):]
        if (safety_check(brute)):
            return True
    return False


def total_damped(reports: list[list[int]]):
    safe_reports = 0
    for r in reports:
        safe_reports += safety_damped(r)
    return safe_reports


print(total_damped(data))
