"""
PRACTICE Test 3, problem 2.

Authors: David Mutchler, Mark Hays, Michael Wollowski,
         Chandan Rupakheti, Matt Boutell, Dave Fisher,
         Claude Anderson, and Brendan Goldacker.  October 2014.
"""  # DONE: PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """
    test_integers()


def test_integers():
    """ Tests the    integers    function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   integers   function:')
    print('--------------------------------------------------')

    sequence1 = [(3, 1, 4), (10, 'hi', 10), [1, 2.5, 3, 4], 'hello', [], ['oops'], [[55], [44]], [30, -4]]
    print(integers(sequence1))
    print('the folllowing line should print a list of [3, 1, 4, 10, 10, 1, 3, 4, 30, -4]')

    sequence2 = [(20, 'blue', 2.2, 2, 11), (10, 22), ('yellow', 2), (3, .1), (2.4, 2.4, 2, 4)]
    print(integers(sequence2))
    print('the following line should print a list of [20, 2, 11, 10, 22, 2, 3, 2, 4]')

    sequence3 = [[11, 11, 11], ['a', '11, 12', 2], (20, 2.0, 1), ('hello')]
    print(integers(sequence3))
    print('the following line should print a list of [11, 11, 11, 2, 20, 1]')

    # ------------------------------------------------------------------
    # DONE: Implement this function, using it to test the NEXT function.
    #       Write the two functions in whichever order you prefer.
    #
    # IMPORTANT: Include  *** at least 3 REASONABLY GOOD tests ***.
    #            Indicate EXPECTED answers for each test.
    # ------------------------------------------------------------------


def integers(sequence_of_sequences):
    """
    Returns a new list that contains all the integers
    in the subsequences of the given sequence, in the order that they
    appear in the subsequences.
    For example, if the argument is:
        [(3, 1, 4),
         (10, 'hi', 10),
         [1, 2.5, 3, 4],
         'hello',
         [],
         ['oops'],
         [[55], [44]],
         [30, -4]
        ]
    then this function returns:
        [3, 1, 4, 10, 10, 1, 3, 4, 30, -4]

    Precondition:  the given argument is a sequence of sequences.
    """
    # ------------------------------------------------------------------
    # DONE: Implement and test this function.
    # HINT: The   type   function indicates whether or not its argument
    #       is an integer.  For example:
    #         -- type(34) is True
    #         -- type(4.6) is False
    #         -- type('three') is False
    #         -- type([1, 2, 3]) is False
    # ------------------------------------------------------------------
    new_list = []
    for k in range(len(sequence_of_sequences)):
        sub_sequence = sequence_of_sequences[k]
        for j in range(len(sub_sequence)):
            if type(sub_sequence[j]) == int:
                new_list.append(sub_sequence[j])
    return new_list

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
