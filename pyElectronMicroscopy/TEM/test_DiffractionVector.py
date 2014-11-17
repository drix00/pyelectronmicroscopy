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
__svnId__ = "$Id: test_DiffractionVector.py 2378 2011-06-20 19:45:48Z hdemers $"

# Standard library modules.
import unittest
import logging

# Third party modules.

# Local modules.
import DiffractionVector
import DiffractionSpot
# Globals and constants variables.

class TestDiffractionVector(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

        self.originPosition = (140.9, 153.3)
        self.positionA = (182.4, 131.9)
        self.spot = DiffractionSpot.DiffractionSpot(self.positionA, self.originPosition)

        self.vector = DiffractionVector.DiffractionVector(id='A', spot=self.spot)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testSkeleton(self):
        #self.fail("Test if the testcase is working.")
        self.assert_(True)

    def testConstructor(self):
        vector = DiffractionVector.DiffractionVector(id='A', spot=self.spot)

        expectedPositionA = (41.5, -21.4)
        actualPositionA = vector.getPosition()

        self.assertAlmostEquals(expectedPositionA[DiffractionVector.X], actualPositionA[DiffractionVector.X])
        self.assertAlmostEquals(expectedPositionA[DiffractionVector.Y], actualPositionA[DiffractionVector.Y])

        #self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_getPosition(self):
        expectedPositionA = (41.5, -21.4)
        actualPositionA = self.vector.getPosition()

        self.assertAlmostEquals(expectedPositionA[DiffractionVector.X], actualPositionA[DiffractionVector.X])
        self.assertAlmostEquals(expectedPositionA[DiffractionVector.Y], actualPositionA[DiffractionVector.Y])

        #self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_getLength(self):
        expectedLengthA = 46.692718918478072
        actualLengthA = self.vector.getLength()

        self.assertAlmostEquals(expectedLengthA, actualLengthA)

        #self.fail("Test if the testcase is working.")
        self.assert_(True)

if __name__ == '__main__':    #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    from pyHendrixDemersTools.Testings import runTestModule
    runTestModule()