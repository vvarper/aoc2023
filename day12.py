dp_memory = {}


def get_possibilites(springs, remaining, num_contiguous=0):
    if not springs:
        return (len(remaining) == 1 and remaining[0] == num_contiguous) or (
                len(remaining) == 0 and num_contiguous == 0)
    if (springs, remaining, num_contiguous) in dp_memory:
        return dp_memory[(springs, remaining, num_contiguous)]

    num_arrangements = 0
    if springs[0] in ('#', '?'):
        num_arrangements += get_possibilites(springs[1:], remaining,
                                             num_contiguous + 1)
    if springs[0] in ('.', '?'):
        if num_contiguous > 0 and len(remaining) > 0 and (
                remaining[0] == num_contiguous):
            num_arrangements += get_possibilites(springs[1:], remaining[1:])
        elif num_contiguous == 0:
            num_arrangements += get_possibilites(springs[1:], remaining)

    dp_memory[(springs, remaining, num_contiguous)] = num_arrangements
    return num_arrangements


# Solution to Problem 1 #######################################################
def problem1(file_path):
    with open(file_path) as file:
        rows = [line.strip().split() for line in file.readlines()]

        total = 0
        for row in rows:
            row[1] = tuple(map(int, row[1].split(',')))
            total += get_possibilites(row[0], row[1])

        return total


# Solution to Problem 2 #######################################################
def problem2(file_path):
    with open(file_path) as file:
        rows = [line.strip().split() for line in file.readlines()]

        total = 0
        for row in rows:
            row[0] = '?'.join([row[0]] * 5)
            row[1] = tuple(map(int, row[1].split(','))) * 5

            total += get_possibilites(row[0], row[1])

        return total


###############################################################################

# File paths
test_path = "data/test12.txt"
input_path = "data/input12.txt"

# Execute the two problems
print("--- Tests ---")
print("Problem 1 test: ", problem1(test_path))
print("Problem 2 test: ", problem2(test_path))

# Execute the two problems solutions
print("\n--- Solutions ---")
print("Problem 1 result: ", problem1(input_path))
print("Problem 2 result: ", problem2(input_path))
