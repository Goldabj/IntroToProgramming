"""
This module uses ZELLEGRAPHICS to demonstrate:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES (aka FIELDS).

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, Matt Boutell,
         and their colleagues. December 2013.
"""
#-----------------------------------------------------------------------
# Students: Read and run this program.
#
#           Also, WITH YOUR INSTRUCTOR, learn to use the DOT trick:
#               rg.           and rg.Circle().
#           to POP UP help from which you can learn how to use
#           objects of a class that you have never seen before.
#           (And the HOVER over a class or method to get its code.)
#
# There is nothing to turn in from this file.
# Just use it as an example to see and learn:
#   -- How to CONSTRUCT an object
#   -- How to APPLY A METHOD to an object (who_dot_doesWhat_withWhat)
#   -- How to ACCESS an INSTANCE VARIABLE of an object (who_dot_what)
#   -- the DOT andd HOVER pop-up tricks
#-----------------------------------------------------------------------

import rosegraphics as rg


def main():
    """
    Uses ZELLEGRAPHICS to demonstrate:
      -- CONSTRUCTING objects,
      -- applying METHODS to them, and
      -- accessing their DATA via INSTANCE VARIABLES (aka FIELDS)
    """
    width = 700
    height = 400
    window = rg.RoseWindow(width, height)
    # Construct a rg.Point.  Note: the y-axis goes DOWN from the TOP
    center_point = rg.Point(300, 100)
    point1 = rg.Point(100, 150)
    point2 = rg.Point(200, 50)

    radius = 50
    circle = rg.Circle(center_point, radius)
    rectangle = rg.Rectangle(point1, point2)

    circle.fill_color = 'orange'

    circle.attach_to(window.main_canvas)

    window.main_canvas.render(3)

    rectangle.attach_to(window.main_canvas)
    circle.fill_color = 'blue'

    window.main_canvas.render()

    corner1 = rectangle.one_corner
    corner2 = rectangle.opposite_corner

    print(corner1, corner2)
    print(rectangle)

    window.close_on_mouse_click()

#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
