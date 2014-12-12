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
__svnId__ = "$Id: test_DiffractionSpot.py 2378 2011-06-20 19:45:48Z hdemers $"

# Standard library modules.
import unittest
import logging

# Third party modules.

# Local modules.
import pyElectronMicroscopy.TEM.DiffractionSpot as DiffractionSpot

# Globals and constants variables.

class TestDiffractionSpot(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

        self.originPosition = (140.9, 153.3)
        self.positionA = (182.4, 131.9)
        self.spot = DiffractionSpot.DiffractionSpot(self.positionA, self.originPosition)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testSkeleton(self):
        #self.fail("Test if the testcase is working.")
        self.assert_(True)

    def testConstructor(self):
        expectedImagePosition = self.positionA
        expectedOrigin = self.originPosition

        spot = DiffractionSpot.DiffractionSpot(expectedImagePosition, expectedOrigin)

        actualImagePosition = spot.getImagePosition()
        self.assertAlmostEquals(expectedImagePosition[DiffractionSpot.X], actualImagePosition[DiffractionSpot.X])
        self.assertAlmostEquals(expectedImagePosition[DiffractionSpot.Y], actualImagePosition[DiffractionSpot.Y])

        actualOrigin = self.spot.getOriginPosition()
        self.assertAlmostEquals(expectedOrigin[DiffractionSpot.X], actualOrigin[DiffractionSpot.X])
        self.assertAlmostEquals(expectedOrigin[DiffractionSpot.Y], actualOrigin[DiffractionSpot.Y])

        #self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_setImagePositionr(self):
        spot = DiffractionSpot.DiffractionSpot()

        expectedImagePosition = self.positionA
        spot.setImagePosition(expectedImagePosition)

        actualImagePosition = spot.getImagePosition()
        self.assertAlmostEquals(expectedImagePosition[DiffractionSpot.X], actualImagePosition[DiffractionSpot.X])
        self.assertAlmostEquals(expectedImagePosition[DiffractionSpot.Y], actualImagePosition[DiffractionSpot.Y])

        #self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_setOriginPosition(self):
        spot = DiffractionSpot.DiffractionSpot()

        expectedOrigin = self.originPosition
        spot.setOriginPosition(self.originPosition)

        actualOrigin = spot.getOriginPosition()
        self.assertAlmostEquals(expectedOrigin[DiffractionSpot.X], actualOrigin[DiffractionSpot.X])
        self.assertAlmostEquals(expectedOrigin[DiffractionSpot.Y], actualOrigin[DiffractionSpot.Y])

        #self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_getPosition(self):
        expectedPositionA = (41.5, -21.4)
        actualPositionA = self.spot.getPosition()

        self.assertAlmostEquals(expectedPositionA[DiffractionSpot.X], actualPositionA[DiffractionSpot.X])
        self.assertAlmostEquals(expectedPositionA[DiffractionSpot.Y], actualPositionA[DiffractionSpot.Y])

        #self.fail("Test if the testcase is working.")
        self.assert_(True)

if __name__ == '__main__':    #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    from pyHendrixDemersTools.Testings import runTestModule
    runTestModule()