from collections import defaultdict

file = "./inputs/day5"
with open(file, 'r') as f:
    s = f.read()
    rulestext, updatestext = s.split('\n\n')

rules = defaultdict(set)
for rule in rulestext.splitlines():
    before, after = rule.split('|')
    rules[before].add(after)


def flatten(update):
    visited = set()
    stack = []

    def dfs(node):
        if node not in visited:
            visited.add(node)
            for child in rules[node]:
                if child in update:
                    dfs(child)
            stack.append(node)

    for node in update:
        dfs(node)
    return stack[::-1]


total_middles = 0
fixed_middles = 0
for update in updatestext.splitlines():
    u = update.split(',')
    good_list = True
    bad = set()
    for value in reversed(u):
        if value in bad:
            good_list = False
            break
        bad.update(rules[value])
    if good_list:
        total_middles += int(u[len(u)//2])
    else:
        fixed = flatten(u)
        fixed_middles += int(fixed[len(fixed)//2])

print(f"{total_middles=}")
print(f"{fixed_middles=}")
