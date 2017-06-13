#!/usr/bin/env python
""" """

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2009 Hendrix Demers"
__license__ = ""

# Subversion informations for the file.
__svnRevision__ = "$Revision$"
__svnDate__ = "$Date$"
__svnId__ = "$Id$"

# Standard library modules.
import math

# Third party modules.
import numpy as np
import matplotlib.pyplot as plt

# Local modules.

# Globals and constants variables.

class ThermionicEmission(object):
    def __init__(self, workFrunctionEnergy_eV, parameterG=None, correctionFactor=0.5):
        self._boltzmannConstant_eV_K = 8.61734315e-5
        self._richardsonConstant_A_m2K2 = 1.20173e6

        self._workFrunctionEnergy_eV = workFrunctionEnergy_eV
        if parameterG is not None:
            self._parameterG = parameterG
        else:
            self._parameterG = self._computeParameterG_A_m2K2(correctionFactor)

    def _computeParameterG_A_m2K2(self, correctionFactor):
        parameterG_A_m2K2 = correctionFactor*self._richardsonConstant_A_m2K2
        return parameterG_A_m2K2

    def currentDensity_A_m2(self, temperature_K):
        factor = self._parameterG*temperature_K**2
        exponentTerm = self._workFrunctionEnergy_eV/(self._boltzmannConstant_eV_K*temperature_K)

        currentDensity_A_m2 = factor*math.exp(-exponentTerm)
        return currentDensity_A_m2


def runGold():
    te = ThermionicEmission(5.1)

    temperatures_K = np.arange(273, 1500, 1)

    currentDensities_A_m2 = [te.currentDensity_A_m2(T) for T in temperatures_K]

    temperatures_C = temperatures_K + 273.15
    plt.figure()
    plt.semilogy(temperatures_C, currentDensities_A_m2)

    plt.xlabel("T (C)")
    plt.ylabel("J (A/m2)")

    plt.axvline(500)
    plt.axvline(700)

    plt.show()

if __name__ == '__main__':    #pragma: no cover
    import pyHendrixDemersTools.Runner as Runner
    Runner.Runner().run(runFunction=runGold)
