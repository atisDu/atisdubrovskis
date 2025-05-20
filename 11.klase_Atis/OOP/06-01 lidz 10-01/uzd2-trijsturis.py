#Klase vieiss ar konstrukotru (inicializatoru)

class Trijsturis:
    def __init__(self, mala1, mala2, mala3):
        self.mala1 = mala1
        self.mala2 = mala2
        self.mala3 = mala3
    
    def druka_laukumu(self):
        s = (self.mala1+self.mala2+self.mala3)/2
        print(round((s*(s-self.mala1)*(s-self.mala2)*(s-self.mala3))**0.5, 2))
    
mala1 = int(input("Ievadi 1. malu"))
mala2 = int(input("Ievadi 2. malu"))
mala3 = int(input("Ievadi 3. malu"))
#izveido objektu
trijsturis1 = Trijsturis(mala1, mala2, mala3)
#objektam izsauc metodes
trijsturis1.druka_laukumu()