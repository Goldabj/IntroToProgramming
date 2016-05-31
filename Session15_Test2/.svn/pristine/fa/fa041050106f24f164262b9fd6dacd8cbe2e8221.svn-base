"""
Test 2, problem 2.

Authors: Mark Hays, David Mutchler, Michael Wollowski, their colleagues,
         and Brendan Goldacker.  October 2014.
"""  # DONE: PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """
    test_problem2()


# ----------------------------------------------------------------------
# Students: Use the following   is_prime   function as appropriate
#           in your solution to the problem below.
#           This  is_prime  function is ALREADY DONE.  Do not modify it.
# ----------------------------------------------------------------------
def is_prime(n):
    """
    Returns True if the given integer is prime, else returns False.

    Note: The algorithm used here is simple and clear but slow.

    Precondition:  The given argument is an integer that is at least 2.
    """
    for k in range(2, (n // 2) + 1):
        if n % k == 0:
            return False

    return True


def test_problem2():
    """ Tests the   problem2   function. """
    # ------------------------------------------------------------------
    # DONE: Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #
    # IMPORTANT: Include  *** at least 6 (SIX) REASONABLY GOOD tests ***
    #
    # IMPORTANT: Be sure that this code REALLY DOES TEST problem2.
    #            Indicate EXPECTED answers where appropriate.
    #
    #            You are welcome to use the   simple_testing   module
    #            for your tests, but you do not have to do so.
    #            (In fact, do NOT use it unless you feel comfortable
    #            with it from having seen it in the practice problems).
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   problem2   function:')
    print('NOTE: You should include at least SIX tests.')
    print('--------------------------------------------------')

    integers = [4, 3, 7, 7, 10, 23]
    print('the following line should print: [3, 7, 7, 23]')
    print(problem2(integers))
    print()

    integers = [5, 2, 3, 5, 2]
    print('the following line should print: [5, 2, 3, 5, 2]')
    print(problem2(integers))
    print()

    integers = [1, 2, 22, 33, 1, 7]
    print('the following line should print: [1, 2, 1, 7]')
    print(problem2(integers))
    print()

    integers = [4, 6, 8]
    print('the following line should print: []')
    print(problem2(integers))
    print()

    integers = [3, 11, 6, 5, 2]
    print('the following line should print: [3, 11, 5, 2]')
    print(problem2(integers))
    print()

    integers = [31, 4, 1, 1, 1, 5, 7, 5]
    print('the following line should print: [31, 1, 1, 1, 5, 7, 5]')
    print(problem2(integers))
    print()


def problem2(integers):
    """
    Returns a new list that contains all the prime numbers in the given
    sequence of integers, in the same order in which they appear in
    the given sequence.

    For example, if the given sequence of integers is:
        -- (4, 3, 7, 7, 10, 23) then this function returns [3, 7, 7, 23]
        -- [55, 10, 4]          then this function returns []
        -- (3, 11, 6, 5, 2)     then this function returns [3, 11, 5, 2]

    Preconditions:
      :type integers: (list, tuple)
    and the given sequence contains only integers that are 2 or larger.
    """
    # ------------------------------------------------------------------
    # DONE: Implement and test this function.
    #
    # IMPORTANT:  Use (call) the above is_prime function as needed
    #             in this problem.
    # ------------------------------------------------------------------
    new_list = []
    for k in range(len(integers)):
        if is_prime(integers[k]):
            new_list.append(integers[k])
    return new_list

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
