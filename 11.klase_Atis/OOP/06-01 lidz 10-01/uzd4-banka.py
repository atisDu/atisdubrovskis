#izvwedidt klasi Bankaskonts
#ielikt klienta vards un atlikums
#klase ir 2 metodews iemaksat(summa) palielina atlikumu
#metode iznemt (summa) - samazina konta atlikumu par norādīto summu, ja pietiek
#objekti klients Laura sākumā ir 100 eiro | iemaksā 50, pārbauda atlikumu | 
#izņem 30, pēc tam mēģina izņemt 200, lai notestētu 
class BankasKonts:
    def __init__(self, vards, atlikums):
        self.vards = vards
        self.atlikums = atlikums
    def iemaksa(self, summa):
        self.atlikums = self.atlikums + int(summa)
        print(f"Kontā iemaksāti {summa} eiro, atlikums: {self.atlikums}")
    def iznemt(self, summa):
        if self.atlikums > summa:
            self.atlikums = self.atlikums - int(summa)   
            print(f"No konta izņemti {summa} eiro, atlikums: {self.atlikums}")
        else:
            print("Kontā nepietiek līdzekļu!")

laura = BankasKonts("Laura", 100)
laura.iemaksa(50)
laura.iznemt(30)
laura.iznemt(200)


class lidzekli(BankasKonts):
    def __init__(self, vards, atlikums, atzime):
        super().__init__(vards, atlikums)
        self.atzime = atzime
    def printe_visu(self):
        print(f"atlikums: {self.atlikums}, atzīme: {self.atzime}")

boburns = lidzekli("Atis",69,2)
boburns.printe_visu()