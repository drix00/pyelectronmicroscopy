#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: electronmicroanalysis.range.xray.test_anderson_hasler_model

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module :py:mod:`electronmicroanalysis.range.xray.anderson_hasler_model`.
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
import unittest

# Third party modules.

# Local modules.
from pywinxraydata.XRayDataWinxray import getIonizationEnergy_eV

# Project modules.
from electronmicroscopy.range.xray.anderson_hasler_model import range_generated_nm

# Globals and constants variables.


class TestAndersonHaslerModel(unittest.TestCase):
    """
    TestCase class for the module `electronmicroanalysis.range.xray.anderson_hasler_model`.
    """

    def setUp(self):
        """
        Setup method.
        """

        unittest.TestCase.setUp(self)

    def tearDown(self):
        """
        Teardown method.
        """

        unittest.TestCase.tearDown(self)

    def testSkeleton(self):
        """
        First test to check if the testcase is working with the testing framework.
        """

        # self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_range_generated_nm(self):
        """
        The function range_generated_nm.
        """
        electron_energy_keV = 20.0

        mg_k_ionization_energy_keV = getIonizationEnergy_eV(12, 'K') * 1.0e-3
        zn_l_ionization_energy_keV = getIonizationEnergy_eV(30, 'L') * 1.0e-3
        zn_k_ionization_energy_keV = getIonizationEnergy_eV(30, 'K') * 1.0e-3

        rho_mg_g_cm3 = 1.74
        rho_zn_g_cm3 = 7.130

        ranges_mg_ka = {0.0: 1362.6392089339756,
                        0.2: 2206.849017687324,
                        0.4: 3051.058826440672,
                        0.6: 3895.268635194019,
                        0.8: 4739.478443947369,
                        1.0: 5583.688252700716}

        ranges_zn_la = {0.0: 1367.3310426510272,
                        0.2: 2214.44763114402,
                        0.4: 3061.5642196370127,
                        0.6: 3908.6808081300046,
                        0.8: 4755.797396622998,
                        1.0: 5602.913985115991}

        ranges_zn_ka = {0.0: 971.2710501214905,
                        0.2: 1573.01253979446,
                        0.4: 2174.7540294674295,
                        0.6: 2776.4955191403983,
                        0.8: 3378.2370088133684,
                        1.0: 3979.9784984863372}

        for mg_weight_fraction in ranges_mg_ka:
            range_ref_nm = ranges_mg_ka[mg_weight_fraction]
            mass_density_g_cm3 = 1.0 / (mg_weight_fraction / rho_mg_g_cm3 + (1.0 - mg_weight_fraction) / rho_zn_g_cm3)
            range_nm = range_generated_nm(mass_density_g_cm3, electron_energy_keV, mg_k_ionization_energy_keV)
            self.assertAlmostEqual(range_ref_nm, range_nm)

        for mg_weight_fraction in ranges_zn_la:
            range_ref_nm = ranges_zn_la[mg_weight_fraction]
            mass_density_g_cm3 = 1.0 / (mg_weight_fraction / rho_mg_g_cm3 + (1.0 - mg_weight_fraction) / rho_zn_g_cm3)
            range_nm = range_generated_nm(mass_density_g_cm3, electron_energy_keV, zn_l_ionization_energy_keV)
            self.assertAlmostEqual(range_ref_nm, range_nm)

        for mg_weight_fraction in ranges_zn_ka:
            range_ref_nm = ranges_zn_ka[mg_weight_fraction]
            mass_density_g_cm3 = 1.0 / (mg_weight_fraction / rho_mg_g_cm3 + (1.0 - mg_weight_fraction) / rho_zn_g_cm3)
            range_nm = range_generated_nm(mass_density_g_cm3, electron_energy_keV, zn_k_ionization_energy_keV)
            self.assertAlmostEqual(range_ref_nm, range_nm)

        # self.fail("Test if the testcase is working.")
        self.assert_(True)


if __name__ == '__main__':  # pragma: no cover
    import nose

    nose.runmodule()
