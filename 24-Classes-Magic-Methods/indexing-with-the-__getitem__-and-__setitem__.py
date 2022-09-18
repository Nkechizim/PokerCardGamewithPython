# pillows = {
#     "soft": 79.99,
#     "hard": 99.99
# }

# print(pillows["soft"])
# print(pillows.__getitem__("soft"))

class CrayonBox():
    def __init__(self):
        self.crayons = []
    def add(self, crayon):
        self.crayons.append(crayon)
    def __getitem__(self, index):
        return self.crayons[index]
    def __setitem__(self, index, value):
        self.crayons[index] = value

cb = CrayonBox()
cb.add("Blue")
cb.add("Green")

print(cb[1])
print(cb[0])

cb[0] = "Red"
print(cb[0])

for crayon in cb:
    print(crayon)