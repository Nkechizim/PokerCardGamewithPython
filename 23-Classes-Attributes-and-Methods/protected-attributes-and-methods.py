class Smartphone():
    def __init__(self):
        self._company = "Apple"
        self._firmware = 10.0
    def update_firmware(self):
        self._firmware += 1

iPhone = Smartphone()
print(iPhone._firmware)
iPhone.update_firmware()
print(iPhone._firmware)
