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
__svnId__ = "$Id: test_AngleBetweenPlanes.py 2378 2011-06-20 19:45:48Z hdemers $"

# Standard library modules.
import unittest
import logging

# Third party modules.

# Local modules.
import electronmicroscopy.tem.AngleBetweenPlanes as AngleBetweenPlanes

# Globals and constants variables.

class TestAngleBetweenPlanes(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testSkeleton(self):
        #self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_angleBetweenPlanesCubic_deg(self):
        plane1 = (1,0,0)

        plane2 = (1,0,0)
        expectedAngle_deg = 0.0
        actualAngle_deg = AngleBetweenPlanes.angleBetweenPlanesCubic_deg(plane1, plane2)
        self.assertAlmostEquals(expectedAngle_deg, actualAngle_deg)

        plane2 = (0,1,0)
        expectedAngle_deg = 90.0
        actualAngle_deg = AngleBetweenPlanes.angleBetweenPlanesCubic_deg(plane1, plane2)
        self.assertAlmostEquals(expectedAngle_deg, actualAngle_deg)

        plane2 = (1,1,0)
        expectedAngle_deg = 45.0
        actualAngle_deg = AngleBetweenPlanes.angleBetweenPlanesCubic_deg(plane1, plane2)
        self.assertAlmostEquals(expectedAngle_deg, actualAngle_deg)

        plane2 = (0,1,1)
        expectedAngle_deg = 90.0
        actualAngle_deg = AngleBetweenPlanes.angleBetweenPlanesCubic_deg(plane1, plane2)
        self.assertAlmostEquals(expectedAngle_deg, actualAngle_deg)

        plane2 = (1,1,1)
        expectedAngle_deg = 54.735610317245339
        actualAngle_deg = AngleBetweenPlanes.angleBetweenPlanesCubic_deg(plane1, plane2)
        self.assertAlmostEquals(expectedAngle_deg, actualAngle_deg)

        #self.fail("Test if the testcase is working.")
        self.assert_(True)

if __name__ == '__main__':    #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    from pyHendrixDemersTools.Testings import runTestModule
    runTestModule()