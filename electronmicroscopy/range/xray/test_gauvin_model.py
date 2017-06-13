#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: electronmicroanalysis.range.xray.test_gauvin_model

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module :py:mod:`electronmicroanalysis.range.xray.gauvin_model`.
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
from pywinxraydata.XRayDataWinxray import getIonizationEnergy_eV, getXRayEnergy_eV
from pyMassAbsorptionCoefficients.models.chantler2005 import Chantler2005

# Project modules.
from electronmicroscopy.range.xray.gauvin_model import range_emitted_nm

# Globals and constants variables.


class TestAndersonHaslerModel(unittest.TestCase):
    """
    TestCase class for the module `electronmicroanalysis.range.xray.gauvin_model`.
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

    def test_range_emitted_nm(self):
        """
        The function range_generated_nm.
        """

        electron_energy_keV = 20.0
        takeoff_angle_deg = 40.0
        alpha = 0.95

        chantler2005 = Chantler2005()

        mg_k_ionization_energy_keV = getIonizationEnergy_eV(12, 'K') * 1.0e-3
        zn_l_ionization_energy_keV = getIonizationEnergy_eV(30, 'L') * 1.0e-3
        zn_k_ionization_energy_keV = getIonizationEnergy_eV(30, 'K') * 1.0e-3

        mg_k_xray_energy_eV = getXRayEnergy_eV(12, 'Ka1')
        zn_l_xray_energy_eV = getXRayEnergy_eV(30, 'La')
        zn_k_xray_energy_eV = getXRayEnergy_eV(30, 'Ka1')

        rho_mg_g_cm3 = 1.74
        rho_zn_g_cm3 = 7.130

        ranges_mg_ka = {0.0: 356.47308121470331,
                        0.2: 689.96526494202976,
                        0.4: 1168.73335841685,
                        0.6: 1880.9789082230711,
                        0.8: 2978.1047022074458,
                        1.0: 4724.1820099776878}

        ranges_zn_la = {0.0: 983.7700861914185,
                        0.2: 1637.1895003835803,
                        0.4: 2326.6129036971597,
                        0.6: 3054.1637914274002,
                        0.8: 3822.0945206235738,
                        1.0: 4632.7942436117628}

        ranges_zn_ka = {0.0: 939.30569943692569,
                        0.2: 1521.9618933746599,
                        0.4: 2105.1684440349391,
                        0.6: 2688.9258720078997,
                        0.8: 3273.2346983764264,
                        1.0: 3858.0954447165973}

        atomic_number = 12
        for mg_weight_fraction in ranges_mg_ka:
            range_ref_nm = ranges_mg_ka[mg_weight_fraction]
            mass_density_g_cm3 = 1.0 / (mg_weight_fraction / rho_mg_g_cm3 + (1.0 - mg_weight_fraction) / rho_zn_g_cm3)

            mac_cm2_g = chantler2005.compute_mac_cm2_g(mg_k_xray_energy_eV, 12) * mg_weight_fraction + \
                        chantler2005.compute_mac_cm2_g(mg_k_xray_energy_eV, 30) * (1.0 - mg_weight_fraction)
            lambda_cm = 1.0 / (mass_density_g_cm3 * mac_cm2_g)
            lambda_nm = lambda_cm * 1.0e7

            range_nm = range_emitted_nm(mass_density_g_cm3, electron_energy_keV, mg_k_ionization_energy_keV,
                                        atomic_number, lambda_nm, takeoff_angle_deg, alpha)
            self.assertAlmostEqual(range_ref_nm, range_nm)

        atomic_number = 30
        for mg_weight_fraction in ranges_zn_la:
            range_ref_nm = ranges_zn_la[mg_weight_fraction]
            mass_density_g_cm3 = 1.0 / (mg_weight_fraction / rho_mg_g_cm3 + (1.0 - mg_weight_fraction) / rho_zn_g_cm3)

            mac_cm2_g = chantler2005.compute_mac_cm2_g(zn_l_xray_energy_eV, 12) * mg_weight_fraction + \
                        chantler2005.compute_mac_cm2_g(zn_l_xray_energy_eV, 30) * (1.0 - mg_weight_fraction)
            lambda_cm = 1.0 / (mass_density_g_cm3 * mac_cm2_g)
            lambda_nm = lambda_cm * 1.0e7

            range_nm = range_emitted_nm(mass_density_g_cm3, electron_energy_keV, zn_l_ionization_energy_keV,
                                          atomic_number, lambda_nm, takeoff_angle_deg, alpha)
            self.assertAlmostEqual(range_ref_nm, range_nm)

        atomic_number = 30
        for mg_weight_fraction in ranges_zn_ka:
            range_ref_nm = ranges_zn_ka[mg_weight_fraction]
            mass_density_g_cm3 = 1.0 / (mg_weight_fraction / rho_mg_g_cm3 + (1.0 - mg_weight_fraction) / rho_zn_g_cm3)

            mac_cm2_g = chantler2005.compute_mac_cm2_g(zn_k_xray_energy_eV, 12) * mg_weight_fraction + \
                        chantler2005.compute_mac_cm2_g(zn_k_xray_energy_eV, 30) * (1.0 - mg_weight_fraction)
            lambda_cm = 1.0 / (mass_density_g_cm3 * mac_cm2_g)
            lambda_nm = lambda_cm * 1.0e7

            range_nm = range_emitted_nm(mass_density_g_cm3, electron_energy_keV, zn_k_ionization_energy_keV,
                                          atomic_number, lambda_nm, takeoff_angle_deg, alpha)
            self.assertAlmostEqual(range_ref_nm, range_nm)

        # self.fail("Test if the testcase is working.")
        self.assert_(True)


if __name__ == '__main__':  # pragma: no cover
    import nose

    nose.runmodule()
