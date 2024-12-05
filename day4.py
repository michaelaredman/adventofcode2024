
ds = [(0, 1), (1, 0), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1), (1, 1)]


def search_grid(grid: list[list[chr]]):
    count = 0
    rows, columns = len(grid), len(grid[0])

    def step(grid: list[list[chr]], letter: chr, pos: tuple[int], dir):
        nonlocal count
        target = {'X': 'M', 'M': 'A', 'A': 'S'}[letter]
        new_pos = (pos[0] + dir[0], pos[1] + dir[1])
        if 0 <= new_pos[0] < rows and 0 <= new_pos[1] < columns:
            if grid[new_pos[0]][new_pos[1]] == target:
                if target == 'S':
                    count += 1
                else:
                    step(grid, target, new_pos, dir)

    for r in range(rows):
        for c in range(columns):
            if grid[r][c] == 'X':
                for d in ds:
                    step(grid, 'X', (r, c), d)
    return count


file = "./inputs/day4"
with open(file, 'r') as f:
    s = f.read()
    grid = []
    for line in s.splitlines():
        grid.append(list(line))
    print('count = ', search_grid(grid))


def count_crosses(grid: list[list[chr]]):
    count = 0
    rs, cs = len(grid), len(grid[0])
    target = {'M', 'S'}
    for r in range(rs):
        for c in range(cs):
            if grid[r][c] == 'A':
                if r + 1 < rs and c + 1 < cs and 0 <= r - 1 and 0 <= c - 1:
                    if {grid[r-1][c-1], grid[r+1][c+1]} == target and {grid[r+1][c-1], grid[r-1][c+1]} == target:
                        count += 1
    return count


with open(file, 'r') as f:
    s = f.read()
    grid = []
    for line in s.splitlines():
        grid.append(list(line))
    print('x-mas count = ', count_crosses(grid))
