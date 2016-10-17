#!/usr/bin/env python
import unittest
import float

class MyTest(unittest.TestCase):
    def test14(self):
        testFpo = float.fpo("0 1010 1100")
        self.assertEqual(testFpo.calculate_decimal(), 14)

    def testHalf(self):
        testFpo = float.fpo("0 00 1")
        self.assertEqual(testFpo.calculate_decimal(), 0.5)

    def testNaN(self):
        testFpo = float.fpo("0 1111 1111")
        self.assertEqual(testFpo.calculate_decimal(), "NaN")

    def testPosInf(self):
        testFpo = float.fpo("0 1111 0000")
        self.assertEqual(testFpo.calculate_decimal(), "inf")

    def testNegInf(self):
        testFpo = float.fpo("1 1111 0000")
        self.assertEqual(testFpo.calculate_decimal(), "-inf")

if __name__ == "__main__":
    unittest.main()
