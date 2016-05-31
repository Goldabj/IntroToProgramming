"""
PRACTICE Test 3, problem 4 (code for TESTING the Elevator class).

Authors: David Mutchler, Mark Hays, Michael Wollowski,
         Chandan Rupakheti, Matt Boutell, Dave Fisher,
         Claude Anderson, and PUT YOUR NAME HERE.  October 2014.
"""  # TODO: PUT YOUR NAME IN THE ABOVE LINE.

import problem4_Elevator as p4

# ----------------------------------------------------------------------
# TODO: Add code below (at the appropriate places)
#       to test your   Elevator   class as you implement it.
#
# IMPORTANT:
#  1. Read the specification of the ENTIRE Elevator class BEFORE
#       writing any code.
#  2. Test each method AS YOU DEFINE IT (one by one).
# ----------------------------------------------------------------------


def main():
    """ Tests the   Elevator  class """
    test_init()
    test_all_people_enter()
    test_last_people_exit()
    test_remaining_capacity()
    test_capacity_exceeded()
    test_oldest_person()
    test_elevator_with_oldest()


def test_init():
    print('------------------------------------')
    print('Testing __init__:')
    elevator1 = p4.Elevator(2000)
    elevator2 = p4.Elevator(400)
    elevator3 = p4.Elevator(1000)

    # Add code below here to continue this test:


def test_all_people_enter():
    print('\n------------------------------------')
    print('Testing all_people_enter:')
    elevator1 = p4.Elevator(2000)
    elevator2 = p4.Elevator(400)
    elevator3 = p4.Elevator(1000)

    people1 = [p4.Person(18, 150),
               p4.Person(42, 200),
               p4.Person(23, 150),
               p4.Person(67, 180),
               p4.Person(30, 210)]
    people2 = [p4.Person(25, 170)]

    elevator1.all_people_enter(people1)
    elevator2.all_people_enter(people2)

    elevator3.all_people_enter(people1)
    elevator3.all_people_enter(people2)

    # Add code below here to continue this test:


def test_last_people_exit():
    print('\n------------------------------------')
    print('Testing last_people_exit:')
    elevator1 = p4.Elevator(2000)
    elevator2 = p4.Elevator(400)
    elevator3 = p4.Elevator(1000)

    people1 = [p4.Person(18, 150),
               p4.Person(42, 200),
               p4.Person(23, 150),
               p4.Person(67, 180),
               p4.Person(30, 210)]
    people2 = [p4.Person(25, 170)]

    elevator1.all_people_enter(people1)
    elevator2.all_people_enter(people2)
    elevator3.all_people_enter(people1)

    elevator1.last_people_exit(3)
    elevator2.last_people_exit(1)
    elevator3.last_people_exit(1)
    elevator3.last_people_exit(1)

    # Add code below here to continue this test:


def test_remaining_capacity():
    print('\n------------------------------------')
    print('Testing remaining_capacity:')
    elevator1 = p4.Elevator(2000)
    elevator2 = p4.Elevator(400)
    elevator3 = p4.Elevator(1000)

    people1 = [p4.Person(18, 150),
               p4.Person(42, 200),
               p4.Person(23, 150)]
    people2 = [p4.Person(25, 170)]
    people3 = [p4.Person(25, 200)]

    elevator1.all_people_enter(people1)
    elevator2.all_people_enter(people1)
    elevator3.all_people_enter(people1)
    elevator3.all_people_enter(people2 + people3)

    # Add code below here to continue this test:


def test_capacity_exceeded():
    print('\n------------------------------------')
    print('Testing capacity_exceeded:')
    elevator1 = p4.Elevator(2000)
    elevator2 = p4.Elevator(400)
    elevator3 = p4.Elevator(1000)

    people1 = [p4.Person(18, 150),
               p4.Person(42, 200),
               p4.Person(23, 150)]
    people2 = [p4.Person(25, 170)]
    people3 = [p4.Person(25, 200)]

    elevator1.all_people_enter(people1)
    elevator2.all_people_enter(people1)
    elevator3.all_people_enter(people1)
    elevator3.all_people_enter(people2 + people3)

    # Add code below here to continue this test:


def test_oldest_person():
    print('\n------------------------------------')
    print('Testing oldest_person')
    elevator1 = p4.Elevator(2000)
    elevator2 = p4.Elevator(750)

    people1 = [p4.Person(18, 150),
               p4.Person(42, 200),
               p4.Person(23, 150),
               p4.Person(67, 180),
               p4.Person(30, 210)]
    people2 = [p4.Person(25, 170)]

    elevator1.all_people_enter(people1)
    elevator2.all_people_enter(people2)

    # Add code below here to continue this test:


def test_elevator_with_oldest():
    print('\n------------------------------------')
    print('Testing elevator_with_oldest')
    elevator1 = p4.Elevator(2000)
    elevator2 = p4.Elevator(750)
    elevator3 = p4.Elevator(1000)
    elevator4 = p4.Elevator(1200)

    people1 = [p4.Person(18, 150),
               p4.Person(42, 200),
               p4.Person(23, 150),
               p4.Person(67, 180),
               p4.Person(30, 210)]
    people2 = [p4.Person(25, 170)]
    people3 = [p4.Person(20, 180),
               p4.Person(40, 150)]
    people4 = [p4.Person(5, 40)]

    elevator1.all_people_enter(people1)
    elevator2.all_people_enter(people2)
    elevator3.all_people_enter((people3))
    elevator4.all_people_enter(people4)

    elevatorsA = [elevator1, elevator2, elevator3]
    elevatorsB = [elevator2, elevator3]

    # Add code below here to continue this test:

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
