import re
from functools import reduce


# Solution to Problem 1 #######################################################
def problem1(file_path):
    max_dict = {'red': 12, 'green': 13, 'blue': 14}
    with open(file_path) as file:
        num_possibles = 0
        for line in file:
            game = line.split(":")
            sets = [a.strip().split() for a in re.split('[,;]', game[1])]
            incr = 0 if any(
                [int(i[0]) > max_dict[i[1]] for i in sets]) else int(
                game[0].split()[1])
            num_possibles += incr

    return num_possibles


# Solution to Problem 2 #######################################################
def problem2(file_path):
    with open(file_path) as file:
        sum_of_powers = 0
        for line in file:
            min_dict = {'red': 0, 'green': 0, 'blue': 0}
            game = line.split(":")
            sets = [a.strip().split() for a in re.split('[,;]', game[1])]

            for i in sets:
                min_dict[i[1]] = max(min_dict[i[1]], int(i[0]))

            sum_of_powers += reduce(lambda x, y: x * y, min_dict.values())

    return sum_of_powers


###############################################################################

# File paths
test_path = "data/test02.txt"
input_path = "data/input02.txt"

# Execute the two problems
print("--- Tests ---")
print("Problem 1 test: ", problem1(test_path))
print("Problem 2 test: ", problem2(test_path))

# Execute the two problems solutions
print("\n--- Solutions ---")
print("Problem 1 result: ", problem1(input_path))
print("Problem 2 result: ", problem2(input_path))
