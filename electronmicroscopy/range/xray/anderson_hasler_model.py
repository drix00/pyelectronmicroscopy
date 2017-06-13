#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: electronmicroanalysis.range.xray.anderson_hasler_model

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

X-ray generated range from Anderson Hasler (1966).
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


def range_generated_nm(mass_density_g_cm3, electron_energy_keV, ionization_energy_keV):
    """"
    X-ray generated range from Anderson and Hasler (1966).
    
    Anderson, C.A. & Hasler, M.F. (1966). Extension of electron microprobe techniques to biochemistry by the use of 
    long wavelength X-rays. In Proceedings of the Fourth International Conference on X-ray Optics and Microanalysis, 
    Castaing, R., Deschamps, P. & Philibert, J. (Eds.), pp. 310–327. Paris: Hermann.

    .. note:: Equation taken from Gauvin (2007)
        Gauvin, R. A universal equation for the emission range of x-rays from bulk specimens Microscopy and 
        Microanalysis, 2007, 13, 354-357
         
    """
    factor_1 = 0.064 / mass_density_g_cm3
    factor_2 = electron_energy_keV ** 1.68 - ionization_energy_keV ** 1.68
    range_um = factor_1 * factor_2
    range_nm = range_um * 1.0e3

    return range_nm
