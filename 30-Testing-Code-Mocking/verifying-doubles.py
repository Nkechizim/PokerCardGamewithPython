from unittest.mock import MagicMock

class BurritoBowl():
    restaurant_name = "Nk's Burritos"

    @classmethod
    def steak_special(cls):
        return cls("Steak", "White", 1)

    def __init__(self, protein, rice, guacamole_portions):
        self.protein = protein
        self.rice = rice
        self.guacamole_portions = guacamole_portions

    def add_guac(self):
        self.guacamole_portions += 1

# lunch = BurritoBowl.steak_special()
# print(lunch.protein)
# lunch.add_guac()
# print(lunch.guacamole_portions)

class_mock = MagicMock(spec = BurritoBowl)
print(class_mock.restaurant_name)
print(class_mock.steak_special())
print(class_mock.add_guac())
# print(class_mock.add_protein())
# print(class_mock.carbohydrate)

#spec_set prohibits adding new attributes on the magic_mock, but the spec allows adding new attributes
instance_mock = MagicMock(spec_set = BurritoBowl.steak_special())
print(instance_mock.protein)
print(instance_mock.rice)
print(instance_mock.add_guac())
print(instance_mock.restaurant_name)
# print(class_mock.add_protein())

# class_mock.beans = "Brown"
# print(class_mock.beans)