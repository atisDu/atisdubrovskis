#Tiek izveidota klase Doktorats
class Doktorats:
    #Tiek inicializēts kontstruktors un definēti atribūti
    def __init__(self, nosaukums, pacientu_sk):
        self.nosaukums = nosaukums
        self.pacientu_sk = pacientu_sk
    
    #Tiek izvidota metode, kas ļauj ievadīt doktorāta datus.
    def datu_ievade(self):
        self.nosaukums = input("Ievadiet doktorāta nosaukumu: ")
        try:
            self.pacientu_sk = int(input("Ievadiet pacientu skaitu: "))
        except ValueError:
            print("Pacientu skaitam jābut veselam skaitlim!")
            self.pacientu_sk = int(input("Ievadiet pacientu skaitu: "))
    
    #Tiek izveidota metode, kas izdrukā atribūtus formatētā veidā
    def datu_izvade(self):
        print(f"Doktorāts {self.nosaukums} apkalpo {self.pacientu_sk} pacientus.")

#Definē doktorātu kā tukšu objektu, izsauc datu ievades metode un izvada atribūtus
augstkalne = Doktorats("", "")
augstkalne.datu_ievade()
augstkalne.datu_izvade()
            