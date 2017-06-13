#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: electronmicroscopy.tem.angle_between_planes

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


def angleBetweenPlanes_deg(plane1, plane2, crystalSystem):
    type = crystalSystem.getType()

    if type == CrystalSystem.CUBIC:
        return angleBetweenPlanesCubic_deg(plane1, plane2)

    elif type == CrystalSystem.TETRAGONAL:
        a = crystalSystem.getA()
        c = crystalSystem.getC()
        return angleBetweenPlanesTetragonal_deg(plane1, plane2, a, c)

    elif type == CrystalSystem.ORTHORHOMIC:
        a = crystalSystem.getA()
        b = crystalSystem.getB()
        c = crystalSystem.getC()
        return angleBetweenPlanesOrthorhombic_deg(plane1, plane2, a, b, c)

    elif type == CrystalSystem.HEXAGONAL:
        a = crystalSystem.getA()
        c = crystalSystem.getC()
        return angleBetweenPlanesHexagonal_deg(plane1, plane2, a, c)

    elif type == CrystalSystem.RHOMBOHEDRAL:
        a = crystalSystem.getA()
        # TODO: Find the correct value for c
        c = crystalSystem.getC()
        return angleBetweenPlanesRhombohedral_deg(plane1, plane2, a, c)

    elif type == CrystalSystem.MONOCLINIC:
        a = crystalSystem.getA()
        b = crystalSystem.getB()
        c = crystalSystem.getC()
        beta = crystalSystem.getBeta()
        return angleBetweenPlanesMonoclinic_deg(plane1, plane2, a, b, c, beta)

    elif type == CrystalSystem.TRICLINIC:
        a = crystalSystem.getA()
        b = crystalSystem.getB()
        c = crystalSystem.getC()
        alpha = crystalSystem.getAlpha()
        beta = crystalSystem.getBeta()
        gamma = crystalSystem.getGamma()
        return angleBetweenPlanesTriclinic_deg(plane1, plane2, a, b, c, alpha, beta, gamma)

    return 0.0


def angleBetweenPlanesCubic_deg(plane1, plane2):
    (h1, k1, l1) = plane1
    (h2, k2, l2) = plane2

    nominator = h1*h2 + k1*k2 + l1*l2

    factor1 = h1*h1 + k1*k1 + l1*l1
    factor2 = h2*h2 + k2*k2 + l2*l2
    denominator = math.sqrt(factor1*factor2)

    cosPhi = nominator/denominator
    phi_rad = math.acos(cosPhi)

    phi_deg = math.degrees(phi_rad)

    return phi_deg


def runHomework05_3b():
    planesList = [((1,0,0), (0,1,0)), ((0,1,0), (0,0,1)), ((0,0,1), (1,0,0))]

    for planes in planesList:
        plane1, plane2 = planes
        angle_deg = angleBetweenPlanesCubic_deg(plane1, plane2)

        print("%s: %0.1f" % (str(planes), angle_deg))


if __name__ == '__main__':  # pragma: no cover
    runHomework05_3b()
