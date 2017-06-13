#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: ${module}

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

${description}
"""

###############################################################################
# Copyright ${year} Hendrix Demers
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

# Project modules.

# Globals and constants variables.
REST_MASS_kg = 9.1091e-31
CHARGE_C = -1.602e-19
KINETIC_ENERGY_eV = 1.0
KINETIC_ENERGY_J = 1.602e-19
VELOCITY_LIGHT_m_s = 2.9979e8
REST_ENERGY_eV = 511e3
PLANCKS_CONSTANT_J_s = 6.6256e-34
SPIN_J_s = PLANCKS_CONSTANT_J_s/(4.0*math.pi)


class ElectronProperties(object):
    def mass(self):
        raise NotImplementedError
