# Solution to Problem 1 #######################################################
def problem1(file_path):
    with open(file_path) as file:
        histories = [list(map(int, line.strip().split())) for line in
                     file.readlines()]
        count = 0

        for history in histories:
            diffs = history.copy()

            while not all([diff == 0 for diff in diffs]):
                count += diffs[-1]
                diffs = [diffs[i + 1] - diffs[i] for i in
                         range(len(diffs) - 1)]

        return count


# Solution to Problem 2 #######################################################
def problem2(file_path):
    with open(file_path) as file:
        histories = [list(map(int, line.strip().split())) for line in
                     file.readlines()]
        count = 0

        for history in histories:
            diffs = history.copy()
            factor = -1
            current_factor = 1

            while not all([diff == 0 for diff in diffs]):
                count += diffs[0] * current_factor
                current_factor *= factor
                diffs = [diffs[i + 1] - diffs[i] for i in
                         range(len(diffs) - 1)]

        return count


###############################################################################

# File paths
test_path = "data/test09.txt"
input_path = "data/input09.txt"

# Execute the two problems
print("--- Tests ---")
print("Problem 1 test: ", problem1(test_path))
print("Problem 2 test: ", problem2(test_path))

# # Execute the two problems solutions
print("\n--- Solutions ---")
print("Problem 1 result: ", problem1(input_path))
print("Problem 2 result: ", problem2(input_path))
