#!/usr/bin/env python
""" """

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2007 Hendrix Demers"
__license__ = ""

# Subversion informations for the file.
__svnRevision__ = "$Revision: 2293 $"
__svnDate__ = "$Date: 2011-03-21 14:39:25 -0400 (Mon, 21 Mar 2011) $"
__svnId__ = "$Id: ElectronProperties.py 2293 2011-03-21 18:39:25Z hdemers $"

# Standard library modules.
import math

# Third party modules.

# Local modules.

# Globals and constants variables.
REST_MASS_kg = 9.1091e-31
CHARGE_C = -1.602e-19
KINETIC_ENERGY_eV = 1.0
KINETIC_ENERGY_J = 1.602e-19
VELOCITY_LIGHT_m_s = 2.9979e8
REST_ENERGY_eV = 511e3
PLANCKS_CONSTANT_J_s = 6.6256e-34
SPIN_J_s = PLANCKS_CONSTANT_J_s/(4.0*math.pi)

class ElectronProperties(object):
    def mass(self):
        raise NotImplementedError

if __name__ == '__main__': #pragma: no cover
    import pyHendrixDemersTools.Runner as Runner
    Runner.Runner().run(runFunction=None)
