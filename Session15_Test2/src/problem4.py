"""
Test 2, problem 4.

Authors: Mark Hays, David Mutchler, Michael Wollowski, their colleagues,
         and Brendan Goldacker.  October 2014.
"""  # DONE: PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the   TEST   functions in this module. """
    test_problem4a()
    test_problem4b()


def test_problem4a():
    """ Tests the   problem4a   function. """
    # ------------------------------------------------------------------
    # We have implemented this function for you.  You are welcome
    # to add more tests if you wish, but you do not have to do so.
    # These tests produce the pictures shown in the attached
    #    problem4a_picture.pdf.
    # ------------------------------------------------------------------
    window1 = rg.RoseWindow(600, 300, 'Problem 4a, tests 1 and 2')

    # Test 1:
    center = rg.Point(50, 50)
    circle = rg.Circle(center, 20)

    corner = rg.Point(180, 160)
    rectangle = rg.Rectangle(corner, 60, 80)

    problem4a(window1, circle, rectangle, 'blue', 'red')

    window1.continue_on_mouse_click()

    # Test 2:
    center = rg.Point(350, 200)
    circle = rg.Circle(center, 60)

    corner = rg.Point(450, 110)
    rectangle = rg.Rectangle(corner, 100, 60)

    problem4a(window1, circle, rectangle, 'yellow', 'green')

    window1.close_on_mouse_click()

    # Test 3:
    window2 = rg.RoseWindow(350, 200, 'problem 4a, test 3')

    center = rg.Point(250, 80)
    circle = rg.Circle(center, 25)

    corner = rg.Point(100, 65)
    rectangle = rg.Rectangle(corner, 100, 70)

    problem4a(window2, circle, rectangle, 'cyan', 'black')

    window2.close_on_mouse_click()


def problem4a(window, circle, rectangle, circle_color, rectangle_color):
    """
    See   problem4a_picture.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws a circle, a rectangle and 4 lines as follows:
      -- The circle should be the given circle,
           but with its FILL color set to the given  circle_color.
      -- The rectangle should be the given rectangle,
           but with its OUTLINE color set to the given  rectangle_color.
      -- The 4 lines each have one end at the center of the given circle
           and the other end at a corner of the rectangle.
           (The rectangle has 4 corners; one line to each.)
           The lines should be drawn AFTER drawing the circle and
           rectangle, so that the lines are on TOP of the circle
           and rectangle.
     -- The circle and rectangle should have their outline thickness
           set to 3 (instead of the default 1).  Similarly, the lines
           should have their thickness set to 3.

    Preconditions:
      :type window: rg.RoseWindow
      :type circle: rg.Circle
      :type rectangle: rg.Rectangle
      :type circle_color (str, rg.Color)
      :type rectangle_color (str, rg.Color)
    and the two color arguments are colors appropriate for rosegraphics.
    """
    # ------------------------------------------------------------------
    # DONE: Implement and test this function.
    # NOTE: Partial credit is available if you can draw
    #       only parts of what is asked for.
    # ------------------------------------------------------------------
    circle.fill_color = circle_color
    rectangle.outline_color = rectangle_color

    point1 = rg.Point(rectangle.center.x - rectangle.width / 2, rectangle.center.y - rectangle.height / 2)
    point2 = rg.Point(rectangle.center.x - rectangle.width / 2, rectangle.center.y + rectangle.height / 2)
    point3 = rg.Point(rectangle.center.x + rectangle.width / 2, rectangle.center.y - rectangle.height / 2)
    point4 = rg.Point(rectangle.center.x + rectangle.width / 2, rectangle.center.y + rectangle.height / 2)

    line1 = rg.Line(circle.center, point1)
    line2 = rg.Line(circle.center, point2)
    line3 = rg.Line(circle.center, point3)
    line4 = rg.Line(circle.center, point4)

    circle.outline_thickness = 3
    rectangle.outline_thickness = 3
    line1.thickness = 3
    line2.thickness = 3
    line3.thickness = 3
    line4.thickness = 3

    circle.attach_to(window.initial_canvas)
    rectangle.attach_to(window.initial_canvas)
    line1.attach_to(window.initial_canvas)
    line2.attach_to(window.initial_canvas)
    line3.attach_to(window.initial_canvas)
    line4.attach_to(window.initial_canvas)

