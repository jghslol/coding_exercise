import unittest
from main import *

class TestMultiplyTwoOrThreeNumbersThatSum2020(unittest.TestCase):
    """
    Tests to check that class to resolve Problem 1 works as expected
    """

    def test_open_file_return_set(self):
        # Test 1: Test that the open file
        # function still opens the correct file
        # which is file 1

        input_file_1 = 'Input/input1.txt'

        self.assertEqual(
            MultiplyTwoOrThreeNumbersThatSum2020(input_file_1).open_file_return_set(),
            MultiplyTwoOrThreeNumbersThatSum2020(INPUT_FILE_1).open_file_return_set()
        )

        # Test 2: Test that the function returns a set

        self.assertEqual(
            type(MultiplyTwoOrThreeNumbersThatSum2020(input_file_1).open_file_return_set()),
            set
        )

        # Test 3: test that the output file does not contain /"n"

        self.assertNotIn(
            "\n",
            MultiplyTwoOrThreeNumbersThatSum2020(INPUT_FILE_1).open_file_return_set()
        )

    def test_find_two_numbers(self):
        # Test to check that p1 outputs the expected
        # value
        expected_value = p1
        self.assertEqual(expected_value, 1013211)


    def test_find_three_numbers(self):
        # Test to check that p2 outputs the
        # expected value
        expected_value = p2
        self.assertEqual(expected_value, 13891280)

class TestCheckThatStringsSatisfiesConstraint(unittest.TestCase):
    """
    Tests to check that class to resolve Problem 2 works as expected
    """
    def test_open_file(self):
        # Test 1: Test that the test open file
        # function still opens the correct file
        # which is file 2

        input_file_2 = 'Input/input2.txt'

        self.assertEqual(
            CheckThatStringsSatisfiesConstraint(input_file_2).open_file(),
            CheckThatStringsSatisfiesConstraint(INPUT_FILE_2).open_file()
        )

    def test_check_constraint(self):
        # Test 2: Test that the function
        # is returning the expected value
        # for occurrences

        expected_value = CheckThatStringsSatisfiesConstraint(INPUT_FILE_2).check_constraint("occurrences")
        self.assertEqual(expected_value, 666)

        # Test 3: Test that the function
        # is returning the expected values for
        # position

        expected_value = CheckThatStringsSatisfiesConstraint(INPUT_FILE_2).check_constraint("position")
        self.assertEqual(expected_value, 499)


if __name__ == '__main__':
    unittest.main()