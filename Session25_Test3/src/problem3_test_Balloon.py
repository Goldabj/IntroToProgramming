"""
Test 3, part of problem 3.

Authors: David Mutchler, Mark Hays, Michael Wollowski,
         Chandan Rupakheti, Matt Boutell, Dave Fisher,
         Claude Anderson, and Brendan Goldacker.  November 2014.
"""  # DONE: PUT YOUR NAME IN THE ABOVE LINE.

# ----------------------------------------------------------------------
# DONE: Add code below (at the appropriate places)
#       to test your   Balloon   class as you implement it.
#       The   Balloon   class is in the separate file  balloon.py
#
# IMPORTANT:
#  1. Read the specification of the ENTIRE   Balloon   class BEFORE
#       writing any code.
#  2. Test each method AS YOU DEFINE IT (one by one).
# ----------------------------------------------------------------------

import problem3_balloon as balloon


def main():
    """ Tests the   Balloon  class """
    test_init()
    test_blow_air_into()
    test_puncture()
    test_let_air_out()
    test_owners_age()
    test_fuller_balloon()
    test_new_balloon()
    test_unpunctured_balloons()


def test_init():
    print('------------------------------------')
    print('Testing __init__:')

    child1 = balloon.Person(6, 40)
    adult1 = balloon.Person(28, 130)
    adult2 = balloon.Person(40, 170)

    balloon1 = balloon.Balloon(1.4, child1)
    balloon2 = balloon.Balloon(4.0, adult1)
    balloon3 = balloon.Balloon(1.5, adult2)
    balloon4 = balloon.Balloon(2.0, child1)

    # Add code below here to continue this test:
    print(balloon1)
    print(balloon2)
    print(balloon3)
    print(balloon4)


def test_blow_air_into():
    print('\n------------------------------------')
    print('Testing blow_air_into:')

    child1 = balloon.Person(6, 40)
    adult1 = balloon.Person(28, 130)
    adult2 = balloon.Person(40, 170)

    balloon1 = balloon.Balloon(1.4, child1)
    balloon2 = balloon.Balloon(4.0, adult1)
    balloon3 = balloon.Balloon(1.5, adult2)
    balloon4 = balloon.Balloon(2.0, child1)

    # Add code below here to continue this test:
    balloon1.blow_air_into(3)
    print(balloon1.volume)
    print('above the volume should be (.09)')
    balloon2.blow_air_into(2)
    print(balloon2.volume)
    print('above the volume should be (1)')
    balloon3.blow_air_into(4)
    print(balloon3.volume)
    print('above the volume should be (0)')
    balloon4.blow_air_into(5)
    print(balloon4.volume)
    print('above the volume should be (.15)')


def test_puncture():
    print('\n------------------------------------')
    print('Testing puncture:')

    child1 = balloon.Person(6, 40)
    adult1 = balloon.Person(28, 130)
    adult2 = balloon.Person(40, 170)

    balloon1 = balloon.Balloon(1.4, child1)
    balloon2 = balloon.Balloon(4.0, adult1)
    balloon3 = balloon.Balloon(1.5, adult2)
    balloon4 = balloon.Balloon(2.0, child1)

    # Add code below here to continue this test:
    balloon1.puncture()
    print(balloon1)
    print('above should print balloon with capacity 0, volume 0')
    balloon2.puncture()
    print(balloon2)
    print('above should print a balloon wiht capacity 0, volume 0')


def test_let_air_out():
    print('\n------------------------------------')
    print('Testing let_air_out:')

    child1 = balloon.Person(6, 40)
    adult1 = balloon.Person(28, 130)
    adult2 = balloon.Person(40, 170)

    balloon1 = balloon.Balloon(1.4, child1)
    balloon2 = balloon.Balloon(4.0, adult1)
    balloon3 = balloon.Balloon(1.5, adult2)
    balloon4 = balloon.Balloon(2.0, child1)

    # Add code below here to continue this test:
    balloon3.let_air_out(3)
    print(balloon3.volume)
    print('above should print 0')
    balloon4.blow_air_into(5)
    air = .03 * 5
    balloon4.let_air_out(1)
    print(balloon4.volume)
    print('above should print', air - (.08 * 1))


def test_owners_age():
    print('\n------------------------------------')
    print('Testing owners_age:')

    child1 = balloon.Person(6, 40)
    adult1 = balloon.Person(28, 130)
    adult2 = balloon.Person(40, 170)

    balloon1 = balloon.Balloon(1.4, child1)
    balloon2 = balloon.Balloon(4.0, adult1)
    balloon3 = balloon.Balloon(1.5, adult2)
    balloon4 = balloon.Balloon(2.0, child1)

    # Add code below here to continue this test:
    print(balloon1.owners_age())
    print('above should print 6')
    print(balloon2.owners_age())
    print('above should print 28')


def test_fuller_balloon():
    print('\n------------------------------------')
    print('Testing fuller_balloon:')

    child1 = balloon.Person(6, 40)
    adult1 = balloon.Person(28, 130)
    adult2 = balloon.Person(40, 170)

    balloon1 = balloon.Balloon(1.4, child1)
    balloon2 = balloon.Balloon(4.0, adult1)
    balloon3 = balloon.Balloon(1.5, adult2)
    balloon4 = balloon.Balloon(2.0, child1)

    # Add code below here to continue this test:
    balloon2.blow_air_into(3)
    balloon3.blow_air_into(2)
    print(balloon2.fuller_balloon(balloon3))
    print('above should print balloon 2')
    balloon3.blow_air_into(1)
    print(balloon2.fuller_balloon(balloon3))
    print('above should print balloon 2')


def test_new_balloon():
    print('\n------------------------------------')
    print('Testing new_balloon:')

    child1 = balloon.Person(6, 40)
    adult1 = balloon.Person(28, 130)
    adult2 = balloon.Person(40, 170)

    balloon1 = balloon.Balloon(1.4, child1)
    balloon2 = balloon.Balloon(4.0, adult1)
    balloon3 = balloon.Balloon(1.5, adult2)
    balloon4 = balloon.Balloon(2.0, child1)

    # Add code below here to continue this test:
    print(balloon1.new_balloon())
    print(balloon2.new_balloon())


def test_unpunctured_balloons():
    print('\n------------------------------------')
    print('Testing unpunctured_balloons:')

    child1 = balloon.Person(6, 40)
    adult1 = balloon.Person(28, 130)
    adult2 = balloon.Person(40, 170)

    balloon1 = balloon.Balloon(1.4, child1)
    balloon2 = balloon.Balloon(4.0, adult1)
    balloon3 = balloon.Balloon(1.5, adult2)
    balloon4 = balloon.Balloon(2.0, child1)

    # Add code below here to continue this test:
    balloon1.puncture()
    balloon4.puncture()
    balloons = [balloon1, balloon2, balloon3, balloon4]
    balloon1.unpunctured_balloons(balloons)


# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
