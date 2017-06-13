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
__svnId__ = "$Id: Cnse670Exam2.py 2293 2011-03-21 18:39:25Z hdemers $"

# Standard library modules.

# Third party modules.

# Local modules.

# Globals and constants variables.

def getLineNumber():
    lineNumbers = range(1,6+1)
    #lineNumbers.extend(range(8,14+1))
    #lineNumbers.extend(range(16,22+1))
    #lineNumbers.extend(range(24,27+1))

    return lineNumbers

def _getFamilies():
    hklFamilies = {}

    hklFamilies[1] = [(1, 0, 0)]
    hklFamilies[2] = [(1, 1, 0)]
    hklFamilies[3] = [(1, 1, 1)]
    hklFamilies[4] = [(2, 0, 0)]
    hklFamilies[5] = [(2, 1, 0)]
    hklFamilies[6] = [(2, 1, 1)]

    return hklFamilies

def getFamily(lineNumber):
    hklFamilies = _getFamilies()

    return hklFamilies[lineNumber]

def run():
    lineNumbers = getLineNumber()
    print(lineNumbers)

if __name__ == '__main__':    #pragma: no cover
    import pyHendrixDemersTools.Runner as Runner
    Runner.Runner().run(runFunction=run)
