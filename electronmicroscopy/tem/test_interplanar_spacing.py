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
__svnId__ = "$Id: test_interplanar_spacing.py 2378 2011-06-20 19:45:48Z hdemers $"

# Standard library modules.
import unittest
import logging

# Third party modules.

# Local modules.
import electronmicroscopy.tem.interplanar_spacing as InterplanarSpacing

# Globals and constants variables.

class TestInterplanarSpacing(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def getTestPlanes(self):
        planes = []
        planes.append((1,0,0))
        planes.append((0,1,0))
        planes.append((0,0,1))
        planes.append((-1,0,0))
        planes.append((0,-1,0))
        planes.append((0,0,-1))

        planes.append((3,2,1))
        planes.append((3,1,2))
        planes.append((1,3,2))
        planes.append((1,2,3))
        planes.append((2,3,1))
        planes.append((2,1,3))

        planes.append((-3,2,1))
        planes.append((-3,-2,1))
        planes.append((-3,-2,-1))
        planes.append((3,-2,1))
        planes.append((3,-2,-1))
        planes.append((3,2,-1))

        return planes

    def getExpectedDCubic(self):
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

    def getExpectedDTetragonal(self):
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

    def getExpectedDOrthorhombic(self):
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

    def getExpectedDHexagonal(self):
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

    def getExpectedDRhombohedral(self):
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

    def getExpectedDMonoclinic(self):
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

    def getExpectedDTriclinic(self):
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

    def testSkeleton(self):
        #self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_interplanarSpacingCubic(self):
        a = 2.5

        planes = self.getTestPlanes()
        expectedDs = self.getExpectedDCubic()

        for expectedD,plane in zip(expectedDs, planes):
            actualD = InterplanarSpacing.interplanarSpacingCubic(plane, a)

            self.assertAlmostEquals(expectedD, actualD)

        self.assertEquals(len(expectedDs), len(planes))

        #self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_interplanarSpacingTetragonal(self):
        a = 2.5
        c = 3.6

        planes = self.getTestPlanes()
        expectedDs = self.getExpectedDTetragonal()

        for expectedD,plane in zip(expectedDs, planes):
            actualD = InterplanarSpacing.interplanarSpacingTetragonal(plane, a, c)

            self.assertAlmostEquals(expectedD, actualD)

        self.assertEquals(len(expectedDs), len(planes))

        #self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_interplanarSpacingOrthorhombic(self):
        a = 2.5
        b = 1.2
        c = 3.6

        planes = self.getTestPlanes()
        expectedDs = self.getExpectedDOrthorhombic()

        for expectedD,plane in zip(expectedDs, planes):
            actualD = InterplanarSpacing.interplanarSpacingOrthorhombic(plane, a, b, c)

            self.assertAlmostEquals(expectedD, actualD)

        self.assertEquals(len(expectedDs), len(planes))

        #self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_interplanarSpacingHexagonal(self):
        a = 2.5
        c = 3.6

        planes = self.getTestPlanes()
        expectedDs = self.getExpectedDHexagonal()

        for expectedD,plane in zip(expectedDs, planes):
            actualD = InterplanarSpacing.interplanarSpacingHexagonal(plane, a, c)

            self.assertAlmostEquals(expectedD, actualD)

        self.assertEquals(len(expectedDs), len(planes))

        #self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_interplanarSpacingRhombohedral(self):
        a = 2.5
        alpha_deg = 39.56

        planes = self.getTestPlanes()
        expectedDs = self.getExpectedDRhombohedral()

        for expectedD,plane in zip(expectedDs, planes):
            actualD = InterplanarSpacing.interplanarSpacingRhombohedral(plane, a, alpha_deg)

            self.assertAlmostEquals(expectedD, actualD)

        self.assertEquals(len(expectedDs), len(planes))

        #self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_interplanarSpacingMonoclinic(self):
        a = 2.5
        b = 1.2
        c = 3.6
        beta_deg = 86.56

        planes = self.getTestPlanes()
        expectedDs = self.getExpectedDMonoclinic()

        for expectedD,plane in zip(expectedDs, planes):
            actualD = InterplanarSpacing.interplanarSpacingMonoclinic(plane, a, b, c, beta_deg)

            self.assertAlmostEquals(expectedD, actualD)

        self.assertEquals(len(expectedDs), len(planes))

        #self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_interplanarSpacingTriclinic(self):
        a = 2.5
        b = 1.2
        c = 3.6
        alpha_deg = 39.56
        beta_deg = 86.56
        gamma_deg = 86.56

        planes = self.getTestPlanes()
        expectedDs = self.getExpectedDTriclinic()

        for expectedD,plane in zip(expectedDs, planes):
            actualD = InterplanarSpacing.interplanarSpacingTriclinic(plane, a, b, c, alpha_deg, beta_deg, gamma_deg)

            self.assertAlmostEquals(expectedD, actualD)

        self.assertEquals(len(expectedDs), len(planes))

        #self.fail("Test if the testcase is working.")
        self.assert_(True)

if __name__ == '__main__':    #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    from pyHendrixDemersTools.Testings import runTestModule
    runTestModule()