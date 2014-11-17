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
__svnId__ = "$Id: AngleBetweenDirections.py 2293 2011-03-21 18:39:25Z hdemers $"

# Standard library modules.
import math

# Third party modules.

# Local modules.
import CrystalSystem

# Globals and constants variables.

def angleBetweenDirections_deg(direction1, direction2, crystalSystem):
    type = crystalSystem.getType()

    if type == CrystalSystem.CUBIC:
        return angleBetweenDirectionsCubic_deg(direction1, direction2)

    elif type == CrystalSystem.TETRAGONAL:
        a = crystalSystem.getA()
        c = crystalSystem.getC()
        return angleBetweenDirectionsTetragonal_deg(direction1, direction2, a, c)

    elif type == CrystalSystem.ORTHORHOMIC:
        a = crystalSystem.getA()
        b = crystalSystem.getB()
        c = crystalSystem.getC()
        return angleBetweenDirectionsOrthorhombic_deg(direction1, direction2, a, b, c)

    elif type == CrystalSystem.HEXAGONAL:
        a = crystalSystem.getA()
        c = crystalSystem.getC()
        return angleBetweenDirectionsHexagonal_deg(direction1, direction2, a, c)

    elif type == CrystalSystem.RHOMBOHEDRAL:
        a = crystalSystem.getA()
        # TODO: Find the correct value for c
        c = crystalSystem.getC()
        return angleBetweenDirectionsRhombohedral_deg(direction1, direction2, a, c)

    elif type == CrystalSystem.MONOCLINIC:
        a = crystalSystem.getA()
        b = crystalSystem.getB()
        c = crystalSystem.getC()
        beta = crystalSystem.getBeta()
        return angleBetweenDirectionsMonoclinic_deg(direction1, direction2, a, b, c, beta)

    elif type == CrystalSystem.TRICLINIC:
        a = crystalSystem.getA()
        b = crystalSystem.getB()
        c = crystalSystem.getC()
        alpha = crystalSystem.getAlpha()
        beta = crystalSystem.getBeta()
        gamma = crystalSystem.getGamma()
        return angleBetweenDirectionsTriclinic_deg(direction1, direction2, a, b, c, alpha, beta, gamma)

    return 0.0

def angleBetweenDirectionsCubic_deg(direction1, direction2):
    (h1, k1, l1) = direction1
    (h2, k2, l2) = direction2

    nominator = h1*h2 + k1*k2 + l1*l2

    factor1 = h1*h1 + k1*k1 + l1*l1
    factor2 = h2*h2 + k2*k2 + l2*l2
    denominator = math.sqrt(factor1*factor2)

    cosRho = nominator/denominator
    rho_rad = math.acos(cosRho)

    rho_deg = math.degrees(rho_rad)

    return rho_deg

if __name__ == '__main__':    #pragma: no cover
    import pyHendrixDemersTools.Runner as Runner
    Runner.Runner().run(runFunction=None)
