import numpy as np


def process_patterns(file):
    data = [list(line.strip()) for line in file.readlines()]

    patterns = []
    current_pattern = []
    for line in data:
        if line:
            current_pattern += [line]
        else:
            patterns += [current_pattern]
            current_pattern = []

    patterns += [current_pattern]

    return patterns


def search_reflection_one_axis(p, avoid=-1):
    note = -1
    for i in range(1, p.shape[0]):
        if i != avoid and np.array_equal(p[i], p[i - 1]):
            size = min(i, p.shape[0] - i)
            if np.array_equal(p[i:i + size], p[i - size:i][::-1]):
                note = i
                break

    return note


def search_reflection(p, avoid_row=-1, avoid_col=-1):
    is_row = False

    # Iterate columns
    note = search_reflection_one_axis(p.T, avoid_col)
    if note == -1:
        note = search_reflection_one_axis(p, avoid_row)
        is_row = True

    return note, is_row


# Solution to Problem 1 #######################################################
def problem1(file_path):
    with open(file_path) as file:
        patterns = process_patterns(file)
        total = 0
        for pattern in patterns:
            p = np.array(pattern)
            note, is_row = search_reflection(p)
            if note != -1:
                total += note + 99 * note * is_row

        return total


# Solution to Problem 2 #######################################################
def problem2(file_path):
    with open(file_path) as file:
        patterns = process_patterns(file)
        total = 0
        for pattern in patterns:
            p = np.array(pattern)

            ori_note, is_row = search_reflection(p)

            avoid_row = -1 if not is_row else ori_note
            avoid_col = -1 if is_row else ori_note

            # For every pixel
            for i, j in np.ndindex(p.shape):
                # Invert the pixel
                p[i][j] = '#' if p[i][j] == '.' else '.'

                # Avoid the pixel in the reflection
                note, is_row = search_reflection(p, avoid_row, avoid_col)
                if note != -1:
                    total += note + 99 * note * is_row
                    break

                # Recover the pixel
                p[i][j] = '#' if p[i][j] == '.' else '.'

        return total


###############################################################################

# File paths
test_path = "data/test13.txt"
input_path = "data/input13.txt"

# Execute the two problems
print("--- Tests ---")
print("Problem 1 test: ", problem1(test_path))
print("Problem 2 test: ", problem2(test_path))

# Execute the two problems solutions
print("\n--- Solutions ---")
print("Problem 1 result: ", problem1(input_path))
print("Problem 2 result: ", problem2(input_path))
