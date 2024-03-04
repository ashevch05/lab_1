import unittest
import test1

class MyTest(unittest.TestCase):

    def test_gcd(self):

        result = test1.gcd(-12,0)
        self.assertEqual(result, -12)

        result = test1.gcd(10,5)
        self.assertEqual(result, 5)

        result = test1.gcd(18,34)
        self.assertEqual(result, 2)

    def test_lcm(self):

        result = test1.lcm(12, 18)
        self.assertEqual(result, 36)

        result = test1.lcm(10, 5)
        self.assertEqual(result, 10)

        result = test1.lcm(18, 34)
        self.assertEqual(result, 306)

    if __name__ == '__main__':
        unittest.main()

