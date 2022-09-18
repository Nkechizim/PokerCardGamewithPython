import unittest

def multiply(a, b):
    return a * b

class MultiplyTestCase(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(3, 5), 15)

if __name__ == "__main__":
    unittest.main()