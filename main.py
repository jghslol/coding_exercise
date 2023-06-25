INPUT_FILE_1 = "Input/input1.txt"
INPUT_FILE_2 = "Input/input2.txt"

class MultiplyTwoOrThreeNumbersThatSum2020:
    """
    Problem 1:
    to find the result of multiplying
    two or three numbers that sum to
    get 2020
    """
    def __init__(self, filename):
        self.filename = filename
        self.number = 2020

    def open_file_return_set(self):
        # Opens file, strips unnecessary
        # characters, transforms data
        # to memory efficient set
        filename = self.filename
        with open(filename) as f:
            input = set(int(line.rstrip('\n')) for line in f)
            return input

    def find_two_numbers(self):
        # Finds two numbers that sum
        # to 2020 iterating over set once
        # giving O(n) performance
        number = self.number
        input = self.open_file_return_set()

        for value in input:
            if number - value in input:
                num_required = number - value
                return num_required * value

    def find_three_numbers(self):
        # Similarly this finds three numbers,
        # but limits iterations to twice
        number = self.number
        input = self.open_file_return_set()

        for value_1 in input:
            for value_2 in input:
                num_required = number - value_1 - value_2
                if num_required in input:
                    return num_required * value_1 * value_2

class CheckThatStringsSatisfiesConstraint:
    """
    Problem 2:
    to check that the string satisfies the constraints
    as set out in the prefix
    """
    def __init__(self, filename):
        self.filename = filename

    def open_file(self):
        # Opens file, reads lines
        filename = self.filename
        with open(filename) as f:
            file = f.readlines()
            return file

    def check_constraint(self, type_of_check):
        # There are two separate problems
        # both dealt with in check_constraint
        # to parse data once
        file = self.open_file()
        valid = 0

        for line in file:
            numbers = line.split(":")[0].split(" ")[0]
            data = line.split(":")[1]
            letter = line.split(":")[0].split(" ")[1]
            min_occ_pos_a = int(numbers.split("-")[0])
            max_occ_pos_b = int(numbers.split("-")[1])
            occur = int(line.split(":")[1].count(letter))

            # This check whether the constraints
            # of min and max occurrences are met, if
            # "occurrences" are set as an argument when
            # the function is called
            if type_of_check == "occurrences":
                if min_occ_pos_a <= occur <= max_occ_pos_b:
                    valid += 1

            # This checks whether the constraints of
            # position are met if "position" is set as
            # an argument when the function is called
            if type_of_check == "position":
                if (data[min_occ_pos_a]  or data[max_occ_pos_b]) == letter:
                    valid += 1
        return valid

p1 = MultiplyTwoOrThreeNumbersThatSum2020(INPUT_FILE_1).find_two_numbers()
p2 = MultiplyTwoOrThreeNumbersThatSum2020(INPUT_FILE_1).find_three_numbers()

p3 = CheckThatStringsSatisfiesConstraint(INPUT_FILE_2).check_constraint("occurrences")
p4 = CheckThatStringsSatisfiesConstraint(INPUT_FILE_2).check_constraint("position")

print(f'The solution to problem 1a is: {p1}')
print(f'The solution to problem 1b is: {p2}')
print(f'The solution to problem 2a is: {p3}')
print(f'The solution to problem 2b is: {p4}')

