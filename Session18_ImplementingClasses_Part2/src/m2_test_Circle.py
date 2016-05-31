"""
Tests the   Circle  class
that is defined in the imported   m2_Circle   module.

Authors: David Mutchler, Mark Hays, Michael Wollowski, Amanda Stouder,
         Chandan Rupakheti, Katie Dion, Claude Anderson, Delvin Defoe,
         Curt Clifton, Matt Boutell, Dave Fisher, their colleagues,
         and Brendan Goldacker.  October 2014.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE

import m1e_Point as pt
import m2_Circle as cir


def main():
    """
    Tests the   Circle   class defined in the imported   cir  module.
    """
    # DONE: Add code below (at the appropriate places)
    #       to test your   Circle   class as you implement it.
    #       Be sure that your tests print the EXPECTED results of the
    #       tests as well as the ACTUAL results from the function calls.
    print('------------------------------------')
    print('Testing __init__:')
    circle1 = cir.Circle(pt.Point(50, 50), 50)
    circle2 = cir.Circle(pt.Point(100, 150), 100)
    circle3 = cir.Circle(pt.Point(200, 200), 25)
    circle4 = cir.Circle(pt.Point(300, 100), 80)

    print(circle1)
    print(circle2)

    print('\n------------------------------------')
    print('Testing __repr__:')

    print(circle1.__repr__())
    print(circle2.__repr__())

    print('\n------------------------------------')
    print('Testing clone:')

    print(circle1.clone())
    print(circle2.clone())

    print('\n------------------------------------')
    print('Testing move_by:')

    circle1.move_by(50, 50)
    print(circle1)
    print('above should be a circle with a center at (100, 100)')

    circle3.move_by(-50, 100)
    print(circle3)
    print('above should be a circle with a center at (150, 350)')

    print('\n------------------------------------')
    print('Testing intersects:')

    print(circle1.intersects(circle2))
    print('above should print True')

    print(circle3.intersects(circle4))
    print('above should print False')

    print('\n------------------------------------')
    print('Testing closer_to_origin:')

    print(circle1.closer_to_origin(circle2))
    print('above should be cirle1')

    print(circle3.closer_to_origin(circle4))
    print('above shoul be circle4')

    print('\n------------------------------------')
    print('Testing super_circle:')

    print(circle1.super_circle(circle2))
    print('above shoud be a circle with a center(100, 125) and a radius of ')


# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
