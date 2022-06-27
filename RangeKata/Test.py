import unittest
import main

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, main.EqualNum('[3,5)','[3,5)'))  # add assertion here

    def test_NoEqual(self):
        self.assertEqual(False, main.EqualNum('[2,9)','[3,5)'))


if __name__ == '__main__':
    unittest.main()
