"""
A simple   Rectangle   class.
NOTE: This is NOT rosegraphics -- it is your OWN Rectangle class.

Authors: David Mutchler, Mark Hays, Michael Wollowski, Amanda Stouder,
         Chandan Rupakheti, Katie Dion, Claude Anderson, Delvin Defoe,
         Curt Clifton, Matt Boutell, Dave Fisher and their colleagues,
         and Brendan Goldacker.  October 2014.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import m1e_Point as pt
import m2_Circle as cir
import math


def main():
    """ Not used here, but could be used for informal testing. """
    # Put your tests in the   m3_test_Rectangle  module, NOT here.
    pass


# ----------------------------------------------------------------------
# TODO:  Define here a class called   Rectangle   that represents a
#        rectangle whose sides are parallel to the x and y axes.
#        It has:
#   Instance variables:
#     -- corner1 (stored as a Point)
#     -- corner2 (stored as a Point)
#          where corner2 is the corner of the Rectangle opposite corner1
#        Do NOT assume that corner1 is any particular corner -- allow
#        for it to be any of the 4 possible corners.
#   Methods:
#     __init__: Takes two required parameters, corner1 and corner2,
#               both of which must be Point objects.
#               Sets this Rectangle's opposite corners
#               to the given points.
#     __repr__: Returns a string that represents this Rectanle
#               as in this example:
#                 'Rectangle(corners = Point(100, 32.7), Point(50, 90))'
#     clone:    Returns a new Rectangle that is a copy of this Rectangle.
#     move_by:  Takes two arguments, dx and dy, both numbers.
#               Moves this Rectangle by dx and dy, respectively.
#     corners:  Returns a list of the 4 Point objects that are corners
#               of this Rectangle.
#     contains: Takes a Point p.
#               Returns True if this Rectangle contains p,
#               else returns False.  We will say that the Rectangle
#               DOES contain p if p is on the Rasectangle's border.
#     intersects:  Takes another Rectange  an argument.
#                  Returns True if this Rectangle and the other
#                  Rectangle intersect, else returns False.
#                    -- Hint: they intersect if one of the Rectangles
#                       contains at least one of the corners
#                       of the other Rectangle.
#     sub_circle:  Returns the largest Circle that fits inside
#                  this Rectangle and is centered within this Rectangle.
#     super_rectangle: Takes a list of Rectangles as an argument.
#                      Returns a new Rectangle that is the smallest
#                      Rectangle that contains all the Rectangles in
#                      the given list.
#
# Include appropriate docstrings with the methods that you define
# (copy-and-paste from the above makes it easy to do so).
# Test your class definition using the   m2_test_Rectangle    module.
#   ** TEST EACH METHOD AS YOU DEFINE IT. **
#
# Wherever reasonable, CALL methods previously defined rather than
# copying the code of those methods.
# ----------------------------------------------------------------------

class Rectangle(object):

    def __init__(self, corner1=pt.Point(0, 0), corner4=pt.Point(0, 0)):
        """Takes two required parameters, corner1 and corner2,
         both of which must be Point objects.
          Sets this Rectangle's opposite corners
           to the given points."""
        self.corner1 = corner1
        self.corner4 = corner4
        self.corner2 = pt.Point(self.corner4.x, self.corner1.y)
        self.corner3 = pt.Point(self.corner1.x, self.corner4.y)

        height = (self.corner4.y - self.corner1.y)
        if height < 0:
            height = (self.corner1.y - self.corner4.y)
        length = (self.corner4.x - self.corner1.x)
        if length < 0:
            length = (self.corner1.x - self.corner4.x)
        self.height = height
        self.length = length


    def __repr__(self):
        """Returns a string that represents this Rectanle"""
        format_string = 'Rectangle(corners at ({}) and ({})'.format(self.corner1, self.corner4)
        return format_string

    def clone(self):
        """Returns a new Rectangle that is a copy of this Rectangle."""
        new_rectangle = self
        return new_rectangle

    def move_by(self, dx, dy):
        """Moves this Rectangle by dx and dy, respectively"""
        self.corner1.x = self.corner1.x + dx
        self.corner1.y = self.corner1.y + dy
        self.corner4.x = self.corner4.x + dx
        self.corner4.y = self.corner4.y + dy

    def corners(self):
        """Returns a list of the 4 Point objects that are corners
         of this Rectangle."""
        self.corner2 = pt.Point(self.corner4.x, self.corner1.y)
        self.corner3 = pt.Point(self.corner1.x, self.corner4.y)
        corners = [self.corner1, self.corner2, self.corner3, self.corner4]
        return corners

    def contains(self, p):
        """Returns True if this Rectangle contains p,
           else returns False.  We will say that the Rectangle
          DOES contain p if p is on the Rasectangle's border."""
        between_x = (self.corner1.x + self.corner4.x) / 2
        between_y = (self.corner1.y + self.corner4.y) / 2
        if p.x < between_x + self.length / 2 and p.x > between_x - self.length / 2:
            if p.y < between_y + self.height / 2 and p.y > between_y - self.height / 2:
                return True
            else:
                return False
        else:
            return False

    def intersects(self, rect2):
        """ Returns True if this Rectangle and the other
           Rectangle intersect, else returns False"""
        if self.contains(rect2.corner1):
            return True
        if self.contains(rect2.corner2):
            return True
        if self.contains(rect2.corner3):
            return True
        if self.contains(rect2.corner4):
            return True
        return False

    def sub_circle(self):
        """Returns the largest Circle that fits inside
             this Rectangle and is centered within this Rectangle."""
        center_x = (self.corner1.x + self.corner4.x) / 2
        center_y = (self.corner1.y + self.corner4.y) / 2
        center = pt.Point(center_x, center_y)
        if self.height > self.length:
            radius = self.length / 2
        if self.length >= self.height:
            radius = self.height / 2
        circle = cir.Circle(center, radius)
        return circle
#
#     def super_rectangle(self, rectangles):
#         rectangle_largex = 0
#         for k in range(len(rectangles)):
#


# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
