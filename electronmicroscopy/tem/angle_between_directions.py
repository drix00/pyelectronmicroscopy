#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: electronmicroscopy.tem.angle_between_directions

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

 
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

# Project modules.
import electronmicroscopy.tem.crystal_system as CrystalSystem

# Globals and constants variables.


def angleBetweenDirections_deg(direction1, direction2, crystalSystem):
    type = crystalSystem.getType()

    if type == CrystalSystem.CUBIC:
        return angleBetweenDirectionsCubic_deg(direction1, direction2)

    elif type == CrystalSystem.TETRAGONAL:
        a = crystalSystem.getA()
        c = crystalSystem.getC()
        return angleBetweenDirectionsTetragonal_deg(direction1, direction2, a, c)

    elif type == CrystalSystem.ORTHORHOMIC:
        a = crystalSystem.getA()
        b = crystalSystem.getB()
        c = crystalSystem.getC()
        return angleBetweenDirectionsOrthorhombic_deg(direction1, direction2, a, b, c)

    elif type == CrystalSystem.HEXAGONAL:
        a = crystalSystem.getA()
        c = crystalSystem.getC()
        return angleBetweenDirectionsHexagonal_deg(direction1, direction2, a, c)

    elif type == CrystalSystem.RHOMBOHEDRAL:
        a = crystalSystem.getA()
        # TODO: Find the correct value for c
        c = crystalSystem.getC()
        return angleBetweenDirectionsRhombohedral_deg(direction1, direction2, a, c)

    elif type == CrystalSystem.MONOCLINIC:
        a = crystalSystem.getA()
        b = crystalSystem.getB()
        c = crystalSystem.getC()
        beta = crystalSystem.getBeta()
        return angleBetweenDirectionsMonoclinic_deg(direction1, direction2, a, b, c, beta)

    elif type == CrystalSystem.TRICLINIC:
        a = crystalSystem.getA()
        b = crystalSystem.getB()
        c = crystalSystem.getC()
        alpha = crystalSystem.getAlpha()
        beta = crystalSystem.getBeta()
        gamma = crystalSystem.getGamma()
        return angleBetweenDirectionsTriclinic_deg(direction1, direction2, a, b, c, alpha, beta, gamma)

    return 0.0


def angleBetweenDirectionsCubic_deg(direction1, direction2):
    (h1, k1, l1) = direction1
    (h2, k2, l2) = direction2

    nominator = h1*h2 + k1*k2 + l1*l2

    factor1 = h1*h1 + k1*k1 + l1*l1
    factor2 = h2*h2 + k2*k2 + l2*l2
    denominator = math.sqrt(factor1*factor2)

    cosRho = nominator/denominator
    rho_rad = math.acos(cosRho)

    rho_deg = math.degrees(rho_rad)

    return rho_deg
