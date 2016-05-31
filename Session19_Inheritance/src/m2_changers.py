"""
Changers change.

Authors: David Mutchler, Mark Hays, Michael Wollowski, Amanda Stouder,
         Chandan Rupakheti, Katie Dion, Claude Anderson, Delvin Defoe,
         Curt Clifton, Matt Boutell, Dave Fisher, their colleagues,
         and Brendan Goldacker.  October 2014.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg
import random
import time

def main():
    """ Not used here, but could be used for informal testing. """
    pass


class Changer(object):
    """
    A Changer has one instance variable:
      -- shape:  Must be an rg._Shape
                   (Circle, Square, Ellipse, Rectangle, Text, etc).
                 The Simulator draws this shape at every frame refresh.
    A Changer has two methods:
      -- change: Can do whatever it wants (including nothing).
                   This method is called by the Simulator just before
                   each frame refresh.
                   NOTE: If this method hangs, the simulator will hang!
      -- better: Takes another Changer and returns whichever Changer
                   is "better" -- this Changer or the given one.
                   The Simulator tries to draw Changers so that the
                   better Changers are on top of the less good Changers.
    """
    def __init__(self, shape):
        """
        Saves the given shape as this Changer's shape.

        Precondition:
          :type shape: rg._Shape
        """
        # --------------------------------------------------------------
        # DONE: With your instructor, implement and test this method.
        # --------------------------------------------------------------
        self.shape = shape

    def change(self):
        """
        Does nothing.  Subclasses may override this method to obtain
        more interesting behaviors.
        """

    def better(self, another_Changer):  # @UnusedVariable
        """
        Returns whichever Changer is "better" -- this Changer or the
        given Changer.  Subclasses must override this method.

        Precondistion:
          :type another_Changer: Changer
        """
        assert False, 'Subclasses must OVERRIDE this method.'


# ----------------------------------------------------------------------
# DONE: With your instructor, implement the following   Dud   class.
# ----------------------------------------------------------------------
class Dud(Changer):
    """
    A Changer whose shape is a black circle at the given point
    with radius 10.  It does nothing (just sits still).
    """

    def __init__(self, point):
        """
        Stores the   shape   as a black circle at the given point
        with radius 10.

        Precondition:
          :type point: rg.Point
        """
        circle = rg.Circle(point, 10)
        circle.fill_color = 'black'
        circle.outline_color = 'black'

        super().__init__(circle)

    def change(self):
        """ Does nothing (a Dud just sits still). """

    def better(self, another_Changer):  # @UnusedVariable
        """
        Returns the given Changer -- Duds are never better than other
        types of Changers (they are "duds", after all!).

        Precondition:
          :type another_Changer: Changer
        """
        return another_Changer


# ----------------------------------------------------------------------
# DONE: With your instructor, implement the following   Mover   class.
# ----------------------------------------------------------------------
class Mover(Changer):
    """
    A Changer with a velocity.  At each call to the  change  method,
    a Mover moves the distance specified by its velocity.
    Movers are better than Duds, but worse than all other Changers.
    """

    def __init__(self, shape, velocity_x=1, velocity_y=1):
        """
        Saves the given shape and velocity.

        Precondition:
          :type shape: rg._Shape
        """
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        super().__init__(shape)

    def change(self):
        """ Moves this Mover per its velocity. """
        self.shape.center.x = self.shape.center.x + self.velocity_x
        self.shape.center.y = self.shape.center.y + self.velocity_y


    def better(self, another_Changer):
        """
        Returns the given Changer unless that Changer is a Dud,
        in which case returns this Mover.
        """
        if another_Changer == Dud:
            return Mover
        return another_Changer


# ----------------------------------------------------------------------
# DONE: Implement and test the classes below.
#       Add additional  Changer  classes if you wish!
#       Test each class as you implement it!
# ----------------------------------------------------------------------
class Randomizer(Changer):
    """
    A Changer that moves randomly: at each call to the  change  method,
    a Randomizer moves to a random point in the simulation's window.
    Randomizers are better than Duds and Movers, worse than all others.
    """
    def change(self):
        self.shape.center.x = random.randrange(600)
        self.shape.center.y = random.randrange(600)

    def better(self, another_Changer):
        if another_Changer == Mover or another_Changer == Dud:
            return Randomizer
        return another_Changer


class Jiggler(Changer):
    """
    A Changer that "jiggles":  At each opportunity to change,
    it moves its shape a small random distance.   The range from which
    the random distances are chosen is set when the Jiggler is constructed.
    So, some Jigglers jiggle violently and others less so.
    """
    def change(self):
        self.shape.center.x = random.randrange(self.shape.center.x - 20, self.shape.center.x + 20)
        self.shape.center.y = random.randrange(self.shape.center.y - 20, self.shape.center.y + 20)

    def better(self, another_Changer):
        if another_Changer == (Randomizer or  Mover or Dud):
            return Jiggler
        return another_Changer


class Follower(Changer):
    """
    A Changer that follows another Changer that it is given when it
    is constructed.  It follows after a delay that it is given.
    """
    def __init__(self, shape, given_changer, seconds):
        self.given_changer = given_changer
        self.seconds = seconds
        super().__init__(shape)

    def change(self):
        self.given_changer.change()

    def better(self, another_Changer):
        if another_Changer == (Randomizer or  Mover or Dud):
            return Jiggler
        return another_Changer


class Grower(Changer):
    """
    A Changer that grows (increases its radius) at a constant rate.
    Its shape must be a circle.
    It stops growing when it gets a radius that reaches a given maximum.
    """
    def __init__(self, shape, maximum):
        self.maximum = maximum
        self.shape = shape

    def change(self):
        if self.shape.radius <= self.maximum:
            self.shape.radius = self.shape.radius + 10

    def better(self, another_Changer):
        if another_Changer == (Jiggler or Randomizer or  Mover or Dud):
            return Grower
        return another_Changer


class MoverGrower(Changer):
    """
    A Changer that combines the effects of a Mover and a Grower.
    """
    def __init__(self, shape, maximum, velocity_x=1, velocity_y=1):
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.maximum = maximum
        super().__init__(shape)

    def change(self):
        self.shape.center.x = self.shape.center.x + self.velocity_x
        self.shape.center.y = self.shape.center.y + self.velocity_y
        if self.shape.radius <= self.maximum:
            self.shape.radius = self.shape.radius + 10



class Exploder:
    """
    A Changer is like a MoverGrower, but when it reaches a certain
    radius, it "explodes":
      -- It changes its rg.Circle to be tiny (so almost invisible)
           and no longer moving.
      -- It constructs two new Exploders, with random initial properties,
           and adds them to the Simulation.
    """
#     def __init__(self, shape, velocity_x=1, velocity_y=1, maximum):
#         self.velocity_x = velocity_x
#         self.velocity_y = velocity_y
#         self.maximum = maximum
#         super().__init__(shape)
#
#     def change(self):
#         if self.radius <= self.maximum:
#             self.shape.center.x = self.shape.center.x + self.velocity_x
#             self.shape.center.y = self.shape.center.y + self.velocity_y
#             self.shape.radius = self.shape.radius + 10
#         if self.radius >= self.maximum:
#             self.shape.radius = .01
#             circle1 = rg.Circle(rg.Point(100, 100), random.randrange(50))
#             velocityx1 = random.randrange(50)
#             velocityy1 = random.randrange(50)
#             max1 = random.randrange(50)
#             circle2 = rg.Circle(rg.Point(300, 300), random.randrange(50))
#             velocityx2 = random.randrange(50)
#             velocityy2 = random.randrange(50)
#             max2 = random.randrange(50)
#             Exploder(circle1, velocityx1, velocityy1, max1)
#             Exploder(circle2, velocityx2, velocityy2, max2)



# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
