import numpy as np

up = {'|': (-1, 0), '7': (0, -1), 'F': (0, 1)}
down = {'|': (1, 0), 'J': (0, -1), 'L': (0, 1)}
left = {'-': (0, -1), 'L': (-1, 0), 'F': (1, 0)}
right = {'-': (0, 1), 'J': (-1, 0), '7': (1, 0)}
directions = {(1, 0): down, (-1, 0): up, (0, -1): left, (0, 1): right}


def build_path(grid, start):
    current = start
    path = [start]

    for direction in directions:
        pipe_pos = [current[0] + direction[0], current[1] + direction[1]]
        if 0 <= pipe_pos[0] < grid.shape[0] and 0 <= pipe_pos[1] < grid.shape[
            1]:
            pipe = grid[pipe_pos[0]][pipe_pos[1]]
            if pipe in directions[direction]:
                current = pipe_pos
                current_dir = direction
                break

    while current != start:
        path += [current]
        pipe = grid[current[0], current[1]]
        current_dir = directions[current_dir][pipe]
        current = [current[0] + current_dir[0], current[1] + current_dir[1]]

    return path


def get_connection(node1, node2, connection):
    row_diff1 = connection[0] - node1[0]
    row_diff2 = connection[0] - node2[0]
    col_diff1 = connection[1] - node1[1]
    col_diff2 = connection[1] - node2[1]

    if row_diff1 == 0 and row_diff2 == 0:
        return '-'
    elif col_diff1 == 0 and col_diff2 == 0:
        return '|'
    elif (col_diff1 < 0 and row_diff2 < 0) or (
            col_diff2 < 0 and row_diff1 < 0):
        return 'F'
    elif (col_diff1 < 0 < row_diff2) or (col_diff2 < 0 < row_diff1):
        return 'L'
    elif (col_diff1 > 0 > row_diff2) or (col_diff2 > 0 > row_diff1):
        return '7'
    else:
        return 'J'


# Solution to Problem 1 #######################################################
def problem1(file_path):
    with open(file_path) as file:
        grid = np.array([list(line.strip()) for line in file.readlines()])
        start = np.where(grid == 'S')
        start = [start[0][0], start[1][0]]

        path = build_path(grid, start)

        return len(path) // 2


# Solution to Problem 2 #######################################################
def problem2(file_path):
    with open(file_path) as file:
        grid = np.array([list(line.strip()) for line in file.readlines()])
        start = np.where(grid == 'S')
        start = [start[0][0], start[1][0]]

        path = build_path(grid, start)
        grid[start[0], start[1]] = get_connection(path[1], path[-1], path[0])

        count = 0
        for i in range(grid.shape[0]):
            in_pipe = 'X'
            area = False
            for j in range(grid.shape[1]):
                if [i, j] in path:
                    # Change area context considering if we are in a
                    # horizontal pipe
                    if in_pipe == 'X' or in_pipe == grid[i, j]:
                        area = not area

                    # Update horizontal pipe context
                    if grid[i, j] == 'F':
                        in_pipe = '7'
                    elif grid[i, j] == 'L':
                        in_pipe = 'J'
                    elif grid[i, j] in '|7J' + in_pipe:
                        in_pipe = 'X'
                elif area:
                    count += 1
                    grid[i, j] = 'I'

        return count


###############################################################################

# File paths
test_path = "data/test10.txt"
input_path = "data/input10.txt"

# Execute the two problems
print("--- Tests ---")
print("Problem 1 test: ", problem1(test_path))
print("Problem 2 test: ", problem2(test_path))

# Execute the two problems solutions
print("\n--- Solutions ---")
print("Problem 1 result: ", problem1(input_path))
print("Problem 2 result: ", problem2(input_path))
