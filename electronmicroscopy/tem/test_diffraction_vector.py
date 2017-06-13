#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: electronmicroscopy.tem.test_diffraction_vector

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module :py:mod:`electronmicroscopy.tem.diffraction_vector`.
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
from electronmicroscopy.tem.diffraction_vector import DiffractionVector, X, Y
from electronmicroscopy.tem.diffraction_spot import DiffractionSpot

# Globals and constants variables.


class TestDiffractionVector(unittest.TestCase):
    """
    TestCase class for the module `electronmicroscopy.tem.diffraction_vector`.
    """

    def setUp(self):
        """
        Setup method.
        """

        unittest.TestCase.setUp(self)

        self.originPosition = (140.9, 153.3)
        self.positionA = (182.4, 131.9)
        self.spot = DiffractionSpot(self.positionA, self.originPosition)

        self.vector = DiffractionVector(id='A', spot=self.spot)

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
        vector = DiffractionVector(id='A', spot=self.spot)

        expected_length_A = (41.5, -21.4)
        actual_length_A = vector.getPosition()

        self.assertAlmostEquals(expected_length_A[X], actual_length_A[X])
        self.assertAlmostEquals(expected_length_A[Y], actual_length_A[Y])

        # self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_getPosition(self):
        expected_length_A = (41.5, -21.4)
        actual_length_A = self.vector.getPosition()

        self.assertAlmostEquals(expected_length_A[X], actual_length_A[X])
        self.assertAlmostEquals(expected_length_A[Y], actual_length_A[Y])

        # self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_getLength(self):
        expected_length_A = 46.692718918478072
        actual_length_A = self.vector.getLength()

        self.assertAlmostEquals(expected_length_A, actual_length_A)

        # self.fail("Test if the testcase is working.")
        self.assert_(True)


if __name__ == '__main__':  # pragma: no cover
    import nose
    nose.runmodule()
