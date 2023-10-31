import unittest
import demoCode

class TestStringMethods(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(demoCode.factorial(0), 1)

    def test_postives(self):
        self.assertEqual(demoCode.factorial(1), 1)
        self.assertEqual(demoCode.factorial(2), 2)
        self.assertEqual(demoCode.factorial(5), 120)
        self.assertEqual(demoCode.factorial(6), 720)



if __name__ == '__main__':
    unittest.main()