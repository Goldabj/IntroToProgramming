"""
A simple   Point   class.
NOTE: This is NOT rosegraphics -- it is your OWN Point class.

Authors: David Mutchler, Mark Hays, Michael Wollowski, Amanda Stouder,
         Chandan Rupakheti, Katie Dion, Claude Anderson, Delvin Defoe,
         Curt Clifton, Matt Boutell, Dave Fisher and their colleagues,
         and Brendan Goldacker.  October 2014.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Not used here, but could be used for informal testing. """
    # Put your tests in the   m3_test_Point  module, NOT here.
    pass


# TODO:  Define here a class called   Point
#        that represents a point in two dimensions.
#        It has:
#   Instance variables:  x and y, for its two coordinates.
#   Methods:
#     __init__: Takes two optional arguments, x and y, both numbers.
#               Sets this Point's coordinates to the given x and y.
#               The defaults for x and y are 0.
#     __repr__: Returns a string that represents this Point
#               as in this example:  'Point(100, 32.7)'
#     move_to:  Takes two arguments, x and y, both numbers.
#               Sets this Point's x and y to those values.
#     move_by:  Takes two arguments, dx and dy, both numbers.
#               Increases this Point's x and y by those values.
#     distance_from:  Takes a Point and returns the distance
#                     that this Point is from the given Point.
#     closer_to:  Takes two Points p2 and p3.
#                 Returns whichever of p2 and p3 is closer
#                 to this Point.  (Returns p2 if they are tied).
#     halfway_to:  Takes a Point.
#                  Returns a new Point whose x coordinate is
#                  the average of the x-coordinates of this Point
#                  and the given Point, and whose y coordinate is
#                  the average of the y-coordinates of this Point
#                  and the given Point.
#
# Include appropriate docstrings with the methods that you define
# (copy-and-paste from the above makes it easy to do so).
# Test your class definition using the   m3_test_Point    module.
#   ** TEST EACH METHOD AS YOU DEFINE IT. **

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------

class Point(object):
    """represents a point in two dimensions"""

    def __init__(self, x=0, y=0):
        """Sets this Point's coordinates to the given x and y."""
        self.x = x
        self.y = y

    def __repr__(self):
        format_string = '({}, {})'
        return format_string.format(self.x, self.y)

    def move_to(self, x2, y2):
        """akes two arguments, x and y, both numbers.
             Sets this Point's x and y to those values."""
        self.x = x2
        self.y = y2
        return Point(x2, y2)

    def move_by(self, dx, dy):
        """moves the point by the given distances of x and y"""
        self.x = self.x + dx
        self.y = self.y + dy
        return self

    def distance_from(self, other_point):
        distance = ((other_point.x - self.x) ** 2 + (other_point.y - self.y) ** 2) ** (1 / 2)
        return distance

    def closer_to(self, p2, p3):
        """Takes two Points p2 and p3.Returns whichever of p2 and p3 is closer
                to this Point.  (Returns p2 if they are tied)."""
        p2_distance = self.distance_from(p2)
        p3_distance = self.distance_from(p3)
        if p2_distance > p3_distance:
            return p3
        if p3_distance >= p2_distance:
            return p2

    def halfway_to(self, point2):
        """Returns a new Point whose x coordinate is the average of the x-coordinates of this Point
                 and the given Point, and whose y coordinate is the average of the y-coordinates 
                 of this Point andd the given Point."""
        new_x = (self.x + point2.x) / 2
        new_y = (self.y + point2.y) / 2
        return Point(new_x, new_y)


if __name__ == '__main__':
    main()
