#!/usr/bin/env python
""" """

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2009 Hendrix Demers"
__license__ = ""

# Subversion informations for the file.
__svnRevision__ = "$Revision: 2293 $"
__svnDate__ = "$Date: 2011-03-21 14:39:25 -0400 (Mon, 21 Mar 2011) $"
__svnId__ = "$Id: diffraction_vector.py 2293 2011-03-21 18:39:25Z hdemers $"

# Standard library modules.

# Third party modules.
import numpy as np

# Local modules.

# Globals and constants variables.
X = 0
Y = 1

class DiffractionVector(object):
    def __init__(self, id, spot):
        self._id = id
        self.setSpot(spot)

    def setSpot(self, spot):
        self._spot = spot
        x, y = spot.getPosition()
        #self._vector = visual.vector(x, y, 0.0)
        self._vector = np.array((x, y, 0.0))

    def getPosition(self):
        return self._spot.getPosition()

    def getLength(self):
        return np.linalg.norm(self._vector)

    def getVector(self):
        return self._vector

    def __eq__(self, other):
        if self.getLength() == other.getLength():
            return True
        else:
            return False

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if self.getLength() < other.getLength():
            return True
        else:
            return False

if __name__ == '__main__':    #pragma: no cover
    import pyHendrixDemersTools.Runner as Runner
    Runner.Runner().run(runFunction=None)
