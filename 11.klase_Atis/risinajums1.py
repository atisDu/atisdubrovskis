def parabudit_vardu_uzvardu(teksts):
    return teksts.isalpha() and teksts.strip()
    

def parbaudit_vecumu(vecums):
    return vecums.isdigit() and int(vecums)>0
    

def parbaudit_atzimi(atzime):
    return atzime.isdigit() and 0<=int(atzime)<=10
    

def ierobezo_meginajumus(parbaudit_funkcija, ievades_teksts,kludas_teksts):
    for i in range (0, 3):
        dati = input(ievades_teksts)
        if parbaudit_funkcija(dati):
            return dati
        print(kludas_teksts)
    print("Pārsniegts mēģinājumu skaits!")
    exit()

    return False


def iegut_ierakstu():
    ieraksti=[]
    while True:
        vards = ierobezo_meginajumus(parabudit_vardu_uzvardu, "Ievadiet vārdu:", "Kļūda, var būt tikai burti")
        if not vards:
            break
        uzvards = ierobezo_meginajumus(parabudit_vardu_uzvardu, "Ievadiet uzvārdu:", "Kļūda, var būt tikai burti")
        if not uzvards:
            break
        vecums = ierobezo_meginajumus(parbaudit_vecumu, "Ievadiet vecumu:", "Kļūda, var būt tikai skaitļi")
        if not vecums:
            break
        atzime = ierobezo_meginajumus(parbaudit_atzimi, "Ievadiet atzīmi:", "Kļūda, var būt tikai skaitļi (0-10)")
        if not atzime:
            break
        
        ieraksti.append((vards,uzvards,int(vecums),int(atzime)))
        turpinat = input("Vai turpināt? (j/n): ").lower()
        if turpinat != "j":
            break
        
        return ieraksti[0]

def saglabat_faila(ieraksti, faila_nosaukums="kontroldarbs.txt"):
    # saglabāt ierakstus ar tabu starp laukiem
    with open(faila_nosaukums, "a", encoding="utf8") as fails:
        for i in ieraksti:
            fails.write("\t".join(map(str, i) + "\n"))
    print(f"Dati saglabāti failā: {faila_nosaukums}")


def iegut_gala_atzimi(ieraksts):
    return ieraksts[3]


def paradit_sakartotus_datus(ieraksti):
    #sakārtoti dati pēc gala atzīmes
    #Svarīgī!! izmanto laikam vienā indeksā saglbātus vairākus
    #definēt anonīmo funkciju lambda, kas pieņem 1 argumentu
    #kārto pēc katra trešā ierakstos
    
    #Abiem jāstrādā
    sakartoti_ieraksti = sorted(ieraksti, key=lambda x:x[3])

    #sakartoti_ieraksti = sorted(ieraksti, key=iegut_gala_atzimi())
    print("\nVārds\tUzvārds\tVecums\tAtzīme")
    for i in ieraksti:
        print("\t".join(map(str, i) + "\n"))

    print(f"Bez formatēšanas: {i}")




def izvelne(): # programmas galvenā daļa
    ieraksti = []

    while True:
        print("Izvēlieties darbību:\n1 - Ievadīt datus\n2 - Saglabāt datus failā\n3 - Parādīt datus sakārtotus pēc gala atzīmes (augošā secībā)\n4 - Iziet no programmas")
        izvele = input("Jūsu izvēle: ")
        if izvele == "1":
            ieraksti += iegut_ierakstu() 
        elif izvele == "2":
            if ieraksti:
                saglabat_faila(ieraksti)
            else:
                print("Nav datu!")
        elif izvele == "3":
            if ieraksti:
                paradit_sakartotus_datus(ieraksti)
            else:
                print("Nav datu!")
                break   
        else:
            print("Nepareiza izvēle!")

izvelne()