class Height():
    def __init__(self, feet):
        self._inches = feet * 12
    
    def _get_feet(self):
        return self._inches / 12

    def _set_feet(self, feet):
        if feet >= 0:
            self._inches = feet * 12

    feet = property(_get_feet, _set_feet)

h = Height(5)

print(h.feet)

h.feet = 8
print(h.feet)
print(h.feet)

h.feet = -2
print(h.feet)