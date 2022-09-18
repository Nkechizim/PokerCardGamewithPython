import unittest

class ObjectTypeTest(unittest.TestCase):
    def test_is_instance(self):
        self.assertIsInstance(1, int)
        self.assertIsInstance(8.765, float)
        self.assertIsInstance([], list)
        self.assertIsInstance({}, dict)

    def test_not_is_instance(self):
        self.assertNotIsInstance(1, float)
        self.assertNotIsInstance(8.765, int)
        self.assertNotIsInstance([], set)
        self.assertNotIsInstance({}, list)
   
 
if __name__ == "__main__":  
    unittest.main() 

# import unittest

# my_numbers = [1, 10, 15, 6, 20]
# def add_numbers():
#     total = 0
#     for number in numbers:
#         total += number
#     return total

# class NameErrorTest(unittest.TestCase):
#     def test_NameError(self):
#         with self.assertRaises(NameError):
#             add_numbers()

# if __name__ == "__main__":
#     unittest.main()