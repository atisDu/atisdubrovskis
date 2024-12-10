vardi = []
uzvardi = []
vecumi = []
atzimes = []


def vaiStop(x):
    try:
        if x == "Stop":
            exit()
    except ValueError:
        return False

def klumes(funkcija):
        for i in range (3):
            if funkcija:
                return True
        return False

def parbaudaVardu():
    vards = input("Ievadiet Vārdu: ")
    if vards == None:
        print("Kļūda")
        return False
    elif vards.strip() != vards:
        print("Kļūda")
        return False
    else:
        vardi.append(vards)
        return True

def parbaudaUzvardu():
    vards = input("Ievadiet uzvārdu: ")
    if vards == None:
        print("Kļūda")
        return True
    elif vards.strip() != vards:
        print("Kļūda")
        return True
    else:
        uzvardi.append(vards)
        return False

def parbaudaVecumu():
    vecums = input("Ievadiet vecumu: ")
    
    if vecums > 0:
        vecumi.append(vecums)
        return False
    else:
        print("Kļūda")
        return True


def parbaudaAtzimi():
    atzime = input("Ievadiet gala atzīmi (1-10): ")
    if atzime >= 0 and atzime <= 10:
            atzimes.append(atzime)
            return False
    else:
            print("Kļūda")
            return True

def ievaditDatus():
    vai = "jā"
    while vai == "jā":
        print("Ievadiet jaunu ierakstu vai ievadiet 'STOP', lai pārtrauktu.")
        
        klumes(parbaudaVardu())
        
        
        

        '''klumes = 0
        while parbaudaVardu != 0:
        if parbaudaVardu(vards) == 1:
            klumes= klumes + 1
        if klumes > 3:
            print("Pārsniegts mēģinājumu skaits!")
            exit()
        '''
       
       
        klumes(parbaudaUzvardu())
        
        klumes(parbaudaVecumu())
        
        klumes(parbaudaAtzimi())

    try:
        vai = input("Vai vēlaties ievadīt vēl vienu ierakstu? (jā/nē): ")
        if vai != "jā" and vai != "nē":
            raise ValueError
    except ValueError:
        print("Kļūme")
        vai = input("Vai vēlaties ievadīt vēl vienu ierakstu? (jā/nē): ")
        if vai == "nē":
            exit()
    exit()

def saglabatDatus():
    f = open("kontroldarbs.txt", "a+")
    pirmaisChar = f.read(1)
    
    if not pirmaisChar:
        print("Fails ir tukšs")
        exit()

    for i in vardi:
        f.write(f"{vardi[i]} {uzvardi[i]}, vecums: {vecumi[i]}, gala atzīme: {atzimes[i]}\n")
    print("Dati saglabāti failā: kontroldarbs.txt")

def sakartotUnParadit():
    vardi.sort()
    uzvardi.sort()
    vecumi.sort()
    atzimes.sort()


    for x in vecumi:
        print(f"{vardi[x]} {uzvardi[x]}, vecums: {vecumi[x]}, gala atzīme: {atzimes[x]}\n")


def izvelne():
    print("Izvēlieties darbību:\n1 - Ievadīt datus\n2 - Saglabāt datus failā\n3 - Parādīt datus sakārtotus pēc gala atzīmes (augošā secībā)\n4 - Iziet no programmas")
    izvele = int(input("Jūsu izvēle: "))
    if izvele == 1:
        ievaditDatus()
    if izvele == 2:
        saglabatDatus()
    if izvele == 3:
        sakartotUnParadit()

izvelne()