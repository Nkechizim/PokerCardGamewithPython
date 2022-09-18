import unittest

class InclusionTest(unittest.TestCase):
    def test_inclusion(self):
        # self.assertTrue("k" in "king")
        self.assertIn("k", "king")
        self.assertIn(3, [4, 5, 3])
        self.assertIn(3, (4, 5, 3))
        self.assertIn("a", {"a": 4, "b": 5, "c": 3})
        self.assertIn("a", {"a": 4, "b": 5, "c": 3}.keys())
        self.assertIn(4, {"a": 4, "b": 5, "c": 3}.values())
        self.assertIn(55, range(50, 59))

    def test_non_inclusion(self):
        self.assertNotIn("w", "king")
        self.assertNotIn(9, [4, 5, 3])
        self.assertNotIn(7, (4, 5, 3))
        self.assertNotIn("j", {"a": 4, "b": 5, "c": 3})
        self.assertNotIn("p", {"a": 4, "b": 5, "c": 3}.keys())
        self.assertNotIn(9, {"a": 4, "b": 5, "c": 3}.values())
        self.assertNotIn(75, range(50, 59))
   
 
if __name__ == "__main__":  
    unittest.main() 