#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: electronmicroscopy.range.kanaya_okayama_models

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Electron range from Kanaya and Okayama.
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

# Local modules.
import pywinxraydata.ElementProperties as ElementProperties

# Project modules

# Globals and constants variables.


def range_nm(atomic_number, energy_eV):
    """
    Compute the non-relativistic range from Kanaya and Okayama model.

    """
    if type(atomic_number) == type([]):
        return _range_original_paper_elements_nm(atomic_number, energy_eV)

    return _range_original_paper_nm(atomic_number, energy_eV)


def compute_mean_atomic_number(elements):
    mean_atomic_number = 0.0
    for Z, wF in elements:
        mean_atomic_number += Z * wF

    assert mean_atomic_number > 0.0
    return mean_atomic_number


def _range_original_paper_nm(atomic_number, energy_eV):
    """
    Compute the non-relativistic range from Kanaya and Okayama model.

    """
    rho_g_cm3 = ElementProperties.getMassDensity_g_cm3(atomic_number)
    A_g_mol = ElementProperties.getAtomicMass_g_mol(atomic_number)

    numerical_factor = 5.025e-12
    empirical_constant = 0.182

    numerator = numerical_factor*A_g_mol*math.pow(energy_eV, 5.0/3.0)

    denominator = rho_g_cm3*empirical_constant*math.pow(float(atomic_number), 8.0 / 9.0)

    range_cm = numerator/denominator

    range_value_nm = range_cm*1.0e7

    return range_value_nm


def _range_original_paper_elements_nm(elements, energy_eV):
    """
    Compute the non-relativistic range from Kanaya and Okayama model.

    """
    range_value_nm = 0.0
    for atomicNumber, weightFraction in elements:
        rho_g_cm3 = ElementProperties.getMassDensity_g_cm3(atomicNumber)
        A_g_mol = ElementProperties.getAtomicMass_g_mol(atomicNumber)

        numerical_factor = 5.025e-12
        empirical_constant = 0.182

        numerator = numerical_factor*A_g_mol*math.pow(energy_eV, 5.0/3.0)

        denominator = weightFraction*rho_g_cm3*empirical_constant*math.pow(float(atomicNumber), 8.0/9.0)

        range_cm = numerator/denominator

        range_value_nm += range_cm*1.0e7

    return range_value_nm


def _range_goldstein_book_nm(atomic_number, energy_eV):
    """
    Compute the non-relativistic range from Kanaya and Okayama model.

    """
    rho_g_cm3 = ElementProperties.getMassDensity_g_cm3(atomic_number)
    A_g_mol = ElementProperties.getAtomicMass_g_mol(atomic_number)

    numerical_factor = 0.0276
    energy_keV = energy_eV*1.0e-3

    numerator = numerical_factor*A_g_mol*math.pow(energy_keV, 1.67)

    denominator = rho_g_cm3*math.pow(float(atomic_number), 0.89)

    range_um = numerator/denominator

    range_value_nm = range_um*1.0e3

    return range_value_nm


def range_relativistic_nm(atomic_number, energy_eV):
    """
    Compute the non-relativistic range from Kanaya and Okayama model.

    """
    rho_g_cm3 = ElementProperties.getMassDensity_g_cm3(atomic_number)
    A_g_mol = ElementProperties.getAtomicMass_g_mol(atomic_number)

    numerator = math.pow(1.0 + 0.978e-6*energy_eV, 5.0/3.0)
    denominator = math.pow(1.0 + 1.957e-6*energy_eV, 4.0/3.0)

    relativistic_factor = numerator/denominator

    numerical_factor = 2.76e-11

    numerator = numerical_factor*A_g_mol*math.pow(energy_eV, 5.0/3.0)

    denominator = rho_g_cm3*math.pow(float(atomic_number), 8.0 / 9.0)

    range_cm = numerator/denominator
    range_cm *= relativistic_factor
    range_value_nm = range_cm*1.0e7

    return range_value_nm
