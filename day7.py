import itertools


def parse_line(line: str):
    target, nums = line.split(': ')
    nums = [int(x) for x in nums.split(' ')]
    target = int(target)
    return target, nums


def possible(target: int, nums: list[int]):
    for comb in range(0, 2**(len(nums) - 1) + 1):
        total = nums[0]
        for i in range(1, len(nums)):
            total = total * nums[i] if comb & (1 << i - 1) else total + nums[i]
        if total == target:
            return True
    return False


file = "./inputs/day7"
with open(file, 'r') as f:
    s = f.read()

total = 0
for line in s.splitlines():
    target, nums = parse_line(line)
    p = possible(target, nums)
    if p:
        total += target
print(f"{total=}")


def possible_complex(target: int, nums: list[int]):

    for comb in itertools.product(range(3), repeat=len(nums) - 1):
        total = nums[0]
        for i in range(1, len(nums)):
            match comb[i-1]:
                case 0:
                    total += nums[i]
                case 1:
                    total *= nums[i]
                case 2:
                    total = int(str(total) + str(nums[i]))
                case _:
                    assert False
        if total == target:
            return True
    return False


total_complex = 0
for line in s.splitlines():
    target, nums = parse_line(line)
    p = possible_complex(target, nums)
    if p:
        total_complex += target
print(f"{total_complex=}")
