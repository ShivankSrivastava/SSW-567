"""
Author: Shivank Srivastava
CWID: 20006832
Date: 21st Sept 2022
"""
import unittest

from Triangle import classifyTriangle


class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testCase1(self):
        self.assertEqual(classifyTriangle(2, 2, 2), 'Equilateral')

    def testCase2(self):
        self.assertEqual(classifyTriangle(15, 15, 15), 'Equilateral')

    def testCase3(self):
        self.assertEqual(classifyTriangle(5, 5, 3), 'Isosceles')

    def testCase4(self):
        self.assertEqual(classifyTriangle(4, 6, 6), 'Isosceles')

    def testCase5(self):
        self.assertEqual(classifyTriangle(10, 11, 12), 'Scalene')

    def testCase6(self):
        self.assertEqual(classifyTriangle(4, 2, 3), 'Scalene')

    def testCase7(self):
        self.assertEqual(classifyTriangle(-1, -1, -1), 'InvalidInput')

    def testCase8(self):
        self.assertEqual(classifyTriangle("200", "0", "0"), 'InvalidInput')

    def testCase9(self):
        self.assertEqual(classifyTriangle(5, 1, 1), 'NotATriangle')

    def testCase10(self):
        self.assertEqual(classifyTriangle(1, 5, 1), 'NotATriangle')

    def testCase11(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right')

    def testCase12(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
