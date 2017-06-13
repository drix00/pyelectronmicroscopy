#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: electronmicroanalysis.range.xray.gauvin_model

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

X-ray emitted range from Gauvin (2007).
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
from math import log, sin, radians, exp

# Third party modules.

# Local modules.

# Project modules.
from electronmicroscopy.range.xray.hovington_model import range_generated_nm

# Globals and constants variables.


def range_emitted_nm(mass_density_g_cm3, electron_energy_keV, ionization_energy_keV, atomic_number, lambda_nm,
                     takeoff_angle_deg, alpha=0.95):
    """"
    X-ray emitted range from Gauvin (2007).

    Gauvin, R. A universal equation for the emission range of x-rays from bulk specimens Microscopy and 
    Microanalysis, 2007, 13, 354-357

    """
    x_g_nm = range_generated_nm(mass_density_g_cm3, electron_energy_keV, ionization_energy_keV, atomic_number)

    factor_1 = log(1.0 / (1.0 - alpha))
    factor_2 = lambda_nm * sin(radians(takeoff_angle_deg))
    factor_3 = 1.0 - exp(-x_g_nm / factor_1 / factor_2)
    range_nm = factor_1 * factor_2 * factor_3

    return range_nm
