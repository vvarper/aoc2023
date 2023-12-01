# Solution to Problem 1 #######################################################
def problem1(file_path):
    with open(file_path) as file:
        score = 0
        for line in file:
            # Iterate line and get all digits
            digits = [int(digit) for digit in line.strip() if digit.isdigit()]

            value = digits[0] * 10 + digits[-1]
            score += value

    return score


# Solution to Problem 2 #######################################################
def problem2(file_path):
    # Create dictionary with name and number
    numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6,
               'seven': 7, 'eight': 8, 'nine': 9}

    with open(file_path) as file:
        score = 0
        for line in file:
            digits = []
            for i in range(len(line)):
                if line[i].isdigit():
                    digits.append(int(line[i]))
                else:
                    for elem in numbers.keys():
                        if line[i:].startswith(elem):
                            digits.append(numbers[elem])
                            break

            value = digits[0] * 10 + digits[-1]

            score += value

    return score


###############################################################################

# File paths
test_path1 = "data/test01-1.txt"
test_path2 = "data/test01-2.txt"
input_path = "data/input01.txt"

# Execute the two problems tests
print("Problem 1 test: ", problem1(test_path1))
print("Problem 2 test: ", problem2(test_path2))

# Execute the two problems solutions
print("Problem 1 result: ", problem1(input_path))
print("Problem 2 result: ", problem2(input_path))
