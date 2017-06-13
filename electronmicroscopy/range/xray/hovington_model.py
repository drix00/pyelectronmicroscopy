#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: electronmicroanalysis.range.xray.hovington_model

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

X-ray generated range from Hovington et al. (1997).
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

# Third party modules.

# Local modules.

# Project modules.

# Globals and constants variables.


def range_generated_nm(mass_density_g_cm3, electron_energy_keV, ionization_energy_keV, atomic_number):
    """"
    X-ray generated range from Hovington et al. (1997).
    
    Hovington, P., Drouin, D., Gauvin, R. & Joy, D.C. (1997). Parameterization of the range of electrons at low energy 
    using the CASINO Monte Carlo program.Microsc Microanal 3 (suppl. 2), 885–886.

    .. note:: Equation taken from Gauvin (2007)
        Gauvin, R. A universal equation for the emission range of x-rays from bulk specimens Microscopy and 
        Microanalysis, 2007, 13, 354-357

    """
    Z = atomic_number

    k = 43.04 + 1.5 * Z + 5.4e-3 * Z * Z
    n = 1.755 - 7.4e-3 * Z + 3.0e-5 * Z * Z

    factor_1 = k / mass_density_g_cm3
    factor_2 = electron_energy_keV ** n - ionization_energy_keV ** n
    range_nm = factor_1 * factor_2

    return range_nm
