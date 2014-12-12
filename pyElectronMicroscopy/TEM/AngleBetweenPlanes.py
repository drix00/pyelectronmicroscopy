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
__svnId__ = "$Id: AngleBetweenPlanes.py 2293 2011-03-21 18:39:25Z hdemers $"

# Standard library modules.
import math

# Third party modules.

# Local modules.
import pyElectronMicroscopy.TEM.CrystalSystem as CrystalSystem

# Globals and constants variables.

def angleBetweenPlanes_deg(plane1, plane2, crystalSystem):
    type = crystalSystem.getType()

    if type == CrystalSystem.CUBIC:
        return angleBetweenPlanesCubic_deg(plane1, plane2)

    elif type == CrystalSystem.TETRAGONAL:
        a = crystalSystem.getA()
        c = crystalSystem.getC()
        return angleBetweenPlanesTetragonal_deg(plane1, plane2, a, c)

    elif type == CrystalSystem.ORTHORHOMIC:
        a = crystalSystem.getA()
        b = crystalSystem.getB()
        c = crystalSystem.getC()
        return angleBetweenPlanesOrthorhombic_deg(plane1, plane2, a, b, c)

    elif type == CrystalSystem.HEXAGONAL:
        a = crystalSystem.getA()
        c = crystalSystem.getC()
        return angleBetweenPlanesHexagonal_deg(plane1, plane2, a, c)

    elif type == CrystalSystem.RHOMBOHEDRAL:
        a = crystalSystem.getA()
        # TODO: Find the correct value for c
        c = crystalSystem.getC()
        return angleBetweenPlanesRhombohedral_deg(plane1, plane2, a, c)

    elif type == CrystalSystem.MONOCLINIC:
        a = crystalSystem.getA()
        b = crystalSystem.getB()
        c = crystalSystem.getC()
        beta = crystalSystem.getBeta()
        return angleBetweenPlanesMonoclinic_deg(plane1, plane2, a, b, c, beta)

    elif type == CrystalSystem.TRICLINIC:
        a = crystalSystem.getA()
        b = crystalSystem.getB()
        c = crystalSystem.getC()
        alpha = crystalSystem.getAlpha()
        beta = crystalSystem.getBeta()
        gamma = crystalSystem.getGamma()
        return angleBetweenPlanesTriclinic_deg(plane1, plane2, a, b, c, alpha, beta, gamma)

    return 0.0

def angleBetweenPlanesCubic_deg(plane1, plane2):
    (h1, k1, l1) = plane1
    (h2, k2, l2) = plane2

    nominator = h1*h2 + k1*k2 + l1*l2

    factor1 = h1*h1 + k1*k1 + l1*l1
    factor2 = h2*h2 + k2*k2 + l2*l2
    denominator = math.sqrt(factor1*factor2)

    cosPhi = nominator/denominator
    phi_rad = math.acos(cosPhi)

    phi_deg = math.degrees(phi_rad)

    return phi_deg

def runHomework05_3b():
    planesList = [((1,0,0), (0,1,0)), ((0,1,0), (0,0,1)), ((0,0,1), (1,0,0))]

    for planes in planesList:
        plane1, plane2 = planes
        angle_deg = angleBetweenPlanesCubic_deg(plane1, plane2)

        print("%s: %0.1f" % (str(planes), angle_deg))

if __name__ == '__main__':    #pragma: no cover
    import pyHendrixDemersTools.Runner as Runner
    Runner.Runner().run(runFunction=runHomework05_3b)
