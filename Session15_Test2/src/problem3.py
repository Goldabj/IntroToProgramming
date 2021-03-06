"""
Test 2, problem 3.

Authors: Mark Hays, David Mutchler, Michael Wollowski, their colleagues,
         and Brendan Goldacker.  October 2014.
"""  # DONE: PUT YOUR NAME IN THE ABOVE LINE.

import simple_testing as st


def main():
    """ Calls the   TEST   functions in this module. """
    test_problem3()


def test_problem3():
    """ Tests the   problem3   function. """
    # ------------------------------------------------------------------
    # We have implemented this function for you.  You are welcome
    # to add more tests if you wish, but you do not have to do so.
    # ------------------------------------------------------------------

    # Some tests:
    tests = [st.SimpleTestCase(problem3,
                               [5, 1, 20],
                               8),
             st.SimpleTestCase(problem3,
                               [25, 0.5, 100],
                               42),
             st.SimpleTestCase(problem3,
                               [3, 1, 12],
                               5),
             st.SimpleTestCase(problem3,
                               [3, 1, 12.001],
                               6),
             st.SimpleTestCase(problem3,
                               [7, 2, 100],
                               8),
             st.SimpleTestCase(problem3,
                               [100, 0.002, 1000],
                               1087),
             st.SimpleTestCase(problem3,
                               [9999, 0.5, 10300],
                               10101),
             ]

    # Run the tests.
    st.SimpleTestCase.run_tests('problem3', tests)


def problem3(m, p, x):
    """
    Returns the smallest n such that the sum
      (m ** p)  +  ((m+1) ** p)  +  (m+2) ** p)  +  ((m+3) ** p)
                +  ...  +  (n ** p)
    is greater than or equal to x.

    Some examples:

      -- If m=5, p=1 and x=20, then this function returns 4,
             since (5 ** 1) + (6 ** 1) + (7 ** 1) is 18
                   which is less than 20
               and (5 ** 1) + (6 ** 1) + (7 ** 1) + (8 ** 1) is 26
                   which is greater than or equal to 20.

      -- If m=25, p=0.5 and x=100, then this function returns 42,
             since (25 ** 0.5) + (26 ** 0.5) + (27 ** 0.25)
                               + ... + (41 ** 0.5) is 97.385
                   which is less than 100
               and (25 ** 0.5) + (26 ** 0.5) + (27 ** 0.25)
                               + ... + (42 ** 0.5) is 103.866
                   which is greater than or equal to 100.

      -- See the test cases in  test_problem3  above for more examples.

    Preconditions:
      :type m: int
      :type p: (float, int)
      :type x: (float, int)
    """
    # ------------------------------------------------------------------
    # DONE: Implement and test this function.
    # ------------------------------------------------------------------
    list = []
    k = -1
    while True:
        k += 1
        list.append((m + k) ** p)
        if sum(list) >= x:
            n = (m + k)
            return n

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
