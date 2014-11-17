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
import math

# Third party modules.

# Local modules.
import DatabasesTools.ElementProperties as ElementProperties

# Project modules

# Globals and constants variables.

def range_nm(atomicNumber, energy_eV):
    """
    Compute the non-relativistic range from Kanaya and Okayama model.

    """
    if type(atomicNumber) == type([]):
        return _rangeOriginalPaperElements_nm(atomicNumber, energy_eV)

    return _rangeOriginalPaper_nm(atomicNumber, energy_eV)

def computeMeanAtomicNumber(elements):
    meanAtomicNumber = 0.0
    for Z, wF in elements:
        meanAtomicNumber += Z * wF

    assert meanAtomicNumber > 0.0
    return meanAtomicNumber

def _rangeOriginalPaper_nm(atomicNumber, energy_eV):
    """
    Compute the non-relativistic range from Kanaya and Okayama model.

    """
    rho_g_cm3 = ElementProperties.getMassDensity_g_cm3(atomicNumber)
    A_g_mol = ElementProperties.getAtomicMass_g_mol(atomicNumber)

    numericalFactor = 5.025e-12
    empiricalConstant = 0.182

    numerator = numericalFactor*A_g_mol*math.pow(energy_eV, 5.0/3.0)

    denominator = rho_g_cm3*empiricalConstant*math.pow(float(atomicNumber), 8.0/9.0)

    range_cm = numerator/denominator

    range_nm = range_cm*1.0e7

    return range_nm

def _rangeOriginalPaperElements_nm(elements, energy_eV):
    """
    Compute the non-relativistic range from Kanaya and Okayama model.

    """
    range_nm = 0.0
    for atomicNumber, weightFraction in elements:
        rho_g_cm3 = ElementProperties.getMassDensity_g_cm3(atomicNumber)
        A_g_mol = ElementProperties.getAtomicMass_g_mol(atomicNumber)

        numericalFactor = 5.025e-12
        empiricalConstant = 0.182

        numerator = numericalFactor*A_g_mol*math.pow(energy_eV, 5.0/3.0)

        denominator = weightFraction*rho_g_cm3*empiricalConstant*math.pow(float(atomicNumber), 8.0/9.0)

        range_cm = numerator/denominator

        range_nm += range_cm*1.0e7

    return range_nm

def _rangeGolsteinBook_nm(atomicNumber, energy_eV):
    """
    Compute the non-relativistic range from Kanaya and Okayama model.

    """
    rho_g_cm3 = ElementProperties.getMassDensity_g_cm3(atomicNumber)
    A_g_mol = ElementProperties.getAtomicMass_g_mol(atomicNumber)

    numericalFactor = 0.0276
    energy_keV = energy_eV*1.0e-3

    numerator = numericalFactor*A_g_mol*math.pow(energy_keV, 1.67)

    denominator = rho_g_cm3*math.pow(float(atomicNumber), 0.89)

    range_um = numerator/denominator

    range_nm = range_um*1.0e3

    return range_nm

def rangeRelativistic_nm(atomicNumber, energy_eV):
    """
    Compute the non-relativistic range from Kanaya and Okayama model.

    """
    rho_g_cm3 = ElementProperties.getMassDensity_g_cm3(atomicNumber)
    A_g_mol = ElementProperties.getAtomicMass_g_mol(atomicNumber)

    numerator = math.pow(1.0 + 0.978e-6*energy_eV, 5.0/3.0)
    denominator = math.pow(1.0 + 1.957e-6*energy_eV, 4.0/3.0)

    relativisticFactor = numerator/denominator

    numericalFactor = 2.76e-11

    numerator = numericalFactor*A_g_mol*math.pow(energy_eV, 5.0/3.0)

    denominator = rho_g_cm3*math.pow(float(atomicNumber), 8.0/9.0)

    range_cm = numerator/denominator
    range_cm *= relativisticFactor
    range_nm = range_cm*1.0e7

    return range_nm


if __name__ == '__main__':  #pragma: no cover
    import pyHendrixDemersTools.Runner as Runner
    Runner.Runner().run(runFunction=None)