def test_problem4b():
    """ Tests the   problem4b   function. """
    # ------------------------------------------------------------------
    # We have implemented this function for you.  You are welcome
    # to add more tests if you wish, but you do not have to do so.
    # These tests produce the pictures shown in the attached
    #    problem4b_picture.pdf.
    # ------------------------------------------------------------------
    window1 = rg.RoseWindow(350, 650, 'Problem 4b, test 1')

    # Test 1:
    point1 = rg.Point(250, 80)
    rectangle1 = rg.Rectangle(rg.Point(50, 30), 50, 30)
    colors1 = ['blue', 'red', 'green', 'white', 'cyan', 'yellow',
               'brown', 'pink']

    problem4b(window1, 7, point1, rectangle1, colors1)

    window1.close_on_mouse_click()

    window2 = rg.RoseWindow(500, 650, 'Problem 4b, tests 2 and 3')

    # Test 2:
    point2 = rg.Point(40, 40)
    rectangle2 = rg.Rectangle(rg.Point(100, 20), 40, 10)
    colors2 = ['blue', 'red', 'green']

    problem4b(window2, 8, point2, rectangle2, colors2)
    window1.continue_on_mouse_click()

    # Test 3:
    point3 = rg.Point(200, 80)
    rectangle3 = rg.Rectangle(rg.Point(400, 100), 80, 50)

    problem4b(window2, 6, point3, rectangle3, colors2)

    window2.close_on_mouse_click()


def problem4b(window, n, point, rectangle, colors):
    """
    See   problem4b_picture.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws  n  "things" as follows:
      -- Each "thing" consists of a circle, a rectangle, and 4 lines,
           as in problem3a.
      -- The first "thing" has:
           -- Its rectangle is the given rectangle.
           -- Its circle is centered at the given point.
           -- The radius of the circle is half of the width
                of the rectangle.
           -- Its 4 lines go from the center of the circle
                to the 4 corners of the rectangle, as in problem3a.
           -- The fill color of the circle is the first (beginning)
                color in the given list of colors.
           -- The outline color of the rectangle is the second color
                in the given list of colors.
      -- Each succeeding "thing" has the same size and relationships
           as the first thing, but is shifted 70 pixels down
           from the previous "thing".
      -- Also, the circles have fill colors per the given list of
           colors, one after the other, starting at the first
           (beginning) color, wrapping as necessary.
      -- Also, the rectangles have outline colors per the given
           list of colors, one after the other, wrapping as necessary,
           but starting at the SECOND color in the list.

    Preconditions:
      :type window: rg.RoseWindow
      :type n: int
      :type point: rg.Point
      :type rectangle: rg.Rectangle
      :type colors: (list, tuple)
    and n is non-negative
    and colors is a sequence of colors appropriate for rosegraphics.
    """
    # ------------------------------------------------------------------
    # DONE: Implement and test this function.  Partial credit
    #       is available if you get only part of this to work.
    #
    # IMPORTANT:  Use (call) the above   problem4a function as needed
    #             in this problem.
    # ------------------------------------------------------------------
    pointR = rectangle.center
    for k in range(n):
        circle = rg.Circle(point, rectangle.width / 2)
        rectangle = rg.Rectangle(pointR, rectangle.width, rectangle.height)
        problem4a(window, circle, rectangle, colors[k], colors[k + 1])
        window.render(.5)
        if k >= len(colors) - 2:
            colors = colors * 2
        point.y = point.y + 70
        pointR.y = pointR.y + 70



# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
