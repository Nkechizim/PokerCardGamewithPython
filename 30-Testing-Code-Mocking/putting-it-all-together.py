import unittest
from unittest.mock import MagicMock

class Actor():
    def jump_out_of_a_helicopter(self):
        return "Nope not doing it!"

    def light_on_fire(self):
        return "Heck No, where's my agent?!"

class Movie():
    def __init__(self, actor):
        self.actor = actor

    def start_filming(self):
        self.actor.jump_out_of_a_helicopter()
        self.actor.light_on_fire()

class MovieTest(unittest.TestCase):
    def test_start_filming(self):
        stunt_actor = MagicMock()
        movie = Movie(stunt_actor)

        movie.start_filming()
        stunt_actor.jump_out_of_a_helicopter.assert_called()
        stunt_actor.light_on_fire.assert_called()

if __name__ == "__main__":
    unittest.main()