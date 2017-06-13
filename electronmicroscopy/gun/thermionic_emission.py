#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: electronmicroscopy.gun.thermionic_emission

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Model for a thermionic emission gun.
"""

###############################################################################
# Copyright 2017 Hendrix Demers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
###############################################################################

# Standard library modules.
import math

# Third party modules.
import numpy as np
import matplotlib.pyplot as plt

# Local modules.

# Project modules.

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


if __name__ == '__main__':  # pragma: no cover
    runGold()
