"""
A simple   Circle   class.
NOTE: This is NOT rosegraphics -- it is your OWN Circle class.

Authors: David Mutchler, Mark Hays, Michael Wollowski, Amanda Stouder,
         Chandan Rupakheti, Katie Dion, Claude Anderson, Delvin Defoe,
         Curt Clifton, Matt Boutell, Dave Fisher and their colleagues,
         and Brendan Goldacker.  October 2014.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import m1e_Point as pt


def main():
    """ Not used here, but could be used for informal testing. """
    # Put your tests in the   m2_test_Circle  module, NOT here.
    pass


# ----------------------------------------------------------------------
# DONE:  Define here a class called   Circle   that represents a circle.
#        It has:
#   Instance variables:
#     -- center (stored as a Point)
#     -- radius
#   Methods:
#     __init__: Takes two optional parameters, center and radius.
#               Sets this Circle's center and radius to the given values.
#               The defaults are a Point at (0, 0) and a radius of 1.
#     __repr__: Returns a string that represents this Circle
#               as in this example:
#                 'Circle(center = Point(100, 32.7), radius = 43)'
#     clone:    Returns a new Circle that is a copy of this Circle.
#     move_by:  Takes two arguments, dx and dy, both numbers.
#               Increases the x and y of this Circle's center
#               by dx and dy, respectively.
#     intersects:  Takes another Circle as an argument.
#                  Returns True if this Circle and the other Circle
#                  intersect, else returns False.  (If they barely
#                  touch, we will NOT call that an "intersection.")
#                    -- Hint: they intersect if the distance from their
#                       centers is less than the sum of their radii.
#     closer_to_origin: Takes another Circle as an argument.
#                       Returns this Circle or the other Circle,
#                       whichever one's center is closer to (0, 0).
#                       Breaks ties in favor of this Circle.
#     super_circle: Takes another Circle as an argument.
#                   Returns a new Circle that is the smallest Circle
#                   that contains both this Circle and the other Circle.
#
# Include appropriate docstrings with the methods that you define
# (copy-and-paste from the above makes it easy to do so).
# Test your class definition using the   m2_test_Circle    module.
#   ** TEST EACH METHOD AS YOU DEFINE IT. **
#
# Wherever reasonable, CALL methods previously defined rather than
# copying the code of those methods.
# ----------------------------------------------------------------------

class Circle(object):

    def __init__(self, center=pt.Point(0, 0), radius=1):
        """Sets this Circle's center and radius to the given values.
           The defaults are a Point at (0, 0) and a radius of 1."""
        self.center = center
        self.radius = radius

    def __repr__(self):
        """Returns a string that represents this Circle"""
        format_string = 'Cricle(center = Point({}), radius = {})'.format(self.center, self.radius)
        return format_string

    def clone(self):
        """Returns a new Circle that is a copy of this Circle."""
        new_circle = self
        return new_circle

    def move_by(self, dx, dy):
        """Increases the x and y of this Circle's center
            by dx and dy, respectively."""
        new_center = self.center.move_by(dx, dy)
        return new_center

    def intersects(self, circle2):
        """Takes another Circle as an argument.
           Returns True if this Circle and the other Circle
            intersect, else returns False."""
        if self.center.distance_from(circle2.center) < (self.radius + circle2.radius):
            return True
        else:
            return False

    def closer_to_origin(self, circle2):
        """Returns this Circle or the other Circle,
             whichever one's center is closer to (0, 0)."""
        if self.center.distance_from(pt.Point()) < circle2.center.distance_from(pt.Point()):
            return self
        else:
            return circle2

    def super_circle(self, circle2):
        """Returns a new Circle that is the smallest Circle
        that contains both this Circle and the other Circle"""
        new_circle_center = (self.center.halfway_to(circle2.center))
        new_circle_radius2 = new_circle_center.distance_from(pt.Point((circle2.center.x + circle2.radius), (circle2.center.y + circle2.radius)))
        new_circle_radius1 = new_circle_center.distance_from(pt.Point((self.center.x + self.radius), (self.center.y + self.radius)))
        if new_circle_radius1 >= new_circle_radius2:
            new_circle_radius = new_circle_radius1
        else:
            new_circle_radius = new_circle_radius2
        new_circle = Circle(new_circle_center, new_circle_radius)
        return new_circle


# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
