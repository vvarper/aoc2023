import numpy as np


def get_score(platform):
    total = 0

    rows = platform.shape[0]
    for i, j in np.ndindex(platform.shape):
        if platform[i, j] == 'O':
            total += rows - i

    return total


def north_tilt(platform):
    for i, j in np.ndindex(platform.shape):
        if platform[i, j] == 'O':
            k = max(i - 1, 0)
            platform[i, j] = '.'
            while k > 0 and platform[k, j] == '.':
                k -= 1

            if platform[k, j] == '.':
                platform[k, j] = 'O'
            else:
                platform[k + 1, j] = 'O'

    return platform


def cycle(platform):
    # North
    platform = north_tilt(platform)

    # West
    platform = north_tilt(platform.T).T

    # South
    platform = np.flip(platform, 0)
    platform = north_tilt(platform)
    platform = np.flip(platform, 0)

    # East
    platform = np.flip(platform, 1)
    platform = north_tilt(platform.T).T
    return np.flip(platform, 1)


# Solution to Problem 1 #######################################################
def problem1(file_path):
    with open(file_path) as file:
        platform = np.array([list(line.strip()) for line in file.readlines()])
        platform = north_tilt(platform)
        return get_score(platform)


# Solution to Problem 2 #######################################################
def problem2(file_path):
    with open(file_path) as file:
        platform = np.array([list(line.strip()) for line in file.readlines()])
        goal = 1000000000
        initial_cycles = 500

        # Trust that the platform reaches a stationary state after 500 cycles
        for i in range(initial_cycles):
            platform = cycle(platform)

        # Find the outer cycle
        previous_state = np.copy(platform)

        platform = cycle(platform)
        cycle_length = 1
        while not np.array_equal(platform, previous_state):
            platform = cycle(platform)
            cycle_length += 1

        remaining_cycles = (goal - initial_cycles) % cycle_length

        platform = previous_state
        for i in range(remaining_cycles):
            platform = cycle(platform)

        return get_score(platform)


###############################################################################

# File paths
test_path = "data/test14.txt"
input_path = "data/input14.txt"

# Execute the two problems
print("--- Tests ---")
print("Problem 1 test: ", problem1(test_path))
print("Problem 2 test: ", problem2(test_path))

# Execute the two problems solutions
print("\n--- Solutions ---")
print("Problem 1 result: ", problem1(input_path))
print("Problem 2 result: ", problem2(input_path))
