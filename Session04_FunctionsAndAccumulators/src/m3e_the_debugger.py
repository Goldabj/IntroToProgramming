"""
A simple program in which you can try out the DEBUGGER.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, Matt Boutell,
         and their colleagues. December 2013.
"""
# ----------------------------------------------------------------------
# Students: Run this program in the DEBUGGER, by using the "BUG" symbol
#           just to the left of the usual RUN (green arrow) symbol.
#           Experiment with the Debugger, with your instructor's help:
#             -- Set (and later remove) some breakpoints.
#             -- Run to the next breakpoint(s).
#             -- Try Step Into.
#             -- Try Step Over and Step Return.
#             -- Examine variables.
#                Expand some objects to see their fields.
#             -- Terminate, then restart the debugger.
#             -- Note the interaction between the debugger and the
#                graphics window, especially when the graphics window
#                is waiting for a mouse click.
# ----------------------------------------------------------------------

import math
import rosegraphics as rg


def main():
    """ Calls  draw_circles   to demonstrate it. """
    draw_circles(5, 'green')  # Draws 5 green circles
    draw_circles(3, 'blue')  # Draws 3 blue circles


def draw_circles(n, color):
    """
    Constructs a rg.GraphWin and draws n circles on it.
    Also prints some variables, just to serve as examples.
    """
    window = rg.RoseWindow(400, 200)
    x = 100
    y = 50
    radius = 25
    for k in range(n):
        sink = math.sin(k)
        k_to_kth = k ** k
        print(k, sink, k_to_kth, x, y)

        p = rg.Point(x, y)
        c = rg.Circle(p, radius)
        c.fill_color = color


        c.attach_to(window.initial_canvas)
        p.attach_to(window.initial_canvas)
        window.render(1)

        p.move_by(10, 10)
        window.render(1)

        x = x + (2 * radius)
        y = y + radius

    window.close_on_mouse_click()

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
