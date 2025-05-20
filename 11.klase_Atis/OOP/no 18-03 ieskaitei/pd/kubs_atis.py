#izveido kuba klasi
class kubs():
    def __init__(self, malas_garums, krasa):
        if malas_garums < 2 or malas_garums > 10 or int(malas_garums) != malas_garums:
            print("Malas garums neatbilst nosacījumiem!")
            self.malas_garums = 2
        else:
            self.malas_garums = malas_garums
        self.krasa = krasa

    def aprekinat_tilpumu(self):
        return (self.malas_garums * self.malas_garums * self.malas_garums)
#Tā kā definēts, ka klasē ir tikai konstruktors un aprekinat_tilpumu metode, pats info tiek izprintēts ārpus klases metodēm, ņemot dedfinētos mainīgos
print("Dati par kubg objektu:")
kubg = kubs(10, "zaļa")

print(f"Kubg krāsa un tilpums: {kubg.krasa} {kubg.aprekinat_tilpumu()}\nKubg malas garums: {kubg.malas_garums}\n***")

print("Dati par kubr objektu:")
kubr = kubs(1, "sarkana")
print(f"Kubr krāsa un tilpums: {kubr.krasa} {kubr.aprekinat_tilpumu()}\nKubr malas garums: {kubr.malas_garums}\n***")

#izveido bloka klasi, kas manto no kuba, bet pieliek klāt vēl argumentu
class bloks(kubs):
    def __init__(self, malas_garums, krasa, kubu_sk_bloka, forma):
        super().__init__(malas_garums, krasa)
        self.derigums = 0
        #Pārbauda argumentu vertības
        if kubu_sk_bloka < 1 or kubu_sk_bloka > 4:
            print("Nepareiza kubu skaita vērtība!")
            self.kubu_sk_bloka = 1
        else:
            self.kubu_sk_bloka = kubu_sk_bloka 
        self.nosaukums = f"{self.krasa}{self.kubu_sk_bloka}"
        if (forma < 11 or forma > 14) and forma != 22:
            print("Forma neatbilst nosacījumiem")
            self.derigums = 0
        else:
            self.derigums = 1
    #Aprēķina tilpumu
    def tilpums(self):
        return (self.malas_garums * self.malas_garums * self.malas_garums * self.kubu_sk_bloka)
    #izvada informāciju par bloku
    def izvadit_info(self):
        if self.derigums == 1:
            print(f"{self.nosaukums} {self.tilpums()} derīgs 1")
        else:
            print(f"{self.nosaukums}  nederīgs 0")
        print("***")
    def mainit_formu(self, forma):
        self.forma = forma
        print(f"Mainīta forma:\n{self.nosaukums} {self.malas_garums} derīgs 1\n***")

#Tā kā nosaukums pašam objektam izvadē ir citadāks, tas ir atseviški jādefinē, varētu arī paņemt krāsas mainīgo, uzlikt pirmo lielo burtu un pēdejo burutu samainīt ar s,
#bet laika ierobežojuma dēļ jāīzmanto vnk print(), jo nosacījumos nav specifiski norādīts, kā jāizvada objekta nosaukums
print("Oranžs objekts:")
oranzs = bloks(5, "oranža", 3, 13)
oranzs.izvadit_info()

print("Zils objekts:")
zils = bloks(7, "zila", 5, 23)
zils.izvadit_info()
zils.mainit_formu(12)

