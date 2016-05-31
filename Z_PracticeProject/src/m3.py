"""
The  **** PRACTICE **** Python Capstone Project.

CSSE 120 - Introduction to Software Development.
Team members: Brendan Goldacker, Scott Reiter, and Alan Yates.

The primary author of this module is: Alan Yates.
"""
# DONE: Put the names of ALL team members in the above where indicated.
#       Put YOUR NAME in the above where indicated.

import m0
import m1
import m2
import m4

import time
import tkinter
from tkinter import ttk
import new_create


# ----------------------------------------------------------------------
# TODO: Do the following in STAGES, using ITERATIVE ENHANCEMENT.
#       That means that for each stage, you implement it, TEST it,
#       COMMIT your work WITH A SHORT, REASONABLE MESSAGE,
#       and then and only then continue to the next stage.
#
# Your ultimate goal for your part of this Practice Project is to have
# a correctly function button:
#   -- Go N centimeters
# plus two entry boxes in which the user can enter:
#   -- speed at which the robot is to move
#   -- centimeters the robot is to move
#
# Use the following ITERATIVE ENHANCEMENT PLAN, where each stage
# augments the preceding stages:
#
#   Stage 1: Frame appears with the button and Entry boxes on it.
#
#   Stage 2: Button prints a message, as a stub.
#              -- A STUB is placeholder code that lets you do some
#                 testing even before you have finished the real code.
#
#   Stage 3: Button prints the values of the two entry boxes,
#              again as a stub.
#
#   Stage 4: Button works correctly.
#              That is, pressing it causes a robot to move at the speed
#              in the first entry box, for the number of centimeters
#              in the second entry box.
#
#   NOTES:
#     You will have to decide where in your code it is best to construct
#     the robot, and where it is best to do a robot shutdown.
#     Keep in mind that:
#       -- You will eventually use your teammate's connect and
#          disconnect buttons to construct the robot.
#       -- That same robot will eventually be used throughout the code.
#
#     TEST using the SIMULATOR for now.
#
# Do ALL your work in THIS file.  Do not touch m0!
# You will INTEGRATE work in the NEXT session, using m0 to do so.
# ----------------------------------------------------------------------

class DataContainer3():
    """ A container for the data shared across the application. """

    def __init__(self):
        """ Initializes instance variables (fields). """
        # Add     self.FOO = BLAH     here as needed.


def main():
    """
    Tests functions in this module.
    Intended to be used internally by the primary author of this module.
    """
    print('-------------------------------')
    print('Testing functions in module m3:')
    print('-------------------------------')
    root = tkinter.Tk()
    dc = m1.DataContainer1

    frame1 = m1.my_frame(root, dc)
    frame1.grid()

    frame3 = my_frame(root, dc)
    frame3.grid()

    frame2 = m2.my_frame(root, dc)
    frame2.grid()

    root.mainloop()

def my_frame(root, dc):
    """
    Constructs and returns a Frame (on the given root window)
    that contains this module's widgets.
    Also sets up callbacks for this module's widgets.

    Preconditions:
      :type root: tkinter.Tk
      :type data: DataContainer3
    """
# Stage 1

    robot = m1.DataContainer1


    frame = ttk.Frame(root, padding=30, relief='raised')

    go_button = ttk.Button(frame, text='Go N centimeters')
    go_button.grid()
    go_button['command'] = lambda: move_N_cm(speed_entry, dist_entry, dc)

    speed_label = ttk.Label(frame, text='robot speed:')
    speed_entry = ttk.Entry(frame, width=10)
    dist_label = ttk.Label(frame, text='N centimeters:')
    dist_entry = ttk.Entry(frame, width=10)
    speed_label.grid()
    speed_entry.grid()
    dist_label.grid()
    dist_entry.grid()

    return frame

# Stage 2/3/4

def move_N_cm(speed_entry, dist_entry, dc):
    """
    moves robot N centimeters at an entered speed
    """
    speed = int(speed_entry.get())
    dist = int(dist_entry.get())
    t = (dist / speed)

    dc.robot.driveDirect(speed, speed)
    time.sleep(t)
    dc.robot.stop()

    print('This button works')
    print('Traveling at:')
    print('Robot speed:', speed)
    print('Distance to travel(cm):', dist)
    print()

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
