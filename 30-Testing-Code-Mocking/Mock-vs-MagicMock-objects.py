from unittest.mock import Mock, MagicMock

#the mafic mock supports magic (dunder) methods while the plain mock does not

plain_mock = Mock()
magic_mock = MagicMock()
print(plain_mock)
print(magic_mock)

#print(len(plain_mock))
print(len(magic_mock))

#print(plain_mock[3])
print(magic_mock[3])
print(magic_mock[50])
print(magic_mock["Hey"])

magic_mock.__len__.return_value = 50
print(len(magic_mock))

if magic_mock:
    print("Hello")

magic_mock.__bool__.return_value = False

if magic_mock:
    print("Bye")

magic_mock.__getitem__.return_value = 250
print(magic_mock[3])
print(magic_mock[50])
print(magic_mock["Hey"])