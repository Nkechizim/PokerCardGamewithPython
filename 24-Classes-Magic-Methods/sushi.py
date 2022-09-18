"""
A module related to the joy of sushi.
No fishy code here!!
"""

def fish():
    """
    Determines if fish is a good meal choice.
    Always returns True because it always is. 
    """
    return True

class Salmon():
    """
    Blueprint for creating a salmon
    """
    def __init__(self):
        self.tastiness = 10

    def bake(self):
        """
        Bake the fish in an oven
        """
        self.tastiness += 1