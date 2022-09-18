from unittest.mock import Mock

mock = Mock(return_value = 30)

print(mock)

# print(mock())
# print(mock.return_value)

# mock.return_value = 25
print(mock())

stunt = Mock()
stunt.jump_building.return_value = "Oh no my leg!!"
stunt.light_fire.return_value = "It burns!!"

print(stunt.jump_building())
print(stunt.light_fire())