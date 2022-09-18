class SushiPlatter():
    def __init__(slef, salmon, tuna, shrimp, squid):
        slef.salmon = salmon
        slef.tuna = tuna
        slef.shrimp = shrimp
        slef.squid = squid
    
    @classmethod
    def luch_special_A(cls):
        return cls(2, 2, 0, 2)
    
    @classmethod
    def tuna_lover(cls):
        return cls(shrimp = 1, tuna = 9, squid = 2, salmon = 0)

boris = SushiPlatter(salmon = 8, tuna = 4, squid = 5, shrimp = 10)
print(boris.squid)

nk = SushiPlatter.luch_special_A()
print(nk.shrimp)
print(nk.salmon)

awy = SushiPlatter.tuna_lover()
print(awy.tuna)