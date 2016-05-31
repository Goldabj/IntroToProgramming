"""
rosegraphics.py - a simple Graphics library for Python.
Its key feature is:
  -- USING this library provides a simple introduction to USING objects.
  
Other key features include:
  -- It is a simple graphics library that allows one to:
        -- Construct objects like circles, lines, etc. on windows
        -- Apply methods like move_by, spin
        -- Access fields like a point's x and y coordinates.
  -- It is built on top of tkinter
        (the standard graphics library that comes with Python)
  -- Unlike tkinter, it is NOT event-driven
        (and hence can be used before students see that paradigm).
  -- It was inspired by zellegraphics, but is a complete
        re-implementation that is designed to be more bullet-proof
        for beginners than zellegraphics is.
  -- While it can serve as an example for defining classes,
        it is NOT intended to do so for beginners.
        It is excellent for helping students learn to USE objects;
        it is NOT perfect for helping students learn to WRITE CLASSES.
        
Authors: David Mutchler, Mark Hays, Chandan Rupakheti and their
         colleagues, with thanks to John Zelle for inspiration and hints.
         First completed version: September 2014.
"""

import tkinter
import time

# WARNING: This library is NOT finished yet!  But it will do for today.

#------------------------------------------------------------------------
# All the windows that are constructed during a run share this
# tkinter.Tk object as their common root.  The first construction
# of a Window sets this  _root  to a Tkinter.Tk object.
#------------------------------------------------------------------------

_master_Tk = None

class RoseWindow():
    """
        A RoseWindow is a "window" that pops up when constructed.
        It has a RoseCanvas upon which one can draw shapes et al.
    """
    def __init__(self, width=400, height=300,
                 title='Rose Graphics',
                 window_color='black', canvas_color=None):
        """
            Constructs a Window with the (optionally) given:
              -- height             [default is 300]
              -- width              [default is 200]
              -- title              [default is 'Rose Graphics']
              -- window_color       [default is 'black']
              -- canvas_color       [default is None, which yields the
                                     tkinter default of a light gray]
        """
        global _master_Tk
        if not _master_Tk:  # If this is the first Window, make the shared root
            _master_Tk = tkinter.Tk()
            _master_Tk.withdraw()

        self._toplevel = tkinter.Toplevel(_master_Tk, background=window_color)
        self._toplevel.title(title)

        self.main_canvas = RoseCanvas(self, width, height, canvas_color)
        self.widgets = [self.main_canvas]

        #----------------------------------------------------------------
        # Catch mouse clicks and key presses.
        #----------------------------------------------------------------
        self.mouse = Mouse()
        self.keyboard = Keyboard()
        self._toplevel.bind('<Button>', self._on_mouse_click)
        self._toplevel.bind('<KeyPress>', self._on_key_press)

        self.render()

    def close_on_mouse_click(self):
        self.get_next_mouse_click()
        self.close()

    def get_next_mouse_click(self):
        self.update()  # flush any prior clicks
        self.mouse.position = None
        while True:
            if self.mouse.position != None:
                break
            self.update()
            time.sleep(.1)  # give up thread

        click_point = self.mouse.position
        self.mouse.position = None

        return click_point

    def close(self):
        """ Close this window """
        if self._toplevel:
            self._toplevel.destroy()
            self._toplevel = None
        self.update()

    def update(self):
        global _master_Tk
        _master_Tk.update()

    def render(self, seconds_to_pause=None):
        self.update()
        for widget in self.widgets:
            if type(widget) == RoseCanvas:
                widget.render()

        if seconds_to_pause:
            time.sleep(seconds_to_pause)

    def _on_mouse_click(self, event):
        self.mouse._update(event)

    def _on_key_press(self, event):
        self.keyboard._update(event)

#     def add_canvas(self, width=None, height=None, background_color=None):
#         # TODO: Set defaults based on the main canvas.
#         new_canvas = RoseCanvas(self, background_color='white')
#         self.widgets.append(new_canvas)
#
#         _root.update()

class RoseWidget():
    """
       A Widget is a thing that one can put on a Window,
       e.g. a Canvas, FortuneTeller, etc.
    """

    def __init__(self, window):
        self._window = window


