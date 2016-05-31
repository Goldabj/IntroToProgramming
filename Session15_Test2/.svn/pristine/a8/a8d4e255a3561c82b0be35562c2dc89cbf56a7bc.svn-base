"""
Test 2, problem 1.

Authors: Mark Hays, David Mutchler, Michael Wollowski, their colleagues,
         and Brendan Goldacker.  October 2014.
"""  # DONE: PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """
    test_problem1()


def test_problem1():
    """ Tests the   problem1   function. """
    # ------------------------------------------------------------------
    # DONE: Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #
    # IMPORTANT: Include  *** at least 4 tests ***.
    #
    # IMPORTANT: Be sure that this code REALLY DOES TEST problem1.
    #   You might want to look at the code that you used to test
    #   Problem 1 of the Practice Problems for Test 2.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   problem1   function:')
    print('NOTE: You should include at least FOUR tests.')
    print('--------------------------------------------------')
    list1 = [4, 66, 9, -2, 55, 0]
    list2 = [7, 22, 5, 10, -5, 9]
    problem1(list1, list2)
    print('the follwing line should print: [11, 88, 14, 8, 50, 9]')
    print(list1)

    list1 = [20, -20, 10]
    list2 = [-20, 20, -10]
    problem1(list1, list2)
    print('the follwing line should print: [0, 0, 0]')
    print(list1)

    list1 = [1, 2, 4, 5]
    list2 = [6, 5, 4, 3]
    problem1(list1, list2)
    print('the follwing line should print: [7, 7, 8, 8]')
    print(list1)

    list1 = [3, 2, 1, 0, 0, 3]
    list2 = [2, 4 , -2, 0, 2, 3]
    problem1(list1, list2)
    print('the follwing line should print: [5, 6, -1, 0, 2, 6]')
    print(list1)

def problem1(list1, list2):
    """
    MUTATES the first of the two given lists so that it becomes
    the item-by-item   sum   of the two given lists.

    For example, if the given lists are:
        [4, 66, 9, -2, 55, 0]
        [7, 22, 5, 10, -5, 9]
    then the first of those two lists should mutate into:
        [11, 88, 14, 8, 50, 9]

    As another example, if the given lists are:
        [ 20, -20,  10]
        [-20,  20, -10]
    then the first of those two lists should mutate into:
        [  0,   0,   0]

    Does NOT return anything explicitly (so returns  None  implicitly).
    Does NOT mutate the second list.

    Preconditions:
      :type list1: list
      :type list2: list
    and the given lists contain only numbers,
    and the lengths of two lists are the same.
    """
    # ------------------------------------------------------------------
    # DONE: Implement and test this function.
    # ------------------------------------------------------------------
    for k in range(len(list1)):
        list1[k] = list1[k] + list2[k]


# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
