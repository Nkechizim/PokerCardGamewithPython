#A fixture: is a piece of code that is used to construct and configure a system under test
import unittest

class Address():
    def __init__(self, city, state):
        self.state = state
        self.city = city

class Owner():
    def __init__(self, name, age):
        self.age = age
        self.name = name

class Restaurant():
    def __init__(self, address, owner):
        self.address = address
        self.owner = owner

    @property
    def owner_age(self):
        return self.owner.age

    def summary(self):
        return f"This restaurant is owned by {self.owner.name} and is located in {self.address.city}"

class TestRestaurant(unittest.TestCase):
    def setUp(self):
        print("This will run before each test") 
        address = Address("V.I", "Lagos")
        owner = Owner("Nkechi", 21)
        self.restaurant = Restaurant(address, owner)

    def tearDown(self):
        print("This will run after each test")

    def test_owner_age(self):
        self.assertIsInstance(self.restaurant.owner_age, int)
        self.assertEqual(self.restaurant.owner_age, 21)

    def test_summary(self):
        self.assertIsInstance(self.restaurant.summary(), str)
        self.assertEqual(self.restaurant.summary(), 
        "This restaurant is owned by Nkechi and is located in V.I")
  
if __name__ == "__main__":  
    unittest.main() 