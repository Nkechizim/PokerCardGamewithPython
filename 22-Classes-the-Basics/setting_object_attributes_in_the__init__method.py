class Guitar():
    def __init__(self, wood):
        self.wood = wood

acoustic = Guitar("Alder")
bass = Guitar("Mahogany")

print(acoustic.wood)
print(bass.wood)