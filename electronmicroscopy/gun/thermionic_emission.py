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
    def __init__(self, work_function_energy_eV, parameter_g=None, correction_factor=0.5):
        self._boltzmannConstant_eV_K = 8.61734315e-5
        self._richardsonConstant_A_m2K2 = 1.20173e6

        self._work_function_energy_eV = work_function_energy_eV
        if parameter_g is not None:
            self._parameterG = parameter_g
        else:
            self._parameterG = self._compute_parameter_g_A_m2K2(correction_factor)

    def _compute_parameter_g_A_m2K2(self, correction_factor):
        parameter_g_A_m2K2 = correction_factor * self._richardsonConstant_A_m2K2
        return parameter_g_A_m2K2

    def current_density_A_m2(self, temperature_K):
        factor = self._parameterG*temperature_K**2
        exponent_term = self._work_function_energy_eV / (self._boltzmannConstant_eV_K * temperature_K)

        current_density_A_m2 = factor*math.exp(-exponent_term)
        return current_density_A_m2


def run_gold():
    te = ThermionicEmission(5.1)

    temperatures_K = np.arange(273, 1500, 1)

    current_densities_A_m2 = [te.current_density_A_m2(T) for T in temperatures_K]

    temperatures_C = temperatures_K + 273.15
    plt.figure()
    plt.semilogy(temperatures_C, current_densities_A_m2)

    plt.xlabel("T (C)")
    plt.ylabel("J (A/m2)")

    plt.axvline(500)
    plt.axvline(700)

    plt.show()


if __name__ == '__main__':  # pragma: no cover
    run_gold()
