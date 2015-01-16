#!/usr/bin/env python
""" """

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2011 Hendrix Demers"
__license__ = ""

# Subversion informations for the file.
__svnRevision__ = "$Revision$"
__svnDate__ = "$Date$"
__svnId__ = "$Id$"

# Standard library modules.

# Third party modules.

# Local modules.

# Project modules
from Range.KanayaOkayamaModels import range_nm as rangeKO_nm

# Globals and constants variables.

def computeRange():
    atomicNumbers = [6, 79, 13, 26]
    energies_keV = [1.0, 10.0, 30.0]

    line = "%4s\t" % ('Z')
    for energy_keV in energies_keV:
        line += "%6.1fkeV\t" % (energy_keV)
    print(line)

    for atomicNumber in atomicNumbers:
        line = "%4i\t" % (atomicNumber)
        for energy_keV in energies_keV:
            range_nm = rangeKO_nm(atomicNumber, energy_keV*1.0e3)
            line += "%9.1f\t" % (range_nm)
        print(line)

if __name__ == '__main__':  #pragma: no cover
    import pyHendrixDemersTools.Runner as Runner
    Runner.Runner().run(runFunction=computeRange)
