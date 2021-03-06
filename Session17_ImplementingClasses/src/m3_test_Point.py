"""
Tests the   Point  class
that is defined in the imported   m3_Point   module.

Authors: David Mutchler, Mark Hays, Michael Wollowski, Amanda Stouder,
         Chandan Rupakheti, Katie Dion, Claude Anderson, Delvin Defoe,
         Curt Clifton, Matt Boutell, Dave Fisher, their colleagues,
         and Brendan Goldacker.  October 2014.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE

import m3_Point as pt


def main():
    """
    Tests the   Point   class defined in the imported   pt  module.
    """
    # TODO: Add code below (at the appropriate places)
    #       to test your   Point   class as you implement it.
    print('------------------------------------')
    print('Testing __init__:')

    p1 = pt.Point(200, 300)
    p2 = pt.Point(y=-50.3)

    print(p1.x, p1.y)
    print('above should be 200 and 300')

    print(p2.x, p2.y)
    print('above should be 0 and -50.3')

    print('\n------------------------------------')
    print('Testing __repr__:')

    print(p1.__repr__())
    print(p2.__repr__())

    print('\n------------------------------------')
    print('Testing move_to:')

    p1.move_to(20, 80)
    p2.move_to(200, 300)

    print(p1.__repr__())
    print('above should be (20, 80)')

    print(p2.__repr__())
    print('above should be (200, 300)')

    print('\n------------------------------------')
    print('Testing move_by:')

    p1.move_by(30, 80)
    p2.move_by(50, -100)

    print(p1.__repr__())
    print('above should be (50, 160)')

    print(p2.__repr__())
    print('above should be (250, 200)')

    print('\n------------------------------------')
    print('Testing distance_from:')

    p3 = pt.Point(50, 50)
    p4 = pt.Point(200, 400)

    print(p1.distance_from(p3))
    print('above should be 110')

    print(p2.distance_from(p4))
    print('above should be 206.155')

    print('\n------------------------------------')
    print('Testing closer_to:')

    print(p1.closer_to(p2, p3))
    print('above should be p3')

    print(p2.closer_to(p4, p3))
    print('above should be p4')

    print('\n------------------------------------')
    print('Testing halfway_to:')

    print(p1.halfway_to(p4))
    print('above should be (125, 280)')

    print(p2.halfway_to(p3))
    print('above should be (150, 125)')

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
