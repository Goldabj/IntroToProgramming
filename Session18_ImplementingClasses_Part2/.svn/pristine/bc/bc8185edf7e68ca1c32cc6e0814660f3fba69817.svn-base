"""
Tests the   Rectangle  class
that is defined in the imported   m3_Rectangle   module.

Authors: David Mutchler, Mark Hays, Michael Wollowski, Amanda Stouder,
         Chandan Rupakheti, Katie Dion, Claude Anderson, Delvin Defoe,
         Curt Clifton, Matt Boutell, Dave Fisher, their colleagues,
         and Brendan Goldacker.  October 2014.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE

import m1e_Point as pt
import m2_Circle as cir
import m3_Rectangle as rect


def main():
    """
    Tests the   Rectangle   class defined in the imported  rect module.
    """
    # TODO: Add code below (at the appropriate places)
    #       to test your   Rectangle   class as you implement it.
    #       Be sure that your tests print the EXPECTED results of the
    #       tests as well as the ACTUAL results from the function calls.
    print('------------------------------------')
    print('Testing __init__:')

    r1 = rect.Rectangle(pt.Point(200, 200), pt.Point(100, 100))
    r2 = rect.Rectangle(pt.Point(50, 50), pt.Point(150, 150))
    r3 = rect.Rectangle(pt.Point(100, 100), pt.Point(175, 175))
    r4 = rect.Rectangle(pt.Point(250, 250), pt.Point(300, 300))

    print(r1.corner1, r1.corner4)
    print(r2.corner1, r2.corner4)

    print('\n------------------------------------')
    print('Testing __repr__:')

    print(r1)
    print('above should print rectangle with corners at (200, 200) and (100, 100)')

    print(r2)
    print('above should print rectangle with corners at (50, 50) and (150 , 150)')

    print('\n------------------------------------')
    print('Testing clone:')

    print(r2.clone())
    print('above should be rectangle with corners at (50, 50) and (150, 150)')

    print('\n------------------------------------')
    print('Testing move_by:')

    r1.move_by(100, 100)
    print(r1)
    print('above should print a rectangle with corners at (300, 300) and (200, 200)')

    r2.move_by(-50, -50)
    print(r2)
    print('above should print a rectangle with conrers at (0, 0) and (100, 100)')

    print('\n------------------------------------')
    print('Testing corners:')

    print(r1.corners())
    print('above should print [(300, 300), (200, 300), (300, 200), (200, 200)]')
    print(r2.corners())
    print('above should print [(0, 0), (100, 0), (0, 100), (100, 100)]')

    print('\n------------------------------------')
    print('Testing contains:')

    print(r1.contains(pt.Point(75, 75)))
    print('above should print Fasle')

    print(r2.contains(pt.Point(75, 75)))
    print('above should print True')

    print('\n------------------------------------')
    print('Testing intersects:')

    print(r1.intersects(r3))
    print('above should print Flase')

    print(r1.intersects(r4))
    print('above shoud print True')

    print('\n------------------------------------')
    print('Testing sub_circle:')

    print(r1.sub_circle())
    print('above should be a cirlce with center (250, 250) and radius (50)')

    print(r2.sub_circle())
    print('above should be a circle with center (50, 50) and radius 50')

    print('\n------------------------------------')
    print('Testing super_rectangle:')




# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
