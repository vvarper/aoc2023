import math


def process_input(file):
    lines = file.readlines()

    moves = lines[0].strip()
    nodes = []

    for i in range(2, len(lines)):
        n = lines[i].strip().split('= (')
        n[0] = n[0].strip()
        n[1] = n[1].strip().replace(')', '').split(', ')

        nodes.append(n)

    return moves, dict(nodes)


# Solution to Problem 1 #######################################################
def problem1(file_path):
    with open(file_path) as file:
        moves, nodes = process_input(file)
        current = 'AAA'
        step = 0

        while current != 'ZZZ':
            current = nodes[current][1] if moves[step % len(moves)] == 'R' else \
                nodes[current][0]
            step += 1

        return step


# Solution to Problem 2 #######################################################
def problem2(file_path):
    with open(file_path) as file:
        moves, nodes = process_input(file)
        current = [node for node in nodes.keys() if node[-1] == 'A']
        steps = []

        for c in current:
            step = 0
            while c[-1] != 'Z':
                c = nodes[c][1] if moves[step % len(moves)] == 'R' else \
                    nodes[c][0]
                step += 1

            steps += [step]

        return math.lcm(*steps)


###############################################################################

# File paths
test_path1 = "data/test08-1.txt"
test_path2 = "data/test08-2.txt"
input_path = "data/input08.txt"

# Execute the two problems
print("--- Tests ---")
print("Problem 1 test: ", problem1(test_path1))
print("Problem 2 test: ", problem2(test_path2))

# # Execute the two problems solutions
print("\n--- Solutions ---")
print("Problem 1 result: ", problem1(input_path))
print("Problem 2 result: ", problem2(input_path))
