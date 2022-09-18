import unittest

class TestStringMethods(unittest.TestCase):
    def test_split(self):
        self.assertEqual("a-b-c".split("-"), ["a", "b", "c"])
        self.assertEqual("d+e+f".split("+"), ["d", "e", "f"])

    def test_count(self):
        self.assertEqual("Nkechizim".count("i"), 2)

    def test_swapcase(self):
        self.assertEqual("Nkechizim".swapcase(), "nKECHIZIM")
        self.assertEqual("Birthday Girl".swapcase(), "bIRTHDAY gIRL")

    def test_index(self):
        self.assertEqual("Nkechizim".index("i"), 5)
        self.assertEqual("Nkechizim".index("e"), 2)


if __name__ == "__main__":
    unittest.main() 