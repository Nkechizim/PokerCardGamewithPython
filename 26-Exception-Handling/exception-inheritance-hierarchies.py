class Mistake(Exception):
    pass

class StupidMistake(Mistake):
    pass

class SillyMistake(Mistake):
    pass

try:
    raise StupidMistake("Extra stupid mistake")
except(StupidMistake) as e:
    print(f"Caught StupidMistake: {e}")

# try:
#     raise StupidMistake("Extra stupid mistake")
# except(SillyMistake) as e:
#     print(f"Caught StupidMistake: {e}")

try:
    raise StupidMistake("Extra stupid mistake")
except(Mistake) as e:
    print(f"Caught error: {e}")