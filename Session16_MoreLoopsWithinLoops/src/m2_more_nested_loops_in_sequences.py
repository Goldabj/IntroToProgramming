"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of SEQUENCES OF SUB-SEQUENCES.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Brendan Goldacker.  February 2014.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the other functions to test them. """
    test_keep_integers()
    test_largest_negative_number()


def test_keep_integers():
    """ Tests the    keep_integers    function. """
    # ------------------------------------------------------------------
    # DONE: 2a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    # ------------------------------------------------------------------
    print()
    print('---------------------------------------')
    print('Testing the   KEEP_INTEGERS   function:')
    print('---------------------------------------')

    sequence1 = [(3, 1, 4), (10, 'hi', 10), [1, 2.5, 3, 4], 'hello', [], ['oops'], [30, -4]]
    keep_integers(sequence1)
    print('the following line should print: [(3, 1, 4), [], [30, -4]')
    print(sequence1)


def keep_integers(seq_seq):
    """
    MUTATES the given list of sequences as follows:  It keeps ONLY
    the items in the sequence that contain ONLY integers.
    For example, if the given argument is:
        [(3, 1, 4),
         (10, 'hi', 10),
         [1, 2.5, 3, 4],
         'hello',
         [],
         ['oops'],
         [30, -4]
        ]
    then this function MUTATES that argument into:
        [(3, 1, 4),
         [],
         [30, -4]
        ]
    Preconditions:  the given argument is a list of sequences.
    """
    # ------------------------------------------------------------------
    # DONE: 2b. Implement and test this function.
    #
    # HINTS:
    #  -- An elegant way to keep the indexing consistent while
    #     deleting items from the exterior sequence is to go through the
    #     exterior sequence BACKWARDS.
    #  -- One way to delete an item from a list is like this:
    #        del x[r]
    #     This example deletes the item at index r in the list x.
    # ------------------------------------------------------------------

    for k in range(len(seq_seq) - 1, -1, -1):
        sublist = seq_seq[k]
        for j in range(len(sublist)):
            if type(sublist[j]) != int:
                del seq_seq[k]
                break



def test_largest_negative_number():
    """ Tests the    largest_negative_number    function. """
    # ------------------------------------------------------------------
    # DONE: 3a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    # ------------------------------------------------------------------
    print()
    print('-------------------------------------------------')
    print('Testing the   LARGEST_NEGATIVE_NUMBER   function:')
    print('-------------------------------------------------')

    numbers = [(30, -5, 8, -20), (100, -2.6, 88, -40, -5), (400, 500)]
    print('the following line should print: -2.6')
    print(largest_negative_number(numbers))

    numbers2 = [(200, 2, 20), (500, 400)]
    print('the follwing line should print: 0')
    print(largest_negative_number(numbers2))


def largest_negative_number(seq_seq):
    """
    Returns the largest negative number in the given sequence of
    sequences of numbers.  Returns 0 if there are no negative numbers
    in the sequence of sequences.

    For example, if the given argument is:
        [(30, -5, 8, -20),
         (100, -2.6, 88, -40, -5),
         (400, 500)
        ]
    then this function returns -2.6.

    As another example, if the given argument is:
      [(200, 2, 20), (500, 400)]
    then this function returns 0.

    Preconditions:
      :type seq_seq: (list, tuple)
    and the given argument is a sequence of sequences,
    where each subsequence contains only numbers.
    """
    # ------------------------------------------------------------------
    # DONE: 3b. Implement and test this function.
    # ------------------------------------------------------------------
    for k in range(len(seq_seq) - 1):
        sublist = seq_seq[k]
        largest_neg = sublist[k]
        for j in range(len(sublist) - 1):
            if largest_neg < sublist[j] and sublist[j] < 0:
                largest_neg = sublist[j]
        if largest_neg > 0:
            largest_neg = 0
    return largest_neg



# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
