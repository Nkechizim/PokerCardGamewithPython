import unittest

class IdentityTest(unittest.TestCase):
    def test_identicality(self):
        a = [1, 2, 3]
        b = a
        c = [1, 2, 3]

        self.assertEqual(a, b)
        self.assertEqual(a, c)
        self.assertEqual(b, c)

        self.assertIs(a, b, "The two object are not the same")
        self.assertIsNot(a, c, "The two object are the same")
        self.assertIsNot(b, c)


if __name__ == "__main__":
    unittest.main()