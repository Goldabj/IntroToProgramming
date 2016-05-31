"""
This module lets you practice simple FOR loops using RANGE expressions:
    -- With one argument: range(x)
    -- With two arguments: range(x, y)
    -- With three arguments: range(x, y, z)

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Bendan Goldacker.  December 2013.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import math


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # DONE: 2. Implement and test this function.
    print_sequence1()
    print_sequence2()
    print_sequence3()
    print_square_roots()
    print_decimals()

def print_sequence1():
    """
    Prints the numbers 0, 1, 2, ... 34, in that order,
    each on its own line.
    """
    # DONE: 3. Implement and test this function.
    #          Implementation requirement: you must use a COUNTED LOOP.
    for k in range(35):
        print(k)


def print_sequence2():
    """
    Prints the numbers 34, 33, 32, 31, ... 0, in that order,
    each on its own line.
    """
    # DONE: 4. Implement and test this function.
    #          Implementation requirement: you must use a COUNTED LOOP.
    for k in range(34, -1, -1):
        print(k)


def print_sequence3():
    """
    Prints the numbers 20, 30, 40, ... 110, in that order,
    each on its own line.
    """
    # DONE: 5. Implement and test this function.
    #          Implementation requirement: you must use a COUNTED LOOP.
    for k in range(20, 120, 10):
        print(k)


def print_square_roots():
    """
    Prints the SQUARE ROOTS of the numbers 121, 122, 123, ... 144,
    in that order, each on its own line.  Thus, the numbers printed
    should be about:   11.0  11.04536  ... 12.0.
    """
    # DONE: 6. Implement and test this function.
    #          Implementation requirement: you must use a COUNTED LOOP.
    # HINT: You need to   import math   at the top of this file
    #       to use math functions like the one for square root.
    #       Once you have that import in place, typing
    #            math.
    #       (note the DOT) and pausing will display options that make
    #       it plain what the notation for the square root function is.
    for k in range(121, 145):
        print(math.sqrt(k))



def print_decimals():
    """
    Prints the numbers 0.123, 0.124, 0.125, ... 0.144, in that order,
    each on its own line.  It is OK if the numbers are not exact.
    """
    # DONE: 7. Implement and test this function.
    #          Implementation requirement: you must use a COUNTED LOOP.
    # HINT: You can NOT use floats in a RANGE expression;
    #         its arguments MUST be ints (whole numbers).
    #         But you can use DIVISION in the EXPRESSION that you PRINT.
    # NOTE: Floating point numbers are APPROXIMATIONS of real numbers.
    #         Depending on how you solve this problem,
    #         you might (or might not) get numbers like 0.12600006
    #         or 0.125999998.  That's OK.
    for k in range(23, 45):
        print("0.1" + str(k))

#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
