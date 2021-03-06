"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Brendan Goldacker.  February 2014.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to test them. """
    test_draw_upside_down_wall()


def test_draw_upside_down_wall():
    """ Tests the    draw_upside_down_wall    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Upside-down wall, Tests 1 and 2')

    rectangle = rg.Rectangle(rg.Point(140, 240), 30, 20)
    draw_upside_down_wall(rectangle, 8, window)

    rectangle = rg.Rectangle(rg.Point(400, 200), 50, 50)
    draw_upside_down_wall(rectangle, 4, window)

    window.close_on_mouse_click()


def draw_upside_down_wall(rectangle, n, window):
    """
    See   Walls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an "upside-down wall" where:
      -- The BOITOM of the wall is a single "brick"
            that is the given rg.Rectangle.
      -- There are n rows in the wall.
      -- Each row is a row of "bricks" that are the same size
            as the given rg.Rectangle.
      -- Each row has one more brick than the row below it.
      -- Each row is centered on the bottom row.

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is nonnegative.
    """
    # ------------------------------------------------------------------
    # TODO: 2. Implement and test this function.
    #     The testing code is already written for you (above).
    # ------------------------------------------------------------------
    original_x = rectangle.center.x
    original_y = rectangle.center.y

    x = original_x
    y = original_y
    for k in range(n):
        for j in range(2, (k + 1)):
            for t in range(2):
                x = original_x + (t * rectangle.width / 2)
                new_rect = rg.Rectangle(rg.Point(x, y), rectangle.width, rectangle.height)
                new_rect.attach_to(window.initial_canvas)
            x = original_x + (j * rectangle.width)
            new_rect = rg.Rectangle(rg.Point(x, y), rectangle.width, rectangle.height)
            new_rect.attach_to(window.initial_canvas)
        for q in range(2, (k + 1)):
            for t in range(2):
                x = original_x - (t * rectangle.width / 2)
                new_rect = rg.Rectangle(rg.Point(x, y), rectangle.width, rectangle.height)
                new_rect.attach_to(window.initial_canvas)
            x = original_x - (q * rectangle.width)
            new_rect = rg.Rectangle(rg.Point(x, y), rectangle.width, rectangle.height)
            new_rect.attach_to(window.initial_canvas)
        y = y - rectangle.height


# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
