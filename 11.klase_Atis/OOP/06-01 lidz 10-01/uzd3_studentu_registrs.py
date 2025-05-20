class Students:
    def __init__(self, vards, uzvards):
        self.vards = vards
        self.uzvards = uzvards

    def parbauda_vecumu(self, vecums, kursa_nr):
        try:
            if vecums < 18:
                raise ValueError
            else: 
                self.vecums = vecums
        except ValueError: 
                print("Jābūt vismaz 18 gadu vecumam!")  
        try:        
            if kursa_nr < 1 or kursa_nr > 4:   
                raise ValueError
            else:
                self.kursa_nr = kursa_nr
        except ValueError:
                print("Var būt tikai 1-4 kurss!")

    def parada_datus(self):
        print(f"-------------------\nStudents: {self.vards} {self.uzvards}\nVecums: {self.vecums}\nKurss: {self.kursa_nr}. kurss")

vards = input("Ievadiet studenta vārdu: ")

uzvards = input("Ievadiet studenta uzvārdu: ")
vecums = int(input("Ievadiet studenta vecumu: "))
kursa_nr = int(input("Ievadiet studenta kursa numuru: "))

janis = Students(vards, uzvards)
janis.parbauda_vecumu(vecums, kursa_nr)
janis.parada_datus()