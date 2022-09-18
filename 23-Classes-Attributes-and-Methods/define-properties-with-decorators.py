class Currency():
    def __init__(self, dollars):
        self._cents = dollars * 100
    
    @property
    def dollars(self):
        return self._cents / 100

    @dollars.setter
    def dollars(self, dollars):
        if dollars >= 0:
            self._cents = dollars * 100

bank_account = Currency(50000)
print(bank_account.dollars)

bank_account.dollars = 650000
print(bank_account.dollars)

bank_account.dollars = -600000
print(bank_account.dollars)

class PizzaPie():
    def __init__(self, total_slices):
        self._slices_eaten = 0
        self.total_slices = total_slices
   
    @property     
    def slices_eaten(self):
        return self._slices_eaten
       
    @slices_eaten.setter    
    def slices_eaten(self, slices_eaten):
        if slices_eaten < self.total_slices:
            self._slices_eaten = slices_eaten
    
    @property     
    def percentage(self):
        return self._slices_eaten / self.total_slices

cheese = PizzaPie(8)
cheese.slices_eaten = 2
print(cheese.percentage)

cheese.slices_eaten = 10
print(cheese.percentage)

#cheese.percentage = 0.50