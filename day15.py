import re
from collections import OrderedDict
from functools import reduce


def get_hash(step):
    return reduce(lambda x, y: ((x + ord(y)) * 17) % 256, step, 0)


# Solution to Problem 1 #######################################################
def problem1(file_path):
    with open(file_path) as file:
        sequence = [list(step.strip()) for step in file.read().split(',')]
        return sum(get_hash(step) for step in sequence)


# Solution to Problem 2 #######################################################
def problem2(file_path):
    with open(file_path) as file:
        sequence = [re.split('[-=]', step.strip()) for step in
                    file.read().split(',')]

        boxes = {i: OrderedDict() for i in range(256)}
        for step in sequence:
            box = get_hash(list(step[0]))
            if step[1] == '':
                boxes[box].pop(step[0], None)
            else:
                boxes[box][step[0]] = int(step[1])

        return sum((1 + box) * (i + 1) * boxes[box][key] for box in boxes if
                   boxes[box] for i, key in enumerate(boxes[box]))


###############################################################################

# File paths
test_path = "data/test15.txt"
input_path = "data/input15.txt"

# Execute the two problems
print("--- Tests ---")
print("Problem 1 test: ", problem1(test_path))
print("Problem 2 test: ", problem2(test_path))

# Execute the two problems solutions
print("\n--- Solutions ---")
print("Problem 1 result: ", problem1(input_path))
print("Problem 2 result: ", problem2(input_path))
