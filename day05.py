# Solution to Problem 1 #######################################################
def problem1(file_path):
    with open(file_path) as file:
        seeds = [int(number) for number in file.readline().strip().split()[1:]]
        processed = [False] * len(seeds)

        for line in file:
            line = line.strip().split()

            if not line:
                processed = [False] * len(seeds)

            elif line[0].isdigit():
                mapping = [int(number) for number in line]

                for i in range(len(seeds)):
                    if not processed[i]:
                        if mapping[1] <= seeds[i] < mapping[1] + mapping[2]:
                            diff = seeds[i] - mapping[1]
                            seeds[i] = mapping[0] + diff
                            processed[i] = True

        return min(seeds)


# Solution to Problem 2 #######################################################
def problem2(file_path):
    with open(file_path) as file:
        seeds_ranges = [int(number) for number in
                        file.readline().strip().split()[1:]]
        seeds_ranges = [
            [seeds_ranges[i], seeds_ranges[i] + seeds_ranges[i + 1] - 1] for i
            in range(0, len(seeds_ranges), 2)]

        for line in file:
            line = line.strip().split()

            if not line:
                processed = [False] * len(seeds_ranges)

            elif line[0].isdigit():
                mapping = [int(number) for number in line]
                new_seeds_ranges = []
                for i in range(len(seeds_ranges)):
                    if not processed[i]:
                        m = [mapping[1], mapping[1] + mapping[2] - 1]

                        # 1. Get new intervals
                        if seeds_ranges[i][0] < m[0] <= seeds_ranges[i][1]:
                            new_seeds_ranges.append(
                                [seeds_ranges[i][0], m[0] - 1])
                            top = seeds_ranges[i][1]
                            if seeds_ranges[i][1] > m[1]:
                                new_seeds_ranges.append(
                                    [m[1] + 1, seeds_ranges[i][1]])
                                top = m[1]

                            seeds_ranges[i] = [m[0], top]

                        elif seeds_ranges[i][0] <= m[1] < seeds_ranges[i][1]:
                            new_seeds_ranges.append(
                                [m[1] + 1, seeds_ranges[i][1]])
                            seeds_ranges[i] = [seeds_ranges[i][0], m[1]]

                        # 2. Update the actual interval
                        if mapping[1] <= seeds_ranges[i][0] < mapping[1] + \
                                mapping[2]:
                            diff = seeds_ranges[i][0] - mapping[1]
                            diff_seeds = seeds_ranges[i][1] - seeds_ranges[i][
                                0]
                            seeds_ranges[i][0] = mapping[0] + diff
                            seeds_ranges[i][1] = mapping[0] + diff + diff_seeds
                            processed[i] = True

                seeds_ranges += new_seeds_ranges
                processed += [False] * len(new_seeds_ranges)

        min_seeds = [s[0] for s in seeds_ranges]

        return min(min_seeds)


###############################################################################

# File paths
test_path = "data/test05.txt"
input_path = "data/input05.txt"

# Execute the two problems
print("--- Tests ---")
print("Problem 1 test: ", problem1(test_path))
print("Problem 2 test: ", problem2(test_path))

# # Execute the two problems solutions
print("\n--- Solutions ---")
print("Problem 1 result: ", problem1(input_path))
print("Problem 2 result: ", problem2(input_path))
