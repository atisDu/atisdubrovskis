#A uzdevums
#Galvenā klase
class Masina:
    #Tiek inicializēts konstruktors un pieškirti attiecīgie atribūti
    def __init__(self, marka, modelis, gads):
        self.marka = marka
        self.modelis = modelis
        self.gads = gads
    #B Uzdevums
    def uzsakt(self): 
            print(f"{self.marka} {self.modelis} sāk darboties.", end="")
            return ""
    def apstaties(self):
            print(f"{self.marka} {self.modelis} ir apstādināta.\n")
    def info_par_auto(self):
       print(f"Marka: {self.marka}, Modelis: {self.modelis}, Gads: {self.gads} ", end="")
       return "" 

#C uzdevums
# tiek izveidots obejkts un palaistas metodes
toyota = Masina("Toyota", "Corolla", 2010)
toyota.info_par_auto()
print("")
toyota.uzsakt()
print("")
toyota.apstaties()

#D uzdevums
#Izveido klasi Elektro_auto un manto
class Elektro_auto(Masina):
    def __init__(self, marka, modelis, gads, akumulatora_ietilp):
        super().__init__(marka, modelis, gads)
        self.uzlades_limenis = 100 
        self.akumulatora_ietilp = akumulatora_ietilp
    # F uzdevums
    def uzsakt(self):
        if self.uzlades_limenis < 20:
            print(f"{self.marka} {self.modelis} nevar sākt darboties, jo akumulators ir pārāk zems: {self.uzlades_limenis}%\n") 
        else:
            print(super().uzsakt())
            print(f"Akumulators: {self.uzlades_limenis}%")
            self.uzlades_limenis = 15
    
    #G uzdevums
    def info_par_auto(self):
        print(super().info_par_auto())
        print(f"Akumulators: {self.akumulatora_ietilp} kWh")

#H uzdevums
# tiek izveidots obejkts un palaistas metodes
tesla = Elektro_auto("Tesla", "Model 3", 2022, 75)
tesla.info_par_auto()
tesla.uzsakt()
# I uzdevums 9 simulē samazināšanos
tesla.uzsakt()

#J uzdevums
#Izveido klasi Degvielas_Auto un manto
class Degvielas_Auto(Masina):
    def __init__(self, marka, modelis, gads, bakas_tilpums):
        super().__init__(marka, modelis, gads)
        self.bakas_tilpums = bakas_tilpums
        #K uzdevums
        self.degvielas_limenis = 100
    
    #L uzdevums
    def uzsakt(self):
        if self.degvielas_limenis < 10:
            print(f"{self.marka} {self.modelis} nevar sākt darboties, jo degvielas līmenis ir pārāk zems: {self.degvielas_limenis}%\n") 
        else:
            print(super().uzsakt())
            print(f"Degvielas līmenis: {self.degvielas_limenis}%")
            # O uzdevums (simulē zemu bākas līmeni)
            self.degvielas_limenis = 5

    #M uzdevums
    def info_par_auto(self):
        print(super().info_par_auto())
        print(f"Bākas tilpums: {self.bakas_tilpums} litri")

#N uzdevums
# tiek izveidots obejkts un palaistas metodes
audi = Degvielas_Auto("Audi", "A7", 2022, 85)
audi.info_par_auto()
audi.uzsakt()
audi.uzsakt()