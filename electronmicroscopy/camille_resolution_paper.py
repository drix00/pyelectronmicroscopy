#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: electronmicroscopy.camille_resolution_paper

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Compute the range for Camille resolution paper.
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
from electronmicroscopy.range.kanaya_okayama_models import range_nm as range_ko_nm

# Globals and constants variables.


def compute_range():
    atomic_numbers = [6, 79, 13, 26]
    energies_keV = [1.0, 10.0, 30.0]

    line = "%4s\t" % ('Z')
    for energy_keV in energies_keV:
        line += "%6.1fkeV\t" % (energy_keV)
    print(line)

    for atomic_number in atomic_numbers:
        line = "%4i\t" % (atomic_number)
        for energy_keV in energies_keV:
            range_nm = range_ko_nm(atomic_number, energy_keV * 1.0e3)
            line += "%9.1f\t" % (range_nm)
        print(line)


if __name__ == '__main__':  # pragma: no cover
    compute_range()
