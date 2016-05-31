"""
The  **** PRACTICE **** Python Capstone Project.

CSSE 120 - Introduction to Software Development.
Team members: Brendan, Scott, Alan (all of them).

The primary author of this module is: Brendan Goldacker.
"""
# DONE: Put the names of ALL team members in the above where indicated.
#       Put YOUR NAME in the above where indicated.

import m0
import m2
import m3
import m4

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
# correctly function buttons:
#   -- Connect using Simulator
#   -- Connect using Port
#   -- Disconnect
# plus an:
#   -- Entry box
# in which the user enters the port to use for connecting to a robot.
#
# Use the following ITERATIVE ENHANCEMENT PLAN, where each stage
# augments the preceding stages:
#
#   Stage 1: Frame appears with the three buttons and Entry box on it.
#
#   Stage 2: Connect_using_Simulator button prints a message, as a stub.
#              -- A STUB is placeholder code that lets you do some
#                 testing even before you have finished the real code.
#
#   Stage 3: Connect_using_Simulator button works correctly.
#              That is, pressing it connects to (i.e. constructs)
#              a robot in the simulator (which must already be open).
#
#   Stage 4: Connect_using_Port button prints whatever the user most
#               recently entered into the Entry box, as a stub.
#
#   Stage 5: Connect_using_Port button works correctly.
#              That is, pressing it connects to (i.e. constructs)
#              a robot using the port specified in the Entry box.
#              (There must already be the usual Bluetooth connection.)
#
#   Stage 6: The Disconnect button works correctly,
#              no matter which Connect button was used.
#
# Do ALL your work in THIS file.  Do not touch m0!
# You will INTEGRATE work in the NEXT session, using m0 to do so.
# ----------------------------------------------------------------------


class DataContainer1():
    """ A container for the data shared across the application. """

    def __init__(self):
        """ Initializes instance variables (fields). """
        # Add     self.FOO = BLAH     here as needed.
        self.robot = None


def main():
    """
    Tests functions in this module.
    Intended to be used internally by the primary author of this module.
    """
    print('-------------------------------')
    print('Testing functions in module m1:')
    print('-------------------------------')
    root = tkinter.Tk()
    data = DataContainer1()

    frame1 = my_frame(root, data)
    frame1.grid()

    frame2 = m2.my_frame(root, data)
    frame2.grid()

    frame3 = m3.my_frame(root, data)
    frame3.grid()

    root.mainloop()


def my_frame(root, data):
    """
    Constructs and returns a Frame (on the given root window)
    that contains this module's widgets.
    Also sets up callbacks for this module's widgets.

    Preconditions:
      :type root: tkinter.Tk
      :type data: DataContainer1
    """
    frame = ttk.Frame(root, padding=20, relief='raised')

    entry = ttk.Entry(frame, width=8)
    entry.grid()

    button1 = ttk.Button(frame, text='Connect to simulator')
    button1.grid()
    button1['command'] = lambda: connect_using_simulator(data)

    button2 = ttk.Button(frame, text='connect using port')
    button2.grid()
    button2['command'] = lambda: connect_using_port(entry, data)

    button3 = ttk.Button(frame, text='Disconnect')
    button3.grid()
    button3['command'] = lambda: disconnect(data)

    return frame

def connect_using_simulator(data):
    """connects to the to the irobot simulator. must pass a data object"""
    port = 'sim'
    data.robot = new_create.Create(port)

def connect_using_port(entry, data):
    """Connects to the robot by the given prot number. Must Pass a data object"""
    port = entry.get()
    data.robot = new_create.Create(port, data)

def disconnect(data):
    """Disconnects from the robot"""
    data.robot.shutdown()
    print('robot is disconnected')

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
