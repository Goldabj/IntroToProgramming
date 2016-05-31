"""
Try out Tkinter and ttk!
"""

import tkinter
from tkinter import ttk
import random


def main():
    # Make a window.
    # Put a Frame on it.
    # Put a Button on the frame.
    # Make your Button do something simple.
    # Add a Label and an Entry.
    # Make your Button do something with the Label and Entry.
    pass

    root = tkinter.Tk()

    main_frame = ttk.Frame(root, padding=(50), relief='raised')
    main_frame.grid()

    label = ttk.Label(main_frame, text='hello')
    label.grid()

    button = ttk.Button(main_frame, text='hello')
    button.grid()
    button['command'] = lambda: change_label(root, label, button)

    entry = ttk.Entry(main_frame, width=8)
    entry.grid()

    button2 = ttk.Button(main_frame, text='print number **10')
    button2.grid()
    button2['command'] = lambda: number_10th(entry, main_frame)

    root.mainloop()

def change_label(root, label, change_label_button):
    new_label = ''
    for k in range(8):
        new_label = new_label + chr(ord('A') + random.randrange(26))
    label['text'] = new_label

def number_10th(entry, frame):
    number = int(entry.get())
    new_number = number ** 10
    new_label = ttk.Label(frame, text='')
    new_label['text'] = str(new_number)
    new_label.grid()

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
