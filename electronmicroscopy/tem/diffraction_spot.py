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
__svnId__ = "$Id: diffraction_spot.py 2293 2011-03-21 18:39:25Z hdemers $"

# Standard library modules.
import math

# Third party modules.

# Local modules.

# Globals and constants variables.
X = 0
Y = 1

class DiffractionSpot(object):
    def __init__(self, imagePosition=None, originPosition=None):
        self.setImagePosition(imagePosition)
        self.setOriginPosition(originPosition)

        self._position = None

    def setImagePosition(self, imagePosition):
        self._imagePosition = imagePosition

    def getImagePosition(self):
        return self._imagePosition

    def setOriginPosition(self, originPosition):
        self._originPosition = originPosition

    def getOriginPosition(self):
        return self._originPosition

    def getPosition(self):
        if self._position == None:
            self._computePosition()

        return self._position

    def _computePosition(self):
        x = self._imagePosition[X] - self._originPosition[X]
        y = self._imagePosition[Y] - self._originPosition[Y]

        self._position = (x, y)

    def getLength(self):
        x, y = self.getPosition()

        lengthSquared = x**2 + y**2
        length = math.sqrt(lengthSquared)

        return length

if __name__ == '__main__':    #pragma: no cover
    import pyHendrixDemersTools.Runner as Runner
    Runner.Runner().run(runFunction=None)
