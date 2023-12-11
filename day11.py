import numpy as np


def get_sum_of_distances_between_galaxies(universe, expand_factor):
    galaxies_positions = []
    universe_i = 0
    for i in range(universe.shape[0]):
        universe_j = 0
        for j in range(universe.shape[1]):
            if universe[i][j] == '#':
                galaxies_positions += [(universe_i, universe_j)]

            if len(universe[:, j]) == universe[:, j].tolist().count('.'):
                universe_j += expand_factor
            else:
                universe_j += 1

        if len(universe[i]) == universe[i].tolist().count('.'):
            universe_i += expand_factor
        else:
            universe_i += 1

    total_distance = 0
    for i in range(len(galaxies_positions)):
        for j in range(i + 1, len(galaxies_positions)):
            total_distance += abs(
                galaxies_positions[i][0] - galaxies_positions[j][0]) + abs(
                galaxies_positions[i][1] - galaxies_positions[j][1])

    return total_distance


# Solution to Problem 1 #######################################################
def problem1(file_path):
    with open(file_path) as file:
        universe = np.array([list(line.strip()) for line in file.readlines()])
        return get_sum_of_distances_between_galaxies(universe, 2)


# Solution to Problem 2 #######################################################
def problem2(file_path):
    with open(file_path) as file:
        universe = np.array([list(line.strip()) for line in file.readlines()])
        return get_sum_of_distances_between_galaxies(universe, 1000000)


###############################################################################

# File paths
test_path = "data/test11.txt"
input_path = "data/input11.txt"

# Execute the two problems
print("--- Tests ---")
print("Problem 1 test: ", problem1(test_path))
print("Problem 2 test: ", problem2(test_path))

# Execute the two problems solutions
print("\n--- Solutions ---")
print("Problem 1 result: ", problem1(input_path))
print("Problem 2 result: ", problem2(input_path))
