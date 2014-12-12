#!/usr/bin/env python
""" """

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2009 Hendrix Demers"
__license__ = ""

# Subversion informations for the file.
__svnRevision__ = "$Revision: 2378 $"
__svnDate__ = "$Date: 2011-06-20 15:45:48 -0400 (Mon, 20 Jun 2011) $"
__svnId__ = "$Id: test_Indexing.py 2378 2011-06-20 19:45:48Z hdemers $"

# Standard library modules.
import unittest
import logging
import math

# Third party modules.
import numpy as np

# Local modules.
import pyElectronMicroscopy.TEM.Indexing as Indexing
import pyHendrixDemersTools.Files as Files

# Globals and constants variables.

class TestIndexing(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

        self.filepath = Files.getCurrentModulePath(__file__, "../../testData/q1a_c16.txt")
        logging.debug(self.filepath)
        self.indexing = Indexing.Indexing(self.filepath, centerID=16)

        self.numberPoints = 22

        # Remove the origin.
        self.numberDiffractionVectors = self.numberPoints - 1
        self.numberUniqueDiffractionVectors = 11

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testSkeleton(self):
        #self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_readFile(self):
        indexing = Indexing.Indexing()
        indexing._readFile(self.filepath)

        points = indexing._positions

        self.assertEquals(self.numberPoints, len(points))

        #self.fail("Test if the testcase is working.")
        self.assert_(True)

    def testConstructor(self):
        points = self.indexing._positions
        self.assertEquals(self.numberPoints, len(points))

        #self.fail("Test if the testcase is working.")
        self.assert_(True)

    def testCenterPoint(self):
        centerID = 16

        expectedCenterPosition = (141.4, 153.9)

        self.indexing.setCenterByID(centerID)
        actualCenterPosition = self.indexing.getCenterPointPosition()

        self.assertAlmostEquals(expectedCenterPosition[0], actualCenterPosition[0])
        self.assertAlmostEquals(expectedCenterPosition[1], actualCenterPosition[1])

        #self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_computeDiffractionVectors(self):
        vectors = self.indexing._vectors
        self.assertEquals(0, len(vectors))

        self.indexing._computeDiffractionVectors()

        vectors = self.indexing._vectors
        self.assertEquals(self.numberDiffractionVectors, len(vectors))

        #self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_computeIndependantDiffractionVectors(self):
        vectors = self.indexing._independantIdVectors
        self.assertEquals(0, len(vectors))

        self.indexing._computeIndependantDiffractionVectors()

        vectors = self.indexing._independantIdVectors
        self.assertEquals(self.numberUniqueDiffractionVectors, len(vectors))

        expectedIds = []
        expectedIds.append(['21', '12', '7', '3'])
        expectedIds.append(['15', '18', '13', '20'])
        expectedIds.append(['19', '14', '11'])
        expectedIds.append(['22', '9', '4'])
        expectedIds.append(['8'])
        expectedIds.append(['5'])
        expectedIds.append(['10'])
        expectedIds.append(['17'])
        expectedIds.append(['1'])
        expectedIds.append(['6'])
        expectedIds.append(['2'])

        for ids1, ids2 in zip(expectedIds, vectors):
            self.assertEquals(ids1, ids2)

        #self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_sortVectorLength(self):
        expectedIds = ['21', '15', '18', '12', '19', '22', '9', '14', '13', '7', '20', '8', '5', '10', '17', '4', '11', '3', '1', '6', '2']

        actualIds = self.indexing._getSortedVectorIds()
        self.assertEquals(self.numberDiffractionVectors, len(actualIds))

        self.assertEquals(expectedIds, actualIds)

        #self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_computeRatioMethod(self):
        self.indexing.computeRatioMethod()

        #self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_computeDiffAngle(self):
        v1 = np.array((1.0, 0.0, 0.0))
        v2 = np.array((0.0, 1.0, 0.0))
        v3 = np.array((1.0, 1.0, 0.0))
        v4 = np.array((-1.0, 0.0, 0.0))

        diffAngle = self.indexing._computeAngleBetweenTwoVectors_rad(v1, v1)
        self.assertAlmostEquals(0.0, diffAngle)

        diffAngle = self.indexing._computeAngleBetweenTwoVectors_rad(v1, v2)
        self.assertAlmostEquals(math.pi/2.0, diffAngle)

        diffAngle = self.indexing._computeAngleBetweenTwoVectors_rad(v2, v1)
        self.assertAlmostEquals(math.pi/2.0, diffAngle)

        diffAngle = self.indexing._computeAngleBetweenTwoVectors_rad(v1, v3)
        self.assertAlmostEquals(math.pi/4.0, diffAngle)

        diffAngle = self.indexing._computeAngleBetweenTwoVectors_rad(v2, v3)
        self.assertAlmostEquals(math.pi/4.0, diffAngle)

        diffAngle = self.indexing._computeAngleBetweenTwoVectors_rad(v1, v4)
        self.assertAlmostEquals(math.pi, diffAngle)

        #self.fail("Test if the testcase is working.")
        self.assert_(True)

if __name__ == '__main__':    #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    from pyHendrixDemersTools.Testings import runTestModule
    runTestModule()
