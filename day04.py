# Solution to Problem 1 #######################################################
def problem1(file_path):
    with open(file_path) as file:
        lines = file.read().splitlines()
        sum = 0
        for line in lines:
            card = line.split(':')[1].split('|')
            win = card[0].strip().split()
            actual = card[1].strip().split()

            count = len(set(win) & set(actual))

            if count > 0:
                sum += 2 ** (count - 1)

        return sum


# Solution to Problem 2 #######################################################
def problem2(file_path):
    with open(file_path) as file:
        lines = file.read().splitlines()

        dict = {i: 1 for i in range(1, len(lines) + 1)}

        for i in dict.keys():
            card = lines[i - 1].split(':')[1].split('|')
            win = card[0].strip().split()
            actual = card[1].strip().split()

            count = 1
            for number in actual:
                if number in win:
                    dict[i + count] += dict[i]
                    count += 1

        return sum(dict.values())


###############################################################################

# File paths
test_path = "data/test04.txt"
input_path = "data/input04.txt"

# Execute the two problems
print("--- Tests ---")
print("Problem 1 test: ", problem1(test_path))
print("Problem 2 test: ", problem2(test_path))

# Execute the two problems solutions
print("\n--- Solutions ---")
print("Problem 1 result: ", problem1(input_path))
print("Problem 2 result: ", problem2(input_path))
