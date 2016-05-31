"""
Tests the various   Ball  classes
that are defined in the imported   m2_changers   module.

Authors: David Mutchler, Mark Hays, Michael Wollowski, Amanda Stouder,
         Chandan Rupakheti, Katie Dion, Claude Anderson, Delvin Defoe,
         Curt Clifton, Matt Boutell, Dave Fisher, their colleagues,
         and PUT YOUR NAME HERE.  October 2014.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE

import simulator as sim
import m2_changers as changers
import rosegraphics as rg


# ----------------------------------------------------------------------
# TODO: Modify this module as needed to test your   Changer   classes
#       as you implement them.  We have supplied some tests for you.
# ----------------------------------------------------------------------
def main():
    """
    Calls the   TEST   functions in this module to get
    lists of Changers that are good for testing the Changer classes.
    Constructs a Simulator, sending the Changers to the Simulator.
    As such, this provides a VISUAL test of the Changer classes.
    """
    # If you add your own classes, add to the following list.
    testers = [test_Dud, test_Mover, test_Randomizer, test_Jiggler,
               test_Follower, test_Grower, test_MoverGrower,
               test_Exploder]

    changers_to_test = []
    for tester in testers:
        changers = tester()
        if changers:
            changers_to_test = changers_to_test + changers

    sim.Simulator(changers_to_test)


def test_Dud():
    """ Returns a list of   Dud   instances good for testing. """
    dud1 = changers.Dud(rg.Point(100, 100))
    dud2 = changers.Dud(rg.Point(150, 80))
    dud3 = changers.Dud(rg.Point(200, 240))

    return [dud1, dud2, dud3]


def test_Mover():
    """ Returns a list of   Mover   instances good for testing. """
    # DONE: Implement and test this method.
    circle = rg.Circle(rg.Point(100, 100), 50)
    circle.fill_color = 'green'
    rectangle = rg.Rectangle(rg.Point(125, 125), 75, 100)
    rectangle.fill_color = 'yellow'
    mover1 = changers.Mover(circle, 20, 20)
    mover2 = changers.Mover(rectangle, 30, 50)

    return [mover1, mover2]


def test_Randomizer():
    """ Returns a list of   Randomizer   instances good for testing. """
    # DONE: Implement and test this method.
    circle = rg.Circle(rg.Point(100, 100), 50)
    circle.fill_color = 'blue'
    rectangle = rg.Rectangle(rg.Point(125, 125), 75, 100)
    rectangle.fill_color = 'orange'
    random1 = changers.Randomizer(circle,)
    random2 = changers.Randomizer(rectangle)

    return [random1, random2]


def test_Jiggler():
    """ Returns a list of   Jiggler   instances good for testing. """
    # DONE: Implement and test this method.
    circle = rg.Circle(rg.Point(100, 320), 25)
    circle.fill_color = 'purple'
    rectangle = rg.Rectangle(rg.Point(500, 600), 120, 200)
    rectangle.fill_color = 'red'
    jiggler1 = changers.Jiggler(circle)
    jiggler2 = changers.Jiggler(rectangle)

    return [jiggler1, jiggler2]


def test_Follower():
    """ Returns a list of   Follower   instances good for testing. """
    # DONE: Implement and test this method.
    circle = rg.Circle(rg.Point(300, 320), 25)
    circle.fill_color = 'pink'
    rectangle = rg.Rectangle(rg.Point(500, 400), 100, 80)
    rectangle.fill_color = 'brown'
    follower1 = changers.Jiggler(circle)
    follower2 = changers.Mover(rectangle, 40, 40)
    test1 = changers.Follower(circle, follower1, 2)
    test2 = changers.Follower(rectangle, follower2, 4)

    return [test1, test2]

def test_Grower():
    """ Returns a list of   Grower   instances good for testing. """
    # DONE: Implement and test this method.
    circle1 = rg.Circle(rg.Point(600, 320), 25)
    circle1.fill_color = 'black'
    circle2 = rg.Circle(rg.Point(200, 320), 25)
    circle2.fill_color = 'green'
    grower1 = changers.Grower(circle1, 60)
    grower2 = changers.Grower(circle2, 90)

    return [grower1, grower2]

def test_MoverGrower():
    """ Returns a list of   MoverGrower   instances good for testing. """
    # DONE: Implement and test this method.
    circle1 = rg.Circle(rg.Point(100, 120), 25)
    circle1.fill_color = 'black'
    circle2 = rg.Circle(rg.Point(30, 20), 25)
    circle2.fill_color = 'green'
    moverg1 = changers.MoverGrower(circle1, 80, 20, 20)
    moverg2 = changers.MoverGrower(circle2, 40, 10, 30)

    return [moverg1, moverg2]


def test_Exploder():
    """ Returns a list of   Exploder   instances good for testing. """
    # DONE: Implement and test this method.
    circle1 = rg.Circle(rg.Point(300, 220), 25)
    circle1.fill_color = 'black'
    circle2 = rg.Circle(rg.Point(330, 220), 25)
    circle2.fill_color = 'green'
    explode1 = changers.MoverGrower(circle1, 20, 20, 80)
    explode2 = changers.MoverGrower(circle2, 10, 30, 40)

    return [explode1, explode2]





# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
