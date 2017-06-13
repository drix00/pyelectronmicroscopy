#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: electronmicroscopy.tem.diffraction_vector

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
import numpy as np

# Local modules.

# Project modules.

# Globals and constants variables.
X = 0
Y = 1

class DiffractionVector(object):
    def __init__(self, id, spot):
        self._id = id
        self.setSpot(spot)

    def setSpot(self, spot):
        self._spot = spot
        x, y = spot.getPosition()
        #self._vector = visual.vector(x, y, 0.0)
        self._vector = np.array((x, y, 0.0))

    def getPosition(self):
        return self._spot.getPosition()

    def getLength(self):
        return np.linalg.norm(self._vector)

    def getVector(self):
        return self._vector

    def __eq__(self, other):
        if self.getLength() == other.getLength():
            return True
        else:
            return False

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if self.getLength() < other.getLength():
            return True
        else:
            return False

if __name__ == '__main__':    #pragma: no cover
    import pyHendrixDemersTools.Runner as Runner
    Runner.Runner().run(runFunction=None)
