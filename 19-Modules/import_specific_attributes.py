#this method is generally discouraged due to namspace colission
from calculator import area, creator, add
from math import sqrt
#from some_other_module import creator    this will create an error

print(sqrt(6))
print(creator)
print(area(7))
