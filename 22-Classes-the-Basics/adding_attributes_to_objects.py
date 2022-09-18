class Guitar():
    def __init__(self):
        print(f"A new Guitar is being created {self}")

acoustic = Guitar()
bass = Guitar()

acoustic.wood = "Mahogany"
acoustic.strings = 6
acoustic.year = 1990

bass.nickname = "Ocean"

print(acoustic.wood)
print(bass.nickname)