class RoseCanvas(RoseWidget):
    """
       A RoseCanvas is a RoseWidget (i.e., a thing on a RoseWindow)
       upon which one can draw shapes and other Drawable things.
    """

    def __init__(self, window, width=200, height=300, background_color=None):
        super().__init__(window)
        self._tkinter_canvas = tkinter.Canvas(window._toplevel,
                                      width=width, height=height,
                                      background=background_color)
        # TODO: Automate gridding better.
        self._tkinter_canvas.grid(padx=5, pady=5)

        self.shapes_on_canvas = {}

    def render(self, seconds_to_pause=None):
        for shape in self.shapes_on_canvas:
            self._tkinter_canvas.delete(self.shapes_on_canvas[shape])
            self._make_representation_for(shape)

        self._window.update()

        if seconds_to_pause:
            time.sleep(seconds_to_pause)

    def _make_representation_for(self, shape):
        if type(shape) == Point:
            WIDTH = 5
            shape_id = self._tkinter_canvas.create_oval(shape.x - WIDTH,
                                                  shape.y - WIDTH,
                                                  shape.x + WIDTH,
                                                  shape.y + WIDTH)
        elif type(shape) == Line:
            shape_id = self._tkinter_canvas.create_line(shape.start.x,
                                                  shape.start.y,
                                                  shape.end.x,
                                                  shape.end.y)
        elif type(shape) == Circle:
            shape_id = self._tkinter_canvas.create_oval(shape.center.x - shape.radius,
                                                        shape.center.y - shape.radius,
                                                        shape.center.x + shape.radius,
                                                        shape.center.y + shape.radius)
        elif type(shape) == Rectangle:
            shape_id = self._tkinter_canvas.create_rectangle(shape.one_corner.x,
                                                             shape.one_corner.y,
                                                             shape.opposite_corner.x,
                                                             shape.opposite_corner.y)

        self._configure_representation_for(shape, shape_id)
        self.shapes_on_canvas[shape] = shape_id

    def _configure_representation_for(self, shape, shape_id):
        options = {'fill': shape.fill_color}
        if type(shape) == Circle or type(shape) == Point or type(Shape) == Rectangle:
            options['outline'] = shape.outline_color
        if type(shape) == Line:
            options['width'] = shape.thickness
        self._tkinter_canvas.itemconfigure(shape_id, options)

class Mouse(object):
    def __init__(self):
        self.position = None

    def _update(self, event):
        self.position = Point(event.x, event.y)

class Keyboard(object):
    def __init__(self):
        self.key_pressed = None

    def _update(self, event):
        pass


class Shape(object):
    def __init__(self, fill_color=None, outline_color=None):
        self.fill_color = fill_color
        self.outline_color = outline_color

    def attach_to(self, rose_canvas):
        rose_canvas._make_representation_for(self)

class Point(Shape):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__()

    def __repr__(self):
        return 'Point at ({}, {})'.format(self.x, self.y)

class Line(Shape):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        super().__init__()
        self.thickness = 1

    def __repr__(self):
        string = 'Line from ({}, {}) to ({}, {}))'
        return string.format(self.start.x, self.start.y,
                             self.end.x, self.end.y)

    def midpoint(self):
        return Point((self.start.x + self.end.x) // 2,
                     (self.start.y + self.end.y) // 2)

class Circle(Shape):
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
        super().__init__()

    def __repr__(self):
        string = 'Circle with center at ({}, {}) and radius {})'
        return string.format(self.center.x, self.center.y,
                             self.radius)

class Rectangle(Shape):
    def __init__(self, one_corner, opposite_corner):
        self.one_corner = one_corner
        self.opposite_corner = opposite_corner
        super().__init__()

    def __repr__(self):
        string = 'Rectangle with opposite corners at ({}, {}) and ({}, {}))'
        return string.format(self.one_corner.x, self.one_corner.y,
                             self.opposite_corner.x, self.opposite_corner.y)

def main():
    """ Calls the   TEST   functions in this module. """
    w = RoseWindow()
    p1 = Point(100, 50)
    p2 = Point(30, 150)

    line = Line(p1, p2)
    circle = Circle(p1, 25)
    circle.fill_color = 'red'

    rectangle = Rectangle(p1, p2)
    rectangle.attach_to(w.main_canvas)
    rectangle.outline_color = 'blue'
    rectangle.fill_color = 'green'
    line.attach_to(w.main_canvas)
    p1.attach_to(w.main_canvas)
    circle.attach_to(w.main_canvas)
    w.render()
    time.sleep(3)

    line.thickness = 6
    circle.fill_color = 'blue'
    w.render()

    print(line.midpoint().x)

    w.close_on_mouse_click()


#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
