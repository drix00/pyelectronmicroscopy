#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: electronmicroscopy.tem.cnse670_exam2

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

def getLineNumber():
    lineNumbers = range(1,6+1)
    #lineNumbers.extend(range(8,14+1))
    #lineNumbers.extend(range(16,22+1))
    #lineNumbers.extend(range(24,27+1))

    return lineNumbers

def _getFamilies():
    hklFamilies = {}

    hklFamilies[1] = [(1, 0, 0)]
    hklFamilies[2] = [(1, 1, 0)]
    hklFamilies[3] = [(1, 1, 1)]
    hklFamilies[4] = [(2, 0, 0)]
    hklFamilies[5] = [(2, 1, 0)]
    hklFamilies[6] = [(2, 1, 1)]

    return hklFamilies

def getFamily(lineNumber):
    hklFamilies = _getFamilies()

    return hklFamilies[lineNumber]

def run():
    lineNumbers = getLineNumber()
    print(lineNumbers)

if __name__ == '__main__':    #pragma: no cover
    import pyHendrixDemersTools.Runner as Runner
    Runner.Runner().run(runFunction=run)
