import unittest

def divide(x, y):
    return x / a

def divide2(x, y):
    if y == 0:
        raise ZeroDivisionError
    return x / y

class DivideTestCase(unittest.TestCase):
    def test_divide(self):
        self.assertRaises(NameError, divide, 4, 5)

    def test_divide_2(self):
        with self.assertRaises(NameError):
            divide(10, 0)

    def test_divide_a(self):
        self.assertRaises(ZeroDivisionError, divide2, 4, 0)

    def test_divide_b(self):
        with self.assertRaises(ZeroDivisionError):
            divide2(10, 0)
 
if __name__ == "__main__":  
    unittest.main() 