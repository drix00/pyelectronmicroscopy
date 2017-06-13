#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: electronmicroscopy.tem.crystal_system

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

# Third party modules.

# Local modules.

# Project modules.

# Globals and constants variables.
CUBIC = "Cubic"
TETRAGONAL = "Tetragonal"
ORTHORHOMIC = "Orthorhomic"
HEXAGONAL = "Hexagonal"
RHOMBOHEDRAL = "Rhombohedral"
MONOCLINIC = "Monoclinic"
TRICLINIC = "Triclinic"

class CrystalSystem(object):
    def __init__(self):
        self._a = None
        self._b = None
        self._c = None
        self._alpha = None
        self._beta = None
        self._gamma = None

        self._type = None

    def getA(self):
        return self._a

    def getB(self):
        return self._b

    def getC(self):
        return self._c

    def getAlpha(self):
        return self._alpha

    def getBeta(self):
        return self._beta

    def getGamma(self):
        return self._gamma

    def getType(self):
        return self._type

if __name__ == '__main__':    #pragma: no cover
    import pyHendrixDemersTools.Runner as Runner
    Runner.Runner().run(runFunction=None)
