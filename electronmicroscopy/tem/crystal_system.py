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
__svnId__ = "$Id: crystal_system.py 2293 2011-03-21 18:39:25Z hdemers $"

# Standard library modules.

# Third party modules.

# Local modules.

# Globals and constants variables.
CUBIC = "Cubic"
TETRAGONAL = "Tetragonal"
ORTHORHOMIC = "Orthorhomic"
HEXAGONAL = "Hexagonal"
RHOMBOHEDRAL = "Rhombohedral"
MONOCLINIC = "Monoclinic"
TRICLINIC = "Triclinic"

class CrystalSystem(object):
    def __init__(self):
        self._a = None
        self._b = None
        self._c = None
        self._alpha = None
        self._beta = None
        self._gamma = None

        self._type = None

    def getA(self):
        return self._a

    def getB(self):
        return self._b

    def getC(self):
        return self._c

    def getAlpha(self):
        return self._alpha

    def getBeta(self):
        return self._beta

    def getGamma(self):
        return self._gamma

    def getType(self):
        return self._type

if __name__ == '__main__':    #pragma: no cover
    import pyHendrixDemersTools.Runner as Runner
    Runner.Runner().run(runFunction=None)
