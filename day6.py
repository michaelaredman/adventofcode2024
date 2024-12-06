from collections import defaultdict
file = "./inputs/day6"
grid = [list(line)
        for line in open(file, 'r').read().splitlines()]

# 1740 too high
# 1688 is correct


def find_start(grid: list[list[chr]]) -> tuple[int]:
    for r in range(len(grid)):
        for c in range(len(grid)):
            if (grid[r][c] == '^'):
                return (r, c)


the_start = find_start(grid)


def walk(grid: list[list[chr]]):
    r, c = the_start
    visited = {(r, c)}
    dir = (-1, 0)
    turn = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}
    while True:
        new_r, new_c = r + dir[0], c + dir[1]
        if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]):
            if grid[new_r][new_c] == '#':
                dir = turn[dir]
            else:
                r, c = new_r, new_c
                visited.add((r, c))
        else:
            return len(visited)


def find_states(grid: list[list[chr]]):
    r, c = the_start
    dir = (-1, 0)
    obstacles = set()
    turn = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}
    while True:
        new_r, new_c = r + dir[0], c + dir[1]
        if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]):
            if grid[new_r][new_c] == '#':
                dir = turn[dir]
            else:
                potential_obstacle = find_loops(grid, (r, c), dir)
                if potential_obstacle != (-1, -1):
                    obstacles.add(potential_obstacle)
                r, c = new_r, new_c
        else:
            if find_start(grid) in obstacles:
                print("We have the start")
            return len(obstacles)


print(walk(grid))


def find_loops(grid: list[list[chr]], pos: tuple[int], dir):
    new_obstacle = (pos[0] + dir[0], pos[1] + dir[1])
    r, c = the_start
    dir = (-1, 0)
    turn = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}
    state = {(r, c, dir[0], dir[1])}
    while True:
        new_r, new_c = r + dir[0], c + dir[1]
        if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]):
            if grid[new_r][new_c] == '#' or (new_r, new_c) == new_obstacle:
                dir = turn[dir]
            else:
                r, c = new_r, new_c
                if (r, c, dir[0], dir[1]) in state:
                    return new_obstacle
                state.add((r, c, dir[0], dir[1]))
        else:
            return (-1, -1)


def find_loops2(grid: list[list[chr]], pos: tuple[int], dir):
    new_obstacle = (pos[0] + dir[0], pos[1] + dir[1])
    r, c = the_start
    turn = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}
    visited = defaultdict(int)
    visited[(r, c)] = 0
    while True:
        new_r, new_c = r + dir[0], c + dir[1]
        if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]):
            if grid[new_r][new_c] == '#' or (new_r, new_c) == new_obstacle:
                dir = turn[dir]
            else:
                r, c = new_r, new_c
                visited[(r, c)] += 1
                if (visited[(r, c)] > 6):
                    return new_obstacle
        else:
            return (-1, -1)


def print_grid(grid, obstacles):
    for i in range(len(grid[0])):
        for j in range(len(grid[1])):
            if (i, j) in obstacles:
                print('O', end='')
            else:
                print(grid[i][j], end='')
        print()


print(f"{find_states(grid)=}")
