def get_valid_plays(time, distance):
    for t in range(1, time):
        if (time - t) * t > distance:
            min_t = t
            break

    for t in range(time - 1, min_t + 1, -1):
        if (time - t) * t > distance:
            max_t = t
            break

    return max_t - min_t + 1


# Solution to Problem 1 #######################################################
def problem1(file_path):
    with open(file_path) as file:
        races = [line.split(':')[1].strip().split() for line in
                 file.readlines()]
        races = [[int(elem) for elem in line] for line in races]

        mult = 1
        for i in range(len(races[0])):
            mult *= get_valid_plays(races[0][i], races[1][i])

        return mult


# Solution to Problem 2 #######################################################
def problem2(file_path):
    with open(file_path) as file:
        race = [int(line.split(':')[1].strip().replace(' ', '')) for line in
                file.readlines()]
        return get_valid_plays(race[0], race[1] + 1)


###############################################################################

# File paths
test_path = "data/test06.txt"
input_path = "data/input06.txt"

# Execute the two problems
print("--- Tests ---")
print("Problem 1 test: ", problem1(test_path))
print("Problem 2 test: ", problem2(test_path))

# # Execute the two problems solutions
print("\n--- Solutions ---")
print("Problem 1 result: ", problem1(input_path))
print("Problem 2 result: ", problem2(input_path))
