import unittest

class TruthinessAndFalsiness(unittest.TestCase):
    def test_truthiness(self):
        #self.assertEqual(3 < 5, True)
        self.assertTrue(3 < 5)
        self.assertTrue(3)
        self.assertTrue("Hello")
        self.assertTrue(["a"])
        self.assertTrue({"b": 1})
    
    def test_falsiness(self):
        self.assertFalse(False)
        self.assertFalse("")
        self.assertFalse([])
        self.assertFalse({})
        self.assertFalse(0)



if __name__ == "__main__":
    unittest.main()