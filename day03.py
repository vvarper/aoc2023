import re


# Return a list of tuples of the form (n, init, end) where n is the number
# and init and end are the indices of the string where the number starts and
# ends
def find_numbers_in_line(line):
    return [(int(match.group()), match.start(), match.end()) for match in
            re.finditer(r'\d+', line)]


# Check if a number (n, init, end) is adjacent to a symbol different from
# '.' in the lines list
def is_adjacent_to_symbol(number, lines, row):
    init_c = max(0, number[1] - 1)
    end_c = min(len(lines[row]) - 1, number[2])

    symbols = lines[row][init_c] + lines[row][end_c]

    if row > 0:
        symbols += lines[row - 1][init_c:end_c + 1]
    if row < len(lines) - 1:
        symbols += lines[row + 1][init_c:end_c + 1]

    return True if re.search(r'[^.\d]', symbols) else False


# Solution to Problem 1 #######################################################
def problem1(file_path):
    with open(file_path) as file:
        valid_numbers = []
        lines = file.read().splitlines()

        for i in range(len(lines)):
            numbers = find_numbers_in_line(lines[i].strip())

            valid_numbers += [number[0] for number in numbers if
                              is_adjacent_to_symbol(number, lines, i)]

        return sum(valid_numbers)


# Solution to Problem 2 #######################################################
def problem2(file_path):
    with open(file_path) as file:
        lines = file.read().splitlines()
        numbers = []
        gears = []
        sum_gears = 0

        for i in range(len(lines)):
            numbers.append(find_numbers_in_line(lines[i]))
            gears += [(i, match.start()) for match in
                      re.finditer(r'\*', lines[i])]

        for gear in gears:
            possible_numbers = [number for sublist in
                                numbers[gear[0] - 1:gear[0] + 2] for number in
                                sublist]
            par_numbers = [number[0] for number in possible_numbers if
                           number[1] - 1 <= gear[1] <= number[2]]

            if len(par_numbers) == 2:
                sum_gears += par_numbers[0] * par_numbers[1]

        return sum_gears


###############################################################################

# File paths
test_path = "data/test03.txt"
input_path = "data/input03.txt"

# Execute the two problems
print("--- Tests ---")
print("Problem 1 test: ", problem1(test_path))
print("Problem 2 test: ", problem2(test_path))

# Execute the two problems solutions
print("\n--- Solutions ---")
print("Problem 1 result: ", problem1(input_path))
print("Problem 2 result: ", problem2(input_path))
