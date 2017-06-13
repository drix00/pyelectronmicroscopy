#!/usr/bin/env python
""" """

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2011 Hendrix Demers"
__license__ = ""

# Subversion informations for the file.
__svnRevision__ = "$Revision$"
__svnDate__ = "$Date$"
__svnId__ = "$Id$"

# Standard library modules.
import unittest
import logging

# Third party modules.

# Local modules.

# Project modules
import electronmicroscopy.range.kanaya_okayama_models as KanayaOkayamaModels

# Globals and constants variables.

class TestKanayaOkayamaModels(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testSkeleton(self):
        #self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_range_nm(self):
        energies_eV = [5.0e3,  10.0e3, 20.0e3, 30.0e3]
        rangesRef_nm = self._getRangesRefOriginal_nm()

        atomicNumbers = [6, 79]
        for atomicNumber in atomicNumbers:
            for energy_eV in energies_eV:
                range_nm = round(KanayaOkayamaModels.range_nm(atomicNumber, energy_eV))
                rangeRef_nm = rangesRef_nm[atomicNumber][energy_eV]
                self.assertEqual(rangeRef_nm, range_nm)

        #self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_rangeOriginalPaper_nm(self):
        energies_eV = [5.0e3,  10.0e3, 20.0e3, 30.0e3]
        rangesRef_nm = self._getRangesRefOriginal_nm()

        atomicNumbers = [6, 79]
        for atomicNumber in atomicNumbers:
            for energy_eV in energies_eV:
                range_nm = round(KanayaOkayamaModels._range_original_paper_nm(atomicNumber, energy_eV))
                rangeRef_nm = rangesRef_nm[atomicNumber][energy_eV]
                self.assertEqual(rangeRef_nm, range_nm)

        #self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_rangeGolsteinBook_nm(self):
        energies_eV = [5.0e3,  10.0e3, 20.0e3, 30.0e3]
        rangesRef_nm = self._getRangesRef_nm()

        atomicNumbers = [6, 79]
        for atomicNumber in atomicNumbers:
            for energy_eV in energies_eV:
                range_nm = round(KanayaOkayamaModels._range_goldstein_book_nm(atomicNumber, energy_eV))
                rangeRef_nm = rangesRef_nm[atomicNumber][energy_eV]
                self.assertEqual(rangeRef_nm, range_nm)

        #self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_rangeRelativistic_nm(self):
        energies_eV = [5.0e3,  10.0e3, 20.0e3, 30.0e3]
        rangesRef_nm = self._getRangesRefRelativistic_nm()

        atomicNumbers = [6, 79]
        for atomicNumber in atomicNumbers:
            for energy_eV in energies_eV:
                range_nm = round(KanayaOkayamaModels.range_relativistic_nm(atomicNumber, energy_eV))
                rangeRef_nm = rangesRef_nm[atomicNumber][energy_eV]
                self.assertEqual(rangeRef_nm, range_nm)

        #self.fail("Test if the testcase is working.")
        self.assert_(True)

    def _getRangesRef_nm(self):
        rangesRef_nm = {}

        rangesRef_nm[6] = {5.0e3: 377, 10.0e3: 1201, 20.0e3: 3823, 30.0e3: 7524}
        rangesRef_nm[79] = {5.0e3: 85, 10.0e3: 270, 20.0e3: 858, 30.0e3: 1689}

        return rangesRef_nm

    def _getRangesRefOriginal_nm(self):
        rangesRef_nm = {}

        rangesRef_nm[6] = {5.0e3: 376, 10.0e3: 1195, 20.0e3: 3793, 30.0e3: 7456}
        rangesRef_nm[79] = {5.0e3: 85, 10.0e3: 269, 20.0e3: 854, 30.0e3: 1679}

        return rangesRef_nm

    def _getRangesRefRelativistic_nm(self):
        rangesRef_nm = {}

        rangesRef_nm[6] = {5.0e3: 374, 10.0e3: 1183, 20.0e3: 3721, 30.0e3: 7249}
        rangesRef_nm[79] = {5.0e3: 84, 10.0e3: 266, 20.0e3: 838, 30.0e3: 1632}

        return rangesRef_nm

if __name__ == '__main__':  #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    from pyHendrixDemersTools.Testings import runTestModule
    runTestModule()
