#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: electronmicroscopy.tem.test_diffraction_spot

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module :py:mod:`electronmicroscopy.tem.diffraction_spot`.
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
from electronmicroscopy.tem.diffraction_spot import DiffractionSpot, X, Y

# Globals and constants variables.


class TestDiffractionSpot(unittest.TestCase):
    """
    TestCase class for the module `electronmicroscopy.tem.diffraction_spot`.
    """

    def setUp(self):
        """
        Setup method.
        """

        unittest.TestCase.setUp(self)

        self.originPosition = (140.9, 153.3)
        self.positionA = (182.4, 131.9)
        self.spot = DiffractionSpot(self.positionA, self.originPosition)

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

    def testConstructor(self):
        expected_image_position = self.positionA
        expected_origin = self.originPosition

        spot = DiffractionSpot(expected_image_position, expected_origin)

        actual_image_position = spot.getImagePosition()
        self.assertAlmostEquals(expected_image_position[X], actual_image_position[X])
        self.assertAlmostEquals(expected_image_position[Y], actual_image_position[Y])

        actual_origin = self.spot.getOriginPosition()
        self.assertAlmostEquals(expected_origin[X], actual_origin[X])
        self.assertAlmostEquals(expected_origin[Y], actual_origin[Y])

        # self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_setImagePositionr(self):
        spot = DiffractionSpot()

        expected_image_position = self.positionA
        spot.setImagePosition(expected_image_position)

        actual_image_position = spot.getImagePosition()
        self.assertAlmostEquals(expected_image_position[X], actual_image_position[X])
        self.assertAlmostEquals(expected_image_position[Y], actual_image_position[Y])

        # self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_setOriginPosition(self):
        spot = DiffractionSpot()

        expected_origin = self.originPosition
        spot.setOriginPosition(self.originPosition)

        actual_origin = spot.getOriginPosition()
        self.assertAlmostEquals(expected_origin[X], actual_origin[X])
        self.assertAlmostEquals(expected_origin[Y], actual_origin[Y])

        # self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_getPosition(self):
        expected_position_a = (41.5, -21.4)
        actual_position_a = self.spot.getPosition()

        self.assertAlmostEquals(expected_position_a[X], actual_position_a[X])
        self.assertAlmostEquals(expected_position_a[Y], actual_position_a[Y])

        # self.fail("Test if the testcase is working.")
        self.assert_(True)


if __name__ == '__main__':  # pragma: no cover
    import nose
    nose.runmodule()
