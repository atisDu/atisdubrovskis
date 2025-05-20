#Klase vieiss ar konstrukotru (inicializatoru)

class Viesis:
    def __init__(self, vards, parole):
        self.vards = vards
        self.parole = parole
    
    def druka_vardu(self):
        print("Lietotājs", self.vards, "parole",self.parole)
    
    def parbauda_paroli(self,parole):
        if self.parole == parole:
            print("Lietotāja ", self.vards, "parole pareiza") 
    
vards = "Valdis"
parole = "12345"

#izveido objektu
viesis1 = Viesis(vards, parole)
#objektam izsauc metodes
viesis1.druka_vardu()
viesis1.parbauda_paroli(parole)