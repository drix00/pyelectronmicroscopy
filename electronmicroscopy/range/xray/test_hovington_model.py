#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: electronmicroanalysis.range.xray.test_hovington_model

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module :py:mod:`electronmicroanalysis.range.xray.hovington_model`.
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
from electronmicroscopy.range.xray.hovington_model import range_generated_nm

# Globals and constants variables.


class TestAndersonHaslerModel(unittest.TestCase):
    """
    TestCase class for the module `electronmicroanalysis.range.xray.hovington_model`.
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

        ranges_mg_ka = {0.0: 1278.9754737764933,
                        0.2: 2071.3522328173326,
                        0.4: 2863.7289918581714,
                        0.6: 3656.1057508990098,
                        0.8: 4448.4825099398495,
                        1.0: 5240.8592689806865}

        ranges_zn_la = {0.0: 1381.3882008053752,
                        0.2: 2237.2137642928433,
                        0.4: 3093.0393277803114,
                        0.6: 3948.864891267778,
                        0.8: 4804.690454755248,
                        1.0: 5660.516018242714}

        ranges_zn_ka = {0.0: 946.6483237175872,
                        0.2: 1533.1350438138857,
                        0.4: 2119.621763910184,
                        0.6: 2706.1084840064814,
                        0.8: 3292.595204102781,
                        1.0: 3879.0819241990785}

        atomic_number = 12
        for mg_weight_fraction in ranges_mg_ka:
            range_ref_nm = ranges_mg_ka[mg_weight_fraction]
            mass_density_g_cm3 = 1.0 / (mg_weight_fraction / rho_mg_g_cm3 + (1.0 - mg_weight_fraction) / rho_zn_g_cm3)
            range_nm = range_generated_nm(mass_density_g_cm3, electron_energy_keV, mg_k_ionization_energy_keV,
                                          atomic_number)
            self.assertAlmostEqual(range_ref_nm, range_nm)

        atomic_number = 30
        for mg_weight_fraction in ranges_zn_la:
            range_ref_nm = ranges_zn_la[mg_weight_fraction]
            mass_density_g_cm3 = 1.0 / (mg_weight_fraction / rho_mg_g_cm3 + (1.0 - mg_weight_fraction) / rho_zn_g_cm3)
            range_nm = range_generated_nm(mass_density_g_cm3, electron_energy_keV, zn_l_ionization_energy_keV,
                                          atomic_number)
            self.assertAlmostEqual(range_ref_nm, range_nm)

        atomic_number = 30
        for mg_weight_fraction in ranges_zn_ka:
            range_ref_nm = ranges_zn_ka[mg_weight_fraction]
            mass_density_g_cm3 = 1.0 / (mg_weight_fraction / rho_mg_g_cm3 + (1.0 - mg_weight_fraction) / rho_zn_g_cm3)
            range_nm = range_generated_nm(mass_density_g_cm3, electron_energy_keV, zn_k_ionization_energy_keV,
                                          atomic_number)
            self.assertAlmostEqual(range_ref_nm, range_nm)

        # self.fail("Test if the testcase is working.")
        self.assert_(True)


if __name__ == '__main__':  # pragma: no cover
    import nose

    nose.runmodule()
