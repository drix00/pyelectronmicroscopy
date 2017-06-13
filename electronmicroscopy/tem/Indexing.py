#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: electronmicroscopy.tem.indexing

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>


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
import math
import logging
from operator import itemgetter

# Third party modules.
import numpy as np

# Local modules.
import pyHendrixDemersTools.Files as Files

# Project modules.
import electronmicroscopy.tem.diffraction_spot as DiffractionSpot
import electronmicroscopy.tem.diffraction_vector as DiffractionVector

# Globals and constants variables.

class Indexing(object):
    def __init__(self, filepath="", centerID=0):
        self._positions = {}
        self._vectors = {}
        self._independantIdVectors = []

        self._error = 1.0
        self._errorPixel = 2.0

        self.setCenterByID(centerID)

        if filepath != "":
            self._readFile(filepath)

    def _readFile(self, filepath):
        lines = open(filepath).readlines()

        names = lines[0].split("\t")
        names[0] = "Vector"

        for line in lines[1:]:
            item = line.split("\t")
            id = str(item[0])
            position = (float(item[3]), float(item[4]))

            self._positions[id] = position

    def setCenterByID(self, centerID):
        self._centerID = str(centerID)

    def getCenterPointPosition(self):
        return self._positions[self._centerID]

    def _computeDiffractionVectors(self):
        originPosition = self.getCenterPointPosition()

        for id in self._positions:
            if id != self._centerID:
                position = self._positions[id]
                spot = DiffractionSpot.DiffractionSpot(position, originPosition)

                vector = DiffractionVector.DiffractionVector(id=id, spot=spot)
                self._vectors[id] = vector

    def _computeAngleBetweenTwoVectors_rad(self, vector1, vector2):
        denominator = np.linalg.norm(vector1)*np.linalg.norm(vector2)
        cosTheta = np.dot(vector1, vector2)/denominator
        theta = math.acos(cosTheta)

        return theta

    def _computeIndependantDiffractionVectors(self):
        if len(self._vectors) == 0:
            self._computeDiffractionVectors()

        inputIDs = self._getSortedVectorIds()
        independantIDs = []

        for id1 in self._getSortedVectorIds():
            if id1 not in independantIDs:
                if id1 in inputIDs:
                    ids = [id1]
                    inputIDs.remove(id1)
                    vector1 = self._vectors[id1].getVector()
                    for id2 in inputIDs[:]:
                        vector2 = self._vectors[id2].getVector()

                        angle = self._computeAngleBetweenTwoVectors_rad(vector1, vector2)

                        errorZero = self._error*(np.linalg.norm(vector1) + np.linalg.norm(vector2))/(np.linalg.norm(vector1*np.linalg.norm(vector2)))
                        errorPi = self._error*0.1

                        error = self._computeError(np.linalg.norm(vector1), np.linalg.norm(vector2))
                        errorZero = error
                        errorPi = error

                        logging.debug("Error for %s and %s: %0.3f %0.3f", id1, id2, errorZero, angle)

                        if 0.0 - errorZero < angle < 0.0 + errorZero:
                            ids.append(id2)
                            inputIDs.remove(id2)
                        elif math.pi - errorPi < angle < math.pi + errorPi:
                            ids.append(id2)
                            inputIDs.remove(id2)

                    independantIDs.append(ids)

        self._independantIdVectors = independantIDs

    def _computeError(self, length1, length2):
        error = self._errorPixel/length1 + self._errorPixel/length2

        return error

    def _getSortedVectorIds(self):
        if self._vectors == {}:
            self._computeDiffractionVectors()

        keyItems = sorted(self._vectors.items(), key=itemgetter(1))

        ids = [keyItem[0] for keyItem in keyItems]

        return ids

    def computeRatioMethod(self, referenceId=None):
        self._computeIndependantDiffractionVectors()

        ratios = {}

        ids = [item[0] for item in self._independantIdVectors]

        vectors = self._vectors
        if referenceId == None:
            referenceId = ids[0]

        referenceLength = vectors[referenceId].getLength()

        for id in ids:
            length = vectors[id].getLength()

            ratio = length/referenceLength
            ratios[id] = ratio

        for id in ids:
            length = vectors[id].getLength()
            ratio = ratios[id]
            ratio2 = ratio**2
            line = "%s\t%0.2f\t%0.2f\t%0.2f" % (id, length, ratio, ratio2)

            for N in range(1, 10):
                line += "\t%0.3f" % (N*ratio2)

            print(line)

def runHomework5q1a():
        configurationFilepath = Files.getCurrentModulePath(__file__, "../pyElectronMicroscope.cfg")
        filepath = Files.getWorksPath(configurationFilepath, "cnse/Courses/CNSE 670 (tem)/Homework/Homework05/images/q1a_c16.txt")
        indexing = Indexing(filepath, centerID=16)

        indexing.computeRatioMethod('15')

def runHomework5q1b():
        configurationFilepath = Files.getCurrentModulePath(__file__, "../pyElectronMicroscope.cfg")
        filepath = Files.getWorksPath(configurationFilepath, "cnse/Courses/CNSE 670 (tem)/Homework/Homework05/images/q1b_c16.txt")
        indexing = Indexing(filepath, centerID=16)

        indexing.computeRatioMethod('14')

def runHomework5q1c():
        configurationFilepath = Files.getCurrentModulePath(__file__, "../pyElectronMicroscope.cfg")
        filepath = Files.getWorksPath(configurationFilepath, "cnse/Courses/CNSE 670 (tem)/Homework/Homework05/images/q1c_c10.txt")
        indexing = Indexing(filepath, centerID=10)

        indexing.computeRatioMethod('11')

def runHomework5q1d():
        configurationFilepath = Files.getCurrentModulePath(__file__, "../pyElectronMicroscope.cfg")
        filepath = Files.getWorksPath(configurationFilepath, "cnse/Courses/CNSE 670 (tem)/Homework/Homework05/images/q1d_c11.txt")
        indexing = Indexing(filepath, centerID=11)

        indexing.computeRatioMethod()

        for ids in indexing._independantIdVectors:
            for id in ids:
                print("%.1f" % (indexing._vectors[id].getLength()))

def run():
    #runHomework5q1a()
    #runHomework5q1b()
    #runHomework5q1c()
    runHomework5q1d()

if __name__ == '__main__':    #pragma: no cover
    import pyHendrixDemersTools.Runner as Runner
    Runner.Runner().run(runFunction=run)
