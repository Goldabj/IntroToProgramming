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

A typical use of rosegraphics.py might be something like:
   TODO: Give a simple example, showing attach and render.

Authors: David Mutchler, Mark Hays, Michael Wollowswki, Matt Boutell,
         Chandan Rupakheti, Claude Anderson and their colleagues,
         with thanks to John Zelle for inspiration and hints.
         First completed version: September 2014.
"""

import tkinter
import time

ARC_DEFAULTS = {}
BITMAP_DEFAULTS = {}
CIRCLE_DEFAULTS = {'fill_color': None,
                   'outline_color': 'black',
                   'outline_thickness': 1}
ELLIPSE_DEFAULTS = {'fill_color': 'black',
                    'outline_color': 'black',
                    'outline_thickness': 1}
IMAGE_DEFAULTS = {}
LINE_DEFAULTS = {'color': 'black',
                 'thickness': 1}
POINT_DEFAULTS = {'radius_for_drawing': 3,
                  'fill_color': 'red',
                  'outline_color': 'black'}
POLYGON_DEFAULTS = {}
RECTANGLE_DEFAULTS = {'fill_color': None,
                      'outline_color': 'black',
                      'outline_thickness': 1}
SQUARE_DEFAULTS = {}
TEXT_DEFAULTS = {}
WINDOW_DEFAULTS = {}
BUTTON_DEFAULTS = {}
ENTRY_DEFAULTS = {}


# CONSIDER: Maybe add curve (various kinds), path, area, and ??
# See Java's Shape.

# ----------------------------------------------------------------------
# All the windows that are constructed during a run share the single
#    _master_Tk   (a tkinter.Tk object)
# as their common root.  The first construction of a RoseWindow
# sets this  _master_Tk to a Tkinter.Tk object.
# ----------------------------------------------------------------------
_master_Tk = None


# ----------------------------------------------------------------------
# RoseWindow is the top-level object.
# It starts with a single RoseCanvas.
# ----------------------------------------------------------------------
class RoseWindow():
    """
    A RoseWindow is a "window" that pops up when constructed.
    It starts with a RoseCanvas upon which one can draw shapes.
    One can add other widgets (FortuneTeller, ttk.Button, etc) to it.
    """

    def __init__(self, width=400, height=300, title='Rose Graphics',
                 window_color='black', canvas_color=None):
        """
        Constructs a Window with a RoseCanvas on it.

        The optional (keyword) arguments:
          -- height, width, title, window_color, canvas_color.
        are each stored in an instance variable of the same name.

        Additional public instance variables are:
          -- initial_canvas:  A RoseCanvas created automatically.
          -- widgets:   The list of widgets (initial_canvas et al)
                          that are on this RoseWindow.
          -- mouse:     The Mouse bound to this RoseWindow.
          -- keyboard:  The Keyboard bound to this RoseWindow.
          -- toplevel:  The tkinter Toplevel that is the graphical
                          incarnation of this RoseWindow.
        """
        # --------------------------------------------------------------
        # The _master_Tk controls the mainloop for ALL the RoseWindows.
        # If this is the first RoseWindow constructed in this run,
        # then construct the _master_Tk object.
        # --------------------------------------------------------------
        global _master_Tk
        if not _master_Tk:
            _master_Tk = tkinter.Tk()
            _master_Tk.withdraw()
        else:
            time.sleep(0.1)  # Helps the window appear on TOP of Eclipse

        # --------------------------------------------------------------
        # Has a tkinter.Toplevel, and a tkinter.Canvas on the Toplevel.
        # --------------------------------------------------------------
        self.toplevel = tkinter.Toplevel(_master_Tk,
                                         background=window_color)
        self.toplevel.title(title)

        self.initial_canvas = RoseCanvas(self, width, height,
                                         canvas_color)
        self.widgets = [self.initial_canvas]

        # TODO: Do any other tailoring of the toplevel as desired,
        #       e.g. borderwidth and style...

        # --------------------------------------------------------------
        # Catch mouse clicks and key presses.
        # --------------------------------------------------------------
        self.mouse = Mouse()
        self.keyboard = Keyboard()
        self.toplevel.bind('<Button>', self._on_mouse_click)
        self.toplevel.bind('<KeyPress>', self._on_key_press)

        self.update()

    def close_on_mouse_click(self):
        self.get_next_mouse_click()
        self.close()

    def get_next_mouse_click(self):
        self.update()  # flush any prior clicks
        self.mouse.position = None
        while True:
            if self.mouse.position is not None:
                break
            self.update()
            time.sleep(.05)  # allow time for other events to be handled

        click_point = self.mouse.position
        self.mouse.position = None

        return click_point

    def close(self):
        """ Close this window """
        if self.toplevel:
            self.toplevel.destroy()
            self.toplevel = None
        self.update()

    def update(self):
        global _master_Tk
        _master_Tk.update()

    def render(self, seconds_to_pause=None):
        for widget in self.widgets:
            if type(widget) == RoseCanvas:
                widget.render()

        self.update()

        if seconds_to_pause:
            time.sleep(seconds_to_pause)

    def _on_mouse_click(self, event):
        self.mouse._update(event)

    def _on_key_press(self, event):
        self.keyboard._update(event)

#     def add_canvas(self, width=None, height=None, background_color=None):
# TODO: Set defaults based on the main canvas.
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
        self._tkinter_canvas = tkinter.Canvas(window.toplevel,
                                              width=width, height=height,
                                              background=background_color)
        # TODO: Automate gridding better.
        self._tkinter_canvas.grid(padx=5, pady=5)

        # CONSIDER: Parallel lists (ugh).  Is there a better approach?
        self.shape_ids = []

    def render(self, seconds_to_pause=None):
        for shape_id in self.shape_ids:
            self._tkinter_canvas.itemconfigure(shape_id,
                                               state=tkinter.NORMAL)
        return
        self._window.update()

        if seconds_to_pause:
            time.sleep(seconds_to_pause)

    def _make_representation_of(self, shape):
#         command = shape._command_for_drawing
        arguments = shape._coordinates_for_drawing
        options = shape._options_for_drawing
        print(options)

#         shape_id = tkinter.Canvas.command(self._tkinter_canvas,
#                                           *arguments)
        if type(shape) == Point or type(shape) == Circle or type(shape) == Ellipse:
            shape_id = self._tkinter_canvas.create_oval(*arguments)
        elif type(shape) == Square or type(shape) == Rectangle:
            shape_id = self._tkinter_canvas.create_rectangle(*arguments)

        self._tkinter_canvas.itemconfigure(shape_id, options)
        self.shape_ids.append(shape_id)

        return shape_id

    def _move_object_by(self, id_on_this_canvas, dx, dy):
        self._tkinter_canvas.move(id_on_this_canvas, dx, dy)

    def _update_object_options(self, id_on_this_canvas, shape):
        options = self._tkinter_canvas.itemconfigure(id_on_this_canvas)
        # TODO: Throw relevant exception if option is not legal.
        for key in shape._options_for_drawing:
            options[key] = shape._options_for_drawing[key]

        # CONSIDER: Is the next line needed?
        self._tkinter_canvas.itemconfigure(id_on_this_canvas, options)


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
    def __init__(self):
        self._options = type(self).DEFAULTS

        # CONSIDER: parallel lists (ugh).  Can I do better?
        self.canvasses = []
        self.ids_on_canvasses = []

    def attach_to(self, rose_canvas):
        if rose_canvas not in self.canvasses:
            shape_id = rose_canvas._make_representation_of(self)
            self.canvasses.append(rose_canvas)
            self.ids_on_canvasses.append(shape_id)

    def _move_on_canvasses(self, dx, dy):
        for k in range(len(self.canvasses)):
            canvas = self.canvasses[k]
            id_on_canvas = self.ids_on_canvasses[k]
            canvas._move_object_by(id_on_canvas, dx, dy)

    def _set_options_on_canvasses(self):
        for k in range(len(self.canvasses)):
            canvas = self.canvasses[k]
            id_on_canvas = self.ids_on_canvasses[k]
            canvas._update_object_options(id_on_canvas)

    def _get_coordinates_for_drawing(self):
        """ The specific Shape MUST supply this property. """
        # TODO: Raise an appropriate Exception if this is called.

    def _get_options_for_drawing(self):
        """ The specific Shape MUST supply this property. """
        # TODO: Raise an appropriate Exception if this is called.


class Arc(Shape):
    """ Not yet implemented. """
    DEFAULTS = ARC_DEFAULTS


class Bitmap(Shape):
    """ Not yet implemented. """
    DEFAULTS = BITMAP_DEFAULTS


class Circle(Shape):
    DEFAULTS = CIRCLE_DEFAULTS

    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

        self.fill_color = Circle.DEFAULTS['fill_color']
        self.outline_color = Circle.DEFAULTS['outline_color']
        self.outline_thickness = Circle.DEFAULTS['outline_thickness']

        super().__init__()

    def __repr__(self):
        string = 'Circle with center at ({}, {}) and radius {})'
        return string.format(self.center.x, self.center.y,
                             self.radius)

    def _get_bounding_box(self):
        rectangle = Rectangle(Point(self.center.x - self.radius,
                                    self.center.y - self.radius),
                              self.radius * 2,
                              self.radius * 2)
        return rectangle

    doc_string = 'Bounding box for this Shape (i.e., smallest Rectangle that encloses it)'
    bounding_box = property(_get_bounding_box,
                            doc=doc_string)

    def _get_coordinates_for_drawing(self):
        return self._get_bounding_box()._get_coordinates_for_drawing()

    doc_string = 'Coordinates tkinter needs to draw this Shape'
    _coordinates_for_drawing = property(_get_coordinates_for_drawing,
                                        doc=doc_string)

    def _get_options_for_drawing(self):
        options = {'fill': self.fill_color,
                   'outline': self.outline_color,
                   'width': self.outline_thickness}
        return options

    doc_string = 'Some of the options (like fill_color) that tkinter uses to draw this Shape'
    _options_for_drawing = property(_get_options_for_drawing,
                                    doc=doc_string)


class Ellipse(Shape):
    DEFAULTS = ELLIPSE_DEFAULTS

    def __init__(self, upper_left_corner, width, height):
        self.upper_left_corner = upper_left_corner
        self.width = width
        self.height = height

        self.fill_color = Circle.DEFAULTS['fill_color']
        self.outline_color = Circle.DEFAULTS['outline_color']
        self.outline_thickness = Circle.DEFAULTS['outline_thickness']

        super().__init__()

    def __repr__(self):
        string = 'Ellipse whose bounding box has upper-left corner at ({}, {})'
        string = string + ', width {} and height {}'
        return string.format(self.upper_left_corner,
                             self.width,
                             self.height)

    def center(self):
        return Point(self.upper_left_corner + self.width / 2,
                     self.upper_left_corner + self.height / 2)

    def bounding_box(self):
        return Rectangle(self.upper_left_corner,
                         self.width, self.height)

    def _get_coordinates_for_drawing(self):
        return self.get_bounding_box().get_coordinates_for_drawing()

    doc_string = 'Coordinates tkinter needs to draw this Shape'
    _coordinates_for_drawing = property(_get_coordinates_for_drawing,
                                        doc=doc_string)

    def _get_options_for_drawing(self):
        options = {'fill': self.fill_color,
                   'outline': self.outline_color,
                   'width': self.outline_thickness}
        return options

    doc_string = 'Some of the options (like fill_color) that tkinter uses to draw this Shape'
    _options_for_drawing = property(_get_options_for_drawing,
                                    doc=doc_string)

class Image(Shape):
    """ Not yet implemented. """
    DEFAULTS = IMAGE_DEFAULTS


class Line(Shape):
    """ A Line has Points for its start and end.
    Options allow it to have: xxx.
    """
    DEFAULTS = LINE_DEFAULTS

    def __init__(self, start, end):
        """ Sets the Points for the start and end of this Line.
        Also sets default values for the options for this Line.
        """
        self.start = start
        self.end = end

        self.color = Line.DEFAULTS['color']
        self.thicknesss = Line.DEFAULTS['thickness']

        super().__init__()

    def __repr__(self):
        string = 'Line from ({}, {}) to ({}, {}))'
        return string.format(self.start.x, self.start.y,
                             self.end.x, self.end.y)

    def move_by(self, delta_x, delta_y):
        self.start.move_by(delta_x, delta_y)
        self.end.move_by(delta_x, delta_y)
        self._move_representations_by(delta_x, delta_y)

    @property
    def midpoint(self):
        return Point((self.start.x + self.end.x) // 2,
                     (self.start.y + self.end.y) // 2)

    def _get_coordinates_for_drawing(self):
        return [self.start.x,
                self.start.y,
                self.end.x,
                self.end.y]

    doc_string = 'Coordinates tkinter needs to draw this Shape'
    _coordinates_for_drawing = property(_get_coordinates_for_drawing,
                                        doc=doc_string)

    def _get_options_for_drawing(self):
        options = {'fill': self.color,
                   'width': self.thickness}
        return options

    doc_string = 'Some of the options (like fill_color) that tkinter uses to draw this Shape'
    _options_for_drawing = property(_get_options_for_drawing,
                                    doc=doc_string)

class Point(Shape):
    DEFAULTS = POINT_DEFAULTS

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.radius_for_drawing = Point.DEFAULTS['radius_for_drawing']
        self.fill_color = Point.DEFAULTS['fill_color']

        super().__init__()

    def __repr__(self):
        return 'Point at ({}, {})'.format(self.x, self.y)

    def move_by(self, delta_x, delta_y):
        self.x = self.x + delta_x
        self.y = self.y + delta_y
        self._move_on_canvasses(delta_x, delta_y)

    def move_to(self, x, y):
        delta_x = x - self.x
        delta_y = y - self.y
        self.move_by(delta_x, delta_y)

    def _get_bounding_box(self):
        dot = Circle(self, self.radius_for_drawing)
        return dot.bounding_box

    doc_string = 'Bounding box for this Shape (i.e., smallest Rectangle that encloses it)'
    bounding_box = property(_get_bounding_box,
                            doc=doc_string)

    def _get_coordinates_for_drawing(self):
        return self._get_bounding_box()._get_coordinates_for_drawing()

    doc_string = 'Coordinates tkinter needs to draw this Shape'
    _coordinates_for_drawing = property(_get_coordinates_for_drawing,
                                        doc=doc_string)

    def _get_options_for_drawing(self):
        options = {'fill': self.fill_color}
        return options

    doc_string = 'Some of the options (like fill_color) that tkinter uses to draw this Shape'
    _options_for_drawing = property(_get_options_for_drawing,
                                    doc=doc_string)


class Polygon(Shape):
    """ Not yet implemented. """
    DEFAULTS = POLYGON_DEFAULTS


class Rectangle(Shape):
    DEFAULTS = RECTANGLE_DEFAULTS

    def __init__(self, upper_left_corner, width, height):
        self.upper_left_corner = upper_left_corner
        self.width = width
        self.height = height

        self.fill_color = Rectangle.DEFAULTS['fill_color']
        self.outline_color = Rectangle.DEFAULTS['outline_color']
        self.outline_thickness = Rectangle.DEFAULTS['outline_thickness']

        super().__init__()

    def __repr__(self):
        string = 'Rectangle with upper-left corner at ({}, {})'
        string = string + ', width {} and height {}'
        return string.format(self.upper_left_corner,
                             self.width,
                             self.height)

    def move_by(self, delta_x, delta_y):
        self.upper_left_corner.move_by(delta_x, delta_y)
        self._move_on_canvasses(delta_x, delta_y)

    def _get_lower_right_corner(self):
        return Point(self.upper_left_corner.x + self.width,
                     self.upper_left_corner.y + self.height)

    lower_right_corner = property(_get_lower_right_corner,
                                  doc='Point that is the lower-right corner')

    def _get_lower_left_corner(self):
        return Point(self.upper_left_corner.x,
                     self.upper_left_corner.y + self.height)

    lower_left_corner = property(_get_lower_left_corner,
                                 doc='Point that is the lower-left corner')

    def _get_upper_right_corner(self):
        return Point(self.upper_left_corner.x + self.width,
                     self.upper_left_corner.y)

    upper_right_corner = property(_get_upper_right_corner,
                                  doc='Point that is the upper-right corner')

    def _get_coordinates_for_drawing(self):
        return [self.upper_left_corner.x,
                self.upper_left_corner.y,
                self.lower_right_corner.x,
                self.lower_right_corner.y]

    doc_string = 'Coordinates tkinter needs to draw this Shape'
    _coordinates_for_drawing = property(_get_coordinates_for_drawing,
                                        doc=doc_string)

    def _get_options_for_drawing(self):
        options = {'fill': self.fill_color,
                   'outline': self.outline_color,
                   'width': self.outline_thickness}
        return options

    doc_string = 'Some of the options (like fill_color) that tkinter uses to draw this Shape'
    _options_for_drawing = property(_get_options_for_drawing,
                                    doc=doc_string)

    @property
    def center(self):
        diagonal = Line(self.one_corner, self.opposite_corner)
        return diagonal.find_midpoint()

    @property
    def command_for_drawing(self):
        return


class Square(Shape):
    """ Not yet implemented. """
    DEFAULTS = SQUARE_DEFAULTS

#     def __init__(self, center, width_height):
#         self.center = center
#         self.width_height = width_height
#         super().__init__()
#
#     def __repr__(self):
#         string = 'Square with center at ({}, {}) and width/height {}'
#         return string.format(self.center, self.width_height)


class Text(Shape):
    """ Not yet implemented. """
    DEFAULTS = TEXT_DEFAULTS


class Window(Shape):
    """ Not yet implemented. """
    DEFAULTS = WINDOW_DEFAULTS


class Button(Shape):
    """ Not yet implemented. """
    DEFAULTS = BUTTON_DEFAULTS


class Entry(Shape):
    """ Not yet implemented. """
    DEFAULTS = ENTRY_DEFAULTS


def main():
    """ Calls the   TEST   functions in this module. """
    w = RoseWindow()

    p1 = Point(100, 50)
    p2 = Point(30, 150)

    rect = Rectangle(p1, 100, 40)


    print('attaching rectangle')
    rect.attach_to(w.initial_canvas)
    p1.attach_to(w.initial_canvas)

    print('rendering p1')
    w.render(3)

    print('moving rect')
    rect.move_by(100, 0)
    p1.move_by(0, 50)
    time.sleep(3)

    print('rendering moved rect')
    w.render()

#     line = Line(p1, p2)
#     circle = Circle(p1, 25)
#     circle.fill_color = 'red'
#     circle.outline_color = 'blue'
#     circle.outline_thickness = 8
#
#     rectangle = Rectangle(p1, p2)
#     rectangle.attach_to(w.initial_canvas)
#     rectangle.outline_color = 'blue'
#     rectangle.outline_thickness = 5
#     rectangle.fill_color = 'green'
#     line.attach_to(w.initial_canvas)
#     p1.attach_to(w.initial_canvas)
#     p2.attach_to(w.initial_canvas)
#     circle.attach_to(w.initial_canvas)
#     w.render(3)
#
# #     line.thickness = 6
# #     circle.fill_color = 'blue'
# #     w.render()
#
#     print(line.find_midpoint().x)

    w.close_on_mouse_click()
#     w = RoseWindow()
#     w.close_on_mouse_click()

#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
