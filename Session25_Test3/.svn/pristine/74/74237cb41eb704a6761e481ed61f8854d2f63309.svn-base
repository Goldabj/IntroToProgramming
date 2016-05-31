"""
Test 3, part of problem 3.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Brendan Goldacker.  November 2014.
"""  # DONE: PUT YOUR NAME IN THE ABOVE LINE.

# ----------------------------------------------------------------------
# DONE: Implement the   Balloon   class below
#       (i.e., replace each "pass" by relevant code).
#       Test your methods by using the  problem3_test_Balloon  module.
#
# IMPORTANT:
#  1. Read the specification of the ENTIRE   Balloon   class BEFORE
#       writing any code.
#  2. Test each method AS YOU DEFINE IT (one by one).
# ----------------------------------------------------------------------


def main():
    """ Not used here, but could be used for informal testing. """
    # Put your tests in the   problem3_test_Balloon  module, NOT here.
    pass


# ----------------------------------------------------------------------
# USE this Person class in implementing the Elevator class below.
# ----------------------------------------------------------------------
class Person(object):
    """
    Simulates a person with an age (in years) and weight (in pounds).
    """

    def __init__(self, age, weight, is_happy=True):
        """
        Stores the Person's age and weight.
        The Person starts out happy by default.
        """
        self.age = age
        self.weight = weight
        self.is_happy = is_happy

    def __repr__(self):
        """ Returns a string representation of this Person. """
        return 'Person({}, {}, {})'.format(self.age,
                                           self.weight,
                                           self.is_happy)

    def clone(self):
        """ Returns a clone (copy) of this Person. """
        return Person(self.age, self.weight, self.is_happy)


class Balloon(object):
    """
    A Balloon has:
      -- a capacity (how much air can be blown into it before it pops)
      -- a current volume (initially 0)
      -- an owner (a Person)
    and any other instance variables you find the need for.
    """

    def __init__(self, capacity, owner):
        """
        A Balloon starts out uninflated (i.e., its current volume is 0)
        and unpunctured, with the given capacity in cubic feet.
        The Balloon has the given owner, where the owner is a Person
        (as defined in the Person class above).

        Preconditions:
          :type capacity: (int, float)
          :type owner: Person
        and the capacity is positive.
        """
        self.capacity = capacity
        self.volume = 0
        self.owner = owner

    def __repr__(self):
        """returns a format string of a created balloon"""
        format_string = 'Ballon with capacity {}, volume {}, and owner {}'
        return format_string.format(self.capacity, self.volume, self.owner)

    def blow_air_into(self, number_of_breaths):
        """
        A person blows into this balloon (thus inflating it)
        the given number of breaths.  If the age of this Balloon's
        owner is less than 12, each breath adds 0.03 cubic feet
        to this balloon's current volume; otherwise, each breath
        adds 0.5 cubic feet to this balloon's current volumne.

        If this balloon's current volume exceeds its capacity,
        the balloon bursts (and its current volume changes to 0)
        and its owner becomes sad (that is, the owner's  is_happy
        instance variable becomes False).

        If a person blows air into a burst balloon,
        nothing happens -- the current volume stays at 0.

        Preconditions:
          :type number_of_breaths: int
        and the number_of_breaths is positive.
        """
        if self.capacity > 0:
            if self.owner.age < 12:
                self.volume = self.volume + (.03 * number_of_breaths)
            else:
                self.volume = self.volume + (.5 * number_of_breaths)
            if self.volume > self.capacity:
                self.volume = 0
                self.capacity = 0
                self.owner.is_happy = False

    def puncture(self):
        """
        Punctures the balloon (putting a hole into it).
        A punctured balloon has current volume 0 and cannot be
        re-inflated.  Also, its owner becomes sad (that is, the owner's
           is_happy  instance variable becomes False).
        """
        self.volume = 0
        self.capacity = 0
        self.owner.is_happy = False

    def let_air_out(self, seconds):
        """
        A person lets air out of this balloon (thus deflating it)
        for the given number of seconds.  Each second removes
        0.08 cubic feet from the balloon's current volume
        (but the balloon never has negative volume).

        Preconditions:
          :type seconds: int
        and the seconds is positive.
        """
        for k in range(seconds):
            self.volume = self.volume - .08
            if self.volume <= 0:
                self.volume = 0
                break

    def owners_age(self):
        """
        Returns the age of the owner of this balloon.
        """
        return self.owner.age

    def fuller_balloon(self, other_balloon):
        """
        Returns this Balloon or the other Balloon, whichever has
        greater current volume.  If tied, return the Balloon whose
        capacity is larger.  If still tied, returns this Ballooon.

        Precondition:
          :type other_balloon: Balloon
        """
        if self.volume > other_balloon.volume:
            return self
        if self.volume < other_balloon.volume:
            return other_balloon
        else:
            return self

    def new_balloon(self):
        """
        Returns a new Balloon whose capacity is the same as the capacity
        of this Balloon and whose owner is a clone of the owner
        of this Balloon.
        """
        new_balloon = self
        return new_balloon

    def unpunctured_balloons(self, balloons):
        """
        Given a list (or tuple) of balloons, returns a list of all the
        unpunctured balloons in the list, along with this balloon
        if it is unpunctured.

        Preconditions:
          :type balloons: (list, tuple)
        where the list (or tuple) contains Balloon objects.
        """
        for k in range(len(balloons)):
            i = 0
            if balloons[i].capacity == 0:
                balloons.remove(balloons[i])
                i = i - 1
            i = i + 1
        if self.capacity != 0:
            balloos = balloons + self
        return balloons

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
