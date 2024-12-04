from collections import defaultdict
file = "./inputs/day1"


def read_input(input: str):
    two_lists = [[], []]
    for line in input.splitlines():
        one, two = [int(x) for x in line.split()]
        two_lists[0].append(one)
        two_lists[1].append(two)
    return two_lists


with open(file, 'r') as f:
    input = f.read()
    data = read_input(input)


def sortID(lists: list[list]):
    for l in lists:
        l.sort()


def total_distance(lists: list[list]):
    result = 0
    sortID(lists)
    for id1, id2 in zip(*lists):
        result += abs(id1 - id2)
    return result


print(total_distance(data))


def similarity_score(two_lists: list[list]):
    count = defaultdict(int)
    for id in two_lists[1]:
        count[id] += 1
    score = 0
    for id in two_lists[0]:
        score += id * count[id]
    return score


print(similarity_score(data))
