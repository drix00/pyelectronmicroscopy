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
__svnId__ = "$Id: InterplanarSpacing.py 2293 2011-03-21 18:39:25Z hdemers $"

# Standard library modules.
import math

# Third party modules.

# Local modules.
import pyElectronMicroscopy.TEM.CrystalSystem

# Globals and constants variables.

def interplanarSpacing(plane, crystalSystem):
    type = crystalSystem.getType()

    if type == CrystalSystem.CUBIC:
        a = crystalSystem.getA()
        return interplanarSpacingCubic(plane, a)

    elif type == CrystalSystem.TETRAGONAL:
        a = crystalSystem.getA()
        c = crystalSystem.getC()
        return interplanarSpacingTetragonal(plane, a, c)

    elif type == CrystalSystem.ORTHORHOMIC:
        a = crystalSystem.getA()
        b = crystalSystem.getB()
        c = crystalSystem.getC()
        return interplanarSpacingOrthorhombic(plane, a, b, c)

    elif type == CrystalSystem.HEXAGONAL:
        a = crystalSystem.getA()
        c = crystalSystem.getC()
        return interplanarSpacingHexagonal(plane, a, c)

    elif type == CrystalSystem.RHOMBOHEDRAL:
        a = crystalSystem.getA()
        alpha = crystalSystem.getAlpha()
        return interplanarSpacingRhombohedral(plane, a, alpha)

    elif type == CrystalSystem.MONOCLINIC:
        a = crystalSystem.getA()
        b = crystalSystem.getB()
        c = crystalSystem.getC()
        beta = crystalSystem.getBeta()
        return interplanarSpacingMonoclinic(plane, a, b, c, beta)

    elif type == CrystalSystem.TRICLINIC:
        a = crystalSystem.getA()
        b = crystalSystem.getB()
        c = crystalSystem.getC()
        alpha = crystalSystem.getAlpha()
        beta = crystalSystem.getBeta()
        gamma = crystalSystem.getGamma()
        return interplanarSpacingTriclinic(plane, a, b, c, alpha, beta, gamma)

    return 0.0

def interplanarSpacingCubic(plane, a):
    reciprocalD2 = _reciprocalD2Cubic(plane, a)

    return _reciprocalD2ToD(reciprocalD2)

def _reciprocalD2Cubic(plane, a):
    h,k,l = plane

    nominator = h**2 + k**2 + l**2
    denominator = a**2
    reciprocalD2 = nominator/denominator

    return reciprocalD2

def _reciprocalD2ToD(reciprocalD2):
        d = 1.0 / math.sqrt(reciprocalD2)
        return d

def interplanarSpacingTetragonal(plane, a, c):
    reciprocalD2 = _reciprocalD2Tetragonal(plane, a, c)

    return _reciprocalD2ToD(reciprocalD2)

def _reciprocalD2Tetragonal(plane, a, c):
    h,k,l = plane

    nominator = h**2 + k**2
    denominator = a**2
    reciprocalD2 = nominator/denominator

    reciprocalD2 += (l**2)/(c**2)

    return reciprocalD2

def interplanarSpacingOrthorhombic(plane, a, b, c):
    reciprocalD2 = _reciprocalD2Orthorhombic(plane, a, b, c)

    return _reciprocalD2ToD(reciprocalD2)

def _reciprocalD2Orthorhombic(plane, a, b, c):
    h,k,l = plane

    reciprocalD2 = (h**2)/(a**2) + (k**2)/(b**2) + (l**2)/(c**2)

    return reciprocalD2

def interplanarSpacingHexagonal(plane, a, c):
    reciprocalD2 = _reciprocalD2Hexagonal(plane, a, c)

    return _reciprocalD2ToD(reciprocalD2)

def _reciprocalD2Hexagonal(plane, a, c):
    h,k,l = plane

    nominator = 4.0*(h**2 + h*k + k**2)
    denominator = 3.0*a**2
    reciprocalD2 = nominator/denominator

    reciprocalD2 += (l**2)/(c**2)

    return reciprocalD2

def interplanarSpacingRhombohedral(plane, a, alpha_deg):
    reciprocalD2 = _reciprocalD2Rhombohedral(plane, a, alpha_deg)

    return _reciprocalD2ToD(reciprocalD2)

# TODO: Implement this method.
def _reciprocalD2Rhombohedral(plane, a, alpha_deg):
    #h,k,l = plane

    reciprocalD2 = 1.0/a**2

    return reciprocalD2

def interplanarSpacingMonoclinic(plane, a, b, c, beta_deg):
    reciprocalD2 = _reciprocalD2Monoclinic(plane, a, b, c, beta_deg)

    return _reciprocalD2ToD(reciprocalD2)

# TODO: Implement this method.
def _reciprocalD2Monoclinic(plane, a, b, c, beta_deg):
    #h,k,l = plane

    reciprocalD2 = 1.0/a**2

    return reciprocalD2

def interplanarSpacingTriclinic(plane, a, b, c, alpha_deg, beta_deg, gamma_deg):
    reciprocalD2 = _reciprocalD2Triclinic(plane, a, b, c, alpha_deg, beta_deg, gamma_deg)

    return _reciprocalD2ToD(reciprocalD2)

# TODO: Implement this method.
def _reciprocalD2Triclinic(plane, a, b, c, alpha_deg, beta_deg, gamma_deg):
    #h,k,l = plane

    reciprocalD2 = 1.0/a**2

    return reciprocalD2

if __name__ == '__main__':    #pragma: no cover
    import pyHendrixDemersTools.Runner as Runner
    Runner.Runner().run(runFunction=None)
