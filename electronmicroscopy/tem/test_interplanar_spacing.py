#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: electronmicroscopy.tem.test_interplanar_spacing

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module :py:mod:`electronmicroscopy.tem.interplanar_spacing`.
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

# Project modules.
from electronmicroscopy.tem.interplanar_spacing import interplanarSpacingCubic, interplanarSpacingTetragonal, \
    interplanarSpacingOrthorhombic, interplanarSpacingHexagonal, interplanarSpacingRhombohedral, \
    interplanarSpacingMonoclinic, interplanarSpacingTriclinic

# Globals and constants variables.


class TestInterplanarSpacing(unittest.TestCase):
    """
    TestCase class for the module `electronmicroscopy.tem.interplanar_spacing`.
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

    def test_interplanarSpacingCubic(self):
        a = 2.5

        planes = get_test_planes()
        expected_ds = get_expected_d_cubic()

        for expected_d, plane in zip(expected_ds, planes):
            actual_d = interplanarSpacingCubic(plane, a)

            self.assertAlmostEquals(expected_d, actual_d)

        self.assertEquals(len(expected_ds), len(planes))

        # self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_interplanarSpacingTetragonal(self):
        a = 2.5
        c = 3.6

        planes = get_test_planes()
        expected_ds = get_expected_d_tetragonal()

        for expected_d, plane in zip(expected_ds, planes):
            actual_d = interplanarSpacingTetragonal(plane, a, c)

            self.assertAlmostEquals(expected_d, actual_d)

        self.assertEquals(len(expected_ds), len(planes))

        # self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_interplanarSpacingOrthorhombic(self):
        a = 2.5
        b = 1.2
        c = 3.6

        planes = get_test_planes()
        expected_ds = get_expected_d_orthorhombic()

        for expected_d, plane in zip(expected_ds, planes):
            actual_d = interplanarSpacingOrthorhombic(plane, a, b, c)

            self.assertAlmostEquals(expected_d, actual_d)

        self.assertEquals(len(expected_ds), len(planes))

        # self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_interplanarSpacingHexagonal(self):
        a = 2.5
        c = 3.6

        planes = get_test_planes()
        expected_ds = get_expected_d_hexagonal()

        for expected_d, plane in zip(expected_ds, planes):
            actual_d = interplanarSpacingHexagonal(plane, a, c)

            self.assertAlmostEquals(expected_d, actual_d)

        self.assertEquals(len(expected_ds), len(planes))

        # self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_interplanarSpacingRhombohedral(self):
        a = 2.5
        alpha_deg = 39.56

        planes = get_test_planes()
        expected_ds = get_expected_d_rhombohedral()

        for expected_d, plane in zip(expected_ds, planes):
            actual_d = interplanarSpacingRhombohedral(plane, a, alpha_deg)

            self.assertAlmostEquals(expected_d, actual_d)

        self.assertEquals(len(expected_ds), len(planes))

        # self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_interplanarSpacingMonoclinic(self):
        a = 2.5
        b = 1.2
        c = 3.6
        beta_deg = 86.56

        planes = get_test_planes()
        expected_ds = get_expected_d_monoclinic()

        for expected_d, plane in zip(expected_ds, planes):
            actual_d = interplanarSpacingMonoclinic(plane, a, b, c, beta_deg)

            self.assertAlmostEquals(expected_d, actual_d)

        self.assertEquals(len(expected_ds), len(planes))

        # self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_interplanarSpacingTriclinic(self):
        a = 2.5
        b = 1.2
        c = 3.6
        alpha_deg = 39.56
        beta_deg = 86.56
        gamma_deg = 86.56

        planes = get_test_planes()
        expected_ds = get_expected_d_triclinic()

        for expected_d, plane in zip(expected_ds, planes):
            actual_d = interplanarSpacingTriclinic(plane, a, b, c, alpha_deg, beta_deg, gamma_deg)

            self.assertAlmostEquals(expected_d, actual_d)

        self.assertEquals(len(expected_ds), len(planes))

        # self.fail("Test if the testcase is working.")
        self.assert_(True)


def get_test_planes():
    planes = []

    planes.append((1, 0, 0))
    planes.append((0, 1, 0))
    planes.append((0, 0, 1))
    planes.append((-1, 0, 0))
    planes.append((0, -1, 0))
    planes.append((0, 0, -1))

    planes.append((3, 2, 1))
    planes.append((3, 1, 2))
    planes.append((1, 3, 2))
    planes.append((1, 2, 3))
    planes.append((2, 3, 1))
    planes.append((2, 1, 3))

    planes.append((-3, 2, 1))
    planes.append((-3, -2, 1))
    planes.append((-3, -2, -1))
    planes.append((3, -2, 1))
    planes.append((3, -2, -1))
    planes.append((3, 2, -1))

    return planes


def get_expected_d_cubic():
    values = []

    values.append(2.5)
    values.append(2.5)
    values.append(2.5)
    values.append(2.5)
    values.append(2.5)
    values.append(2.5)

    values.append(0.66815310478106094)
    values.append(0.66815310478106094)
    values.append(0.66815310478106094)
    values.append(0.66815310478106094)
    values.append(0.66815310478106094)
    values.append(0.66815310478106094)

    values.append(0.66815310478106094)
    values.append(0.66815310478106094)
    values.append(0.66815310478106094)
    values.append(0.66815310478106094)
    values.append(0.66815310478106094)
    values.append(0.66815310478106094)

    return values


def get_expected_d_tetragonal():
    values = []

    values.append(2.5)
    values.append(2.5)
    values.append(3.6)
    values.append(2.5)
    values.append(2.5)
    values.append(3.6)

    values.append(0.68086149017077868)
    values.append(0.72383197610000505)
    values.append(0.72383197610000505)
    values.append(0.81801282472381764)
    values.append(0.68086149017077868)
    values.append(0.81801282472381764)

    values.append(0.68086149017077868)
    values.append(0.68086149017077868)
    values.append(0.68086149017077868)
    values.append(0.68086149017077868)
    values.append(0.68086149017077868)
    values.append(0.68086149017077868)

    return values


def get_expected_d_orthorhombic():
    values = []

    values.append(2.5)
    values.append(1.2)
    values.append(3.6)
    values.append(2.5)
    values.append(1.2)
    values.append(3.6)

    values.append(0.48252690814099836)
    values.append(0.63977989039277638)
    values.append(0.38579735919182145)
    values.append(0.52470329858389009)
    values.append(0.3788541880465412)
    values.append(0.70205456580136349)

    values.append(0.48252690814099836)
    values.append(0.48252690814099836)
    values.append(0.48252690814099836)
    values.append(0.48252690814099836)
    values.append(0.48252690814099836)
    values.append(0.48252690814099836)

    return values


def get_expected_d_hexagonal():
    values = []

    values.append(2.1650635094610964)
    values.append(2.1650635094610964)
    values.append(3.6)
    values.append(2.1650635094610964)
    values.append(2.1650635094610964)
    values.append(3.6)

    values.append(0.49203841548543459)
    values.append(0.569620253164557)
    values.append(0.569620253164557)
    values.append(0.67608047940072502)
    values.append(0.49203841548543459)
    values.append(0.67608047940072502)

    values.append(0.7979613991076534)
    values.append(0.49203841548543459)
    values.append(0.49203841548543459)
    values.append(0.7979613991076534)
    values.append(0.7979613991076534)
    values.append(0.49203841548543459)

    return values


def get_expected_d_rhombohedral():
    values = []

    values.append(2.5)
    values.append(2.5)
    values.append(2.5)
    values.append(2.5)
    values.append(2.5)
    values.append(2.5)

    values.append(2.5)
    values.append(2.5)
    values.append(2.5)
    values.append(2.5)
    values.append(2.5)
    values.append(2.5)

    values.append(2.5)
    values.append(2.5)
    values.append(2.5)
    values.append(2.5)
    values.append(2.5)
    values.append(2.5)

    return values


def get_expected_d_monoclinic():
    values = []

    values.append(2.5)
    values.append(2.5)
    values.append(2.5)
    values.append(2.5)
    values.append(2.5)
    values.append(2.5)

    values.append(2.5)
    values.append(2.5)
    values.append(2.5)
    values.append(2.5)
    values.append(2.5)
    values.append(2.5)

    values.append(2.5)
    values.append(2.5)
    values.append(2.5)
    values.append(2.5)
    values.append(2.5)
    values.append(2.5)

    return values


def get_expected_d_triclinic():
    values = []

    values.append(2.5)
    values.append(2.5)
    values.append(2.5)
    values.append(2.5)
    values.append(2.5)
    values.append(2.5)

    values.append(2.5)
    values.append(2.5)
    values.append(2.5)
    values.append(2.5)
    values.append(2.5)
    values.append(2.5)

    values.append(2.5)
    values.append(2.5)
    values.append(2.5)
    values.append(2.5)
    values.append(2.5)
    values.append(2.5)

    return values


if __name__ == '__main__':  # pragma: no cover
    import nose
    nose.runmodule()
