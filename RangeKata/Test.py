import unittest
import main

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, main.EqualNum('[3,5)','[3,5)'))  # add assertion here

    def test_NoEqual(self):
        self.assertEqual(False, main.EqualNum('[2,9)','[3,5)'))

    def test_Contains(self):
        self.assertEqual(True, main.ContainsRN('[2,9)','[3,5]'))

    def test_NoContains(self):
        self.assertEqual(False, main.ContainsRN('[3,5)', '[2,9)'))

    def test_NoContains2(self):
        self.assertEqual(False, main.ContainsRN('[2,5)', '[7,9)'))

    def test_NoContains3(self):
        self.assertEqual(False, main.ContainsRN('[2,5)', '[3,9)'))

    def test_Contains2(self):
        self.assertEqual(True, main.ContainsRN('[3,5]', '[3,5)'))

    def test_EndPoint(self):
        self.assertEqual('2,5', main.EndPointsRN('[2,6)'))

    def test_EndPoint2(self):
        self.assertEqual('2,6', main.EndPointsRN('[2,6]'))

    def test_EndPoint3(self):
        self.assertEqual('3,5', main.EndPointsRN('(2,6)'))

    def test_EndPoint4(self):
        self.assertEqual('3,6', main.EndPointsRN('(2,6]'))


if __name__ == '__main__':
    unittest.main()
