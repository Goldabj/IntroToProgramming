"""
This module lets you see the Create ROBOT in a SIMULATOR.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, Matt Boutell,
         Dave Fisher and their colleagues. January 2014.
"""
# ----------------------------------------------------------------------
# Just an example to remind you how robots work.
# ----------------------------------------------------------------------

import new_create
import time


def main():
    """ Demonstrates the use of the Create Robot's SIMULATOR. """
    port = 'sim'  # Note the quotes.
    robot = new_create.Create(port)

    robot.driveDirect(30, -30)
    time.sleep(3)
    robot.stop()

    robot.shutdown()

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
