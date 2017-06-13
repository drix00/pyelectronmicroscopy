#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: electronmicroscopy.tem.test_angle_between_planes

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module :py:mod:`electronmicroscopy.tem.angle_between_planes`.
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
from electronmicroscopy.tem.angle_between_planes import angleBetweenPlanesCubic_deg

# Globals and constants variables.


class TestAngleBetweenPlanes(unittest.TestCase):
    """
    TestCase class for the module `electronmicroscopy.tem.angle_between_planes`.
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

    def test_angleBetweenPlanesCubic_deg(self):
        plane1 = (1, 0, 0)

        plane2 = (1, 0, 0)
        expected_angle_deg = 0.0
        actual_angle_deg = angleBetweenPlanesCubic_deg(plane1, plane2)
        self.assertAlmostEquals(expected_angle_deg, actual_angle_deg)

        plane2 = (0, 1, 0)
        expected_angle_deg = 90.0
        actual_angle_deg = angleBetweenPlanesCubic_deg(plane1, plane2)
        self.assertAlmostEquals(expected_angle_deg, actual_angle_deg)

        plane2 = (1, 1, 0)
        expected_angle_deg = 45.0
        actual_angle_deg = angleBetweenPlanesCubic_deg(plane1, plane2)
        self.assertAlmostEquals(expected_angle_deg, actual_angle_deg)

        plane2 = (0, 1, 1)
        expected_angle_deg = 90.0
        actual_angle_deg = angleBetweenPlanesCubic_deg(plane1, plane2)
        self.assertAlmostEquals(expected_angle_deg, actual_angle_deg)

        plane2 = (1, 1, 1)
        expected_angle_deg = 54.735610317245339
        actual_angle_deg = angleBetweenPlanesCubic_deg(plane1, plane2)
        self.assertAlmostEquals(expected_angle_deg, actual_angle_deg)

        # self.fail("Test if the testcase is working.")
        self.assert_(True)


if __name__ == '__main__':  # pragma: no cover
    import nose
    nose.runmodule()
