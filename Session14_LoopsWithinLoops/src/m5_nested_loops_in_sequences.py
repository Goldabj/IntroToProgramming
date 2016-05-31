"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of SEQUENCES OF SUB-SEQUENCES.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Brendan Goldacker.  February 2014.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the other functions to test them. """
    test_sum_numbers()
    test_print_characters()
    test_print_characters_slanted()


def test_sum_numbers():
    """ Tests the    sum_numbers    function. """
    # DONE: 2a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    print()
    print('-------------------------------------')
    print('Testing the   SUM_NUMBERS   function:')
    print('-------------------------------------')
    sequence1 = ([1, 2, 4], [3, 4, 5], (2, 1))
    print('the following line should print: 22')
    print(sum_numbers(sequence1))

    sequence2 = ((12, 12), [1, 2, 4, 5], (1, 1, 1))
    print('the following line should print: 39')
    print(sum_numbers(sequence2))

    sequence3 = ([3, 1, 4], (10, 10), [1, 2, 3, 4])
    print('the following line should print: 38')
    print(sum_numbers(sequence3))




def sum_numbers(seq_seq):
    """
    Returns the sum of the numbers in the given sequence
    of subsequences.  For example, if the given argument is:
        [(3, 1, 4), (10, 10), [1, 2, 3, 4]]
    then this function returns    38
    (which is 3 + 1 + 4 + 10 + 10 + 1 + 2 + 3 + 4).
    Preconditions:  the given argument is a sequences of sequences,
                    and each item in the subsequences is a number.
    """
    # DONE: 2b. Implement and test this function.

#     total = 0
#     for k in range(len(seq_seq)):
#         total = total + sum(seq_seq[k])
#     return total

    # or

    total = 0
    for k in range(len(seq_seq)):
        sublist = seq_seq[k]
        for j in range(len(seq_seq[k])):
            total = total + sublist[j]
    return total

def test_print_characters():
    """ Tests the    print_characters    function. """
    # DONE: 3a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    print()
    print('------------------------------------------')
    print('Testing the   PRINT_CHARACTERS   function:')
    print('------------------------------------------')

    sequence1 = ('hi', 'bye', 'a tie!')
    print_characters(sequence1)


def print_characters(sequence_of_strings):
    """
    Prints all the characters in the sequence of strings,
    but each character on ITS OWN LINE.  For example,
    if the given argument is ['hi', 'bye', ' a tie!'],
    then this function prints:
       h
       i
       b
       y
       e
       a

       t
       i
       e
       !
    Precondition:  the given argument is a sequence of strings.
    """
    # DONE: 3b. Implement and test this function.
    for k in range(len(sequence_of_strings)):
        sublist = sequence_of_strings[k]
        for j in range(len(sublist)):
            print(sublist[j])



def test_print_characters_slanted():
    """ Tests the    print_characters_slanted    function. """
    # DONE: 4a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    print()
    print('--------------------------------------------------')
    print('Testing the   PRINT_CHARACTERS_SLANTED   function:')
    print('--------------------------------------------------')

    sequence1 = ('hi', 'bye', 'a tie!')
    print_characters_slanted(sequence1)

def print_characters_slanted(sequence_of_strings):
    """
    Same as the previous problem, but each string 'slants'.
    For example, if the given argument is ['hi', 'bye', 'a tie!'],
    then this function prints:
       h
        i
       b
        y
         e
       a

         t
          i
           e
            !
    Precondition:  the given argument is a sequence of strings.
    """
    # DONE: 4b. Implement and test this function.
    for k in range(len(sequence_of_strings)):
        sublist = sequence_of_strings[k]
        for j in range(len(sublist)):
            for z in range(j + 1):
                print(' ', end='')
            print(sublist[j])
# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
