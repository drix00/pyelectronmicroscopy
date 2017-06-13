#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: electronmicroscopy.tem.diffraction_spot

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

# Globals and constants variables.
X = 0
Y = 1

class DiffractionSpot(object):
    def __init__(self, imagePosition=None, originPosition=None):
        self.setImagePosition(imagePosition)
        self.setOriginPosition(originPosition)

        self._position = None

    def setImagePosition(self, imagePosition):
        self._imagePosition = imagePosition

    def getImagePosition(self):
        return self._imagePosition

    def setOriginPosition(self, originPosition):
        self._originPosition = originPosition

    def getOriginPosition(self):
        return self._originPosition

    def getPosition(self):
        if self._position == None:
            self._computePosition()

        return self._position

    def _computePosition(self):
        x = self._imagePosition[X] - self._originPosition[X]
        y = self._imagePosition[Y] - self._originPosition[Y]

        self._position = (x, y)

    def getLength(self):
        x, y = self.getPosition()

        lengthSquared = x**2 + y**2
        length = math.sqrt(lengthSquared)

        return length

if __name__ == '__main__':    #pragma: no cover
    import pyHendrixDemersTools.Runner as Runner
    Runner.Runner().run(runFunction=None)
