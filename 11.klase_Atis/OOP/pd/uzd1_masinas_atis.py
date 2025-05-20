#Izveido klasi transportlidzeklis
class Transportlidzeklis:
    #Tiek inicializēts konstruktors un pieškirti attiecīgie atribūti
    def __init__(self, zimols, modelis, reg_datums, pilna_masa, degvielas_veids):
        self.zimols = zimols
        self.modelis = modelis
        self.reg_datums = reg_datums
        self.pilna_masa = pilna_masa
        self.degvielas_veids = degvielas_veids
    
    #Izdrukā visus atribūtus, kas definēti objektā formatētā veidā
    def izvadit_info(self):
        print(f"zīmols: {self.zimols}\nmodelis: {self.modelis}\nreģistrācijas datums: {self.reg_datums}\npilna masa: {self.pilna_masa}\ndegvielas veids: {self.degvielas_veids}")

#Izveido objektu un izsauc tā izvades funkciju 
audi = Transportlidzeklis("Audi","A4","22.10.2019.",1800,"BG")
audi.izvadit_info()