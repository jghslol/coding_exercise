# Coding Exercise

The code solves questions 1a - 2b of a coding challenge. The task was specifically to use OOP when writing the code.

The instructions are below:

Problem 1
1.a

From the input provided in the file input1.txt, find the two numbers that sum to 2020 and provide the result of multiplying them together.

e.g. For the list below, the two numbers are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

1721
979
366
299
675
1456

1.b

Now find the three numbers in the input set that sum to 2020. Using the example above again, the three numbers that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

2.a

The input provided in the file input2.txt consists of lines with the following format:

n-n c: str

where n is a digit, c is a character and str is a string.

Each line defines a constraint for a string and the string itself. The constraint (n-n c) indicates the lowest and highest number of times a given letter can appear in the string for it to be valid.

In the example input below, 2 strings are valid. The middle string, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third strings are valid: they contain one a or nine c, both meeting their defined constraint.

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc

How many strings meet the constraint in the input2.txt file provided?

2.b

Suppose we change the meaning of the constraint to define the positions the letter may appear in the string. Exactly one of these positions must contain the given letter.

Using the example above:

- 1-3 a: abcde is valid: position 1 contains a and position 3 does not
- 1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b
- 2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c

How many strings meet the constraint in the input2.txt file with the modified constraint?

**Requirements**

There are no libraries that require installation.

Python 3.9.6

**Running the code**

-Ensure that the file structure is maintained

-To run the main test run file as a script through
command line (python3 main.py)

-Run the tests as a script (python3 test_main.py)


