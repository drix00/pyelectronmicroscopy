#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: electronmicroscopy.tem.test_indexing

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module :py:mod:`electronmicroscopy.tem.indexing`.
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
import logging
import math
import os.path

# Third party modules.
import numpy as np
from nose import SkipTest

# Local modules.
import pyHendrixDemersTools.Files as Files

# Project modules.
from electronmicroscopy.tem.indexing import Indexing

# Globals and constants variables.


class TestIndexing(unittest.TestCase):
    """
    TestCase class for the module `electronmicroscopy.tem.indexing`.
    """

    def setUp(self):
        """
        Setup method.
        """

        unittest.TestCase.setUp(self)

        self.filepath = Files.getCurrentModulePath(__file__, "../../testData/q1a_c16.txt")
        logging.debug(self.filepath)
        if not os.path.isfile(self.filepath):
            raise SkipTest

        self.indexing = Indexing(self.filepath, centerID=16)

        self.numberPoints = 22

        # Remove the origin.
        self.numberDiffractionVectors = self.numberPoints - 1
        self.numberUniqueDiffractionVectors = 11

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

    def test_readFile(self):
        indexing = Indexing()
        indexing._readFile(self.filepath)

        points = indexing._positions

        self.assertEquals(self.numberPoints, len(points))

        # self.fail("Test if the testcase is working.")
        self.assert_(True)

    def testConstructor(self):
        points = self.indexing._positions
        self.assertEquals(self.numberPoints, len(points))

        # self.fail("Test if the testcase is working.")
        self.assert_(True)

    def testCenterPoint(self):
        center_id = 16

        expected_center_position = (141.4, 153.9)

        self.indexing.setCenterByID(center_id)
        actual_center_position = self.indexing.getCenterPointPosition()

        self.assertAlmostEquals(expected_center_position[0], actual_center_position[0])
        self.assertAlmostEquals(expected_center_position[1], actual_center_position[1])

        # self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_computeDiffractionVectors(self):
        vectors = self.indexing._vectors
        self.assertEquals(0, len(vectors))

        self.indexing._computeDiffractionVectors()

        vectors = self.indexing._vectors
        self.assertEquals(self.numberDiffractionVectors, len(vectors))

        # self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_computeIndependantDiffractionVectors(self):
        vectors = self.indexing._independantIdVectors
        self.assertEquals(0, len(vectors))

        self.indexing._computeIndependantDiffractionVectors()

        vectors = self.indexing._independantIdVectors
        self.assertEquals(self.numberUniqueDiffractionVectors, len(vectors))

        expected_ids = []
        expected_ids.append(['21', '12', '7', '3'])
        expected_ids.append(['15', '18', '13', '20'])
        expected_ids.append(['19', '14', '11'])
        expected_ids.append(['22', '9', '4'])
        expected_ids.append(['8'])
        expected_ids.append(['5'])
        expected_ids.append(['10'])
        expected_ids.append(['17'])
        expected_ids.append(['1'])
        expected_ids.append(['6'])
        expected_ids.append(['2'])

        for ids1, ids2 in zip(expected_ids, vectors):
            self.assertEquals(ids1, ids2)

        # self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_sortVectorLength(self):
        expected_ids = ['21', '15', '18', '12', '19', '22', '9', '14', '13', '7', '20', '8', '5', '10', '17', '4',
                        '11', '3', '1', '6', '2']

        actual_ids = self.indexing._getSortedVectorIds()
        self.assertEquals(self.numberDiffractionVectors, len(actual_ids))

        self.assertEquals(expected_ids, actual_ids)

        # self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_computeRatioMethod(self):
        self.indexing.computeRatioMethod()

        # self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_computeDiffAngle(self):
        v1 = np.array((1.0, 0.0, 0.0))
        v2 = np.array((0.0, 1.0, 0.0))
        v3 = np.array((1.0, 1.0, 0.0))
        v4 = np.array((-1.0, 0.0, 0.0))

        diff_angle = self.indexing._computeAngleBetweenTwoVectors_rad(v1, v1)
        self.assertAlmostEquals(0.0, diff_angle)

        diff_angle = self.indexing._computeAngleBetweenTwoVectors_rad(v1, v2)
        self.assertAlmostEquals(math.pi/2.0, diff_angle)

        diff_angle = self.indexing._computeAngleBetweenTwoVectors_rad(v2, v1)
        self.assertAlmostEquals(math.pi/2.0, diff_angle)

        diff_angle = self.indexing._computeAngleBetweenTwoVectors_rad(v1, v3)
        self.assertAlmostEquals(math.pi/4.0, diff_angle)

        diff_angle = self.indexing._computeAngleBetweenTwoVectors_rad(v2, v3)
        self.assertAlmostEquals(math.pi/4.0, diff_angle)

        diff_angle = self.indexing._computeAngleBetweenTwoVectors_rad(v1, v4)
        self.assertAlmostEquals(math.pi, diff_angle)

        # self.fail("Test if the testcase is working.")
        self.assert_(True)


if __name__ == '__main__':  # pragma: no cover
    import nose
    nose.runmodule()
