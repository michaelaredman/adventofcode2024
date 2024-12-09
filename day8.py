from collections import defaultdict
file = "./inputs/day8"
with open(file, 'r') as f:
    s = f.read()

grid = [list(line) for line in s.splitlines()]


def find_antenna(grid: list[list[chr]]):
    antenna = defaultdict(list)
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] != '.':
                antenna[grid[r][c]].append((r, c))
    return antenna


class Field:

    def __init__(self, grid: list[list[chr]]):
        self.grid = grid
        self.antennae = find_antenna(grid)
        self.rows, self.columns = len(grid), len(grid[0])

    def _check_bounds(self, loc):
        return 0 <= loc[0] < self.rows and 0 <= loc[1] < self.columns

    def find_antinodes(self):
        self.antinodes = set()
        for freq, locations in self.antennae.items():
            for i in range(0, len(locations) - 1):
                for j in range(i + 1, len(locations)):
                    l1, l2 = locations[i], locations[j]
                    if self._check_bounds((2*l2[0] - l1[0], 2*l2[1] - l1[1])):
                        self.antinodes.add((2*l2[0] - l1[0], 2*l2[1] - l1[1]))
                    if self._check_bounds((2*l1[0] - l2[0], 2*l1[1] - l2[1])):
                        self.antinodes.add((2*l1[0] - l2[0], 2*l1[1] - l2[1]))
        return self.antinodes

    def harmonic_antinodes(self):
        self.antinodes = set()
        for freq, locations in self.antennae.items():
            for i in range(0, len(locations) - 1):
                for j in range(i + 1, len(locations)):
                    l1, l2 = locations[i], locations[j]
                    diff = (l1[0] - l2[0], l1[1] - l2[1])
                    node = (l1[0], l1[1])
                    while self._check_bounds(node):
                        self.antinodes.add(node)
                        node = (node[0] + diff[0], node[1] + diff[1])
                    node = (l1[0], l1[1])
                    while self._check_bounds(node):
                        self.antinodes.add(node)
                        node = (node[0] - diff[0], node[1] - diff[1])
        return self.antinodes


# for each freq
# for each pair of ants (i = 0 -> n - 2, j = i + 1 -> n-1)
# calculate diff
# add diff to one adn subtract from the other
# if in the grid bounds, add to a list of coords or dict (check problem)
field = Field(grid)
antinodes = field.find_antinodes()
print(f"{len(antinodes)=}")

harmonic_antinodes = field.harmonic_antinodes()
print(f"{len(harmonic_antinodes)=}")
