"""
PRACTICE Test 3, problem 1.

Authors: David Mutchler, Mark Hays, Michael Wollowski,
         Chandan Rupakheti, Matt Boutell, Dave Fisher,
         Claude Anderson, and Brendan Goldacker.  October 2014.
"""  # DONE: PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """
    test_shape()
    test_another_shape()


def test_shape():
    """ Tests the    shape    function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   SHAPE   function:')
    print('--------------------------------------------------')

    print()
    print('Test 1 of shape: r=7')
    shape(7)

    print()
    print('Test 2 of shape: r=4')
    shape(4)

    print()
    print('Test 3 of shape: r=2')
    shape(2)


def shape(r):
    """
    Prints a shape with r rows that looks like this example where r=7:
    +++++++ 7654321
     ++++++ 654321
      +++++ 54321
       ++++ 4321
        +++ 321
         ++ 21
          + 1

    Another example, where r=4:
    ++++ 4321
     +++ 321
      ++ 21
       + 1

    Preconditions:  r is a positive number.
    For purposes of "lining up", assume r is a single digit.
    """
    # ------------------------------------------------------------------
    # DONE: Implement and test this function.
    #          Some tests are already written for you (above).
    #
    # IMPLEMENTATION RESTRICTION:
    #   You may NOT use string multiplication in this problem.
    # ------------------------------------------------------------------
    for q in range(r):
        for l in range(q):
            print(" ", end="")
        for k in range(r - q):
            print('+', end='')
        print(" ", end="")
        for j in range(r - q, 0, -1):
            print(j, end="")
        print()


def test_another_shape():
    """ Tests the    another_shape    function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   ANOTHER_SHAPE   function:')
    print('--------------------------------------------------')

    print()
    print('Test 1 of another_shape: r=5, m=8')
    another_shape(5, 8)

    print()
    print('Test 2 of another_shape: r=4, m=6')
    another_shape(4, 6)

    print()
    print('Test 3 of another_shape: r=7, m=7')
    another_shape(7, 7)


def another_shape(r, m):
    """
    Prints a shape with r rows that looks like this example
    in which r = 5 and m = 8:
    ++++++++ 12345678
     +++++++ 7654321
      ++++++ 123456
       +++++ 54321
        ++++ 1234
    Note that the numbers in rows 1, 3, 5, ... always start at 1
    and INCREASE, while the numbers in rows 2, 4, 6, ... DECREASE
    and always END at 1.
    Also, the number of + symbols in the first row always equals m.

    Here is another example in which r = 4 and m = 6
    ++++++ 123456
     +++++ 54321
      ++++ 1234
       +++ 321

    Yet one more example, in which r=7 and m=7:
    +++++++ 1234567
     ++++++ 654321
      +++++ 12345
       ++++ 4321
        +++ 123
         ++ 21
          + 1

    Preconditions:  r and m are positive integers with r <= m.
    For purposes of "lining up", assume m and n are single digits.
    """
    # ------------------------------------------------------------------
    # DONE: Implement and test this function.
    #          Some tests are already written for you (above).
    #
    # IMPLEMENTATION RESTRICTION:
    #   You may NOT use string multiplication in this problem.
    # ------------------------------------------------------------------
    for k in range(r):
        for j in range(k):
            print(' ', end="")
        for l in range(m - k):
            print('+', end="")
        print(' ', end="")
        if k % 2 == 0:
            for q in range(1, (m - k) + 1):
                print(q, end="")
        else:
            for q in range(m - k, 0, -1):
                print(q, end="")
        print()


# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
