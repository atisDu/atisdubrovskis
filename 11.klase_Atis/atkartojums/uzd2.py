masinas = []


def pieivienot_masinu(nsk, marka, gads):
    masinas.append({
        'nosaukums':nsk,
        'marka':marka,
        'gads':gads
    })

    
    print(f"Automobilis {nsk} pievienots sarakstam.")

def paradit_masinas():
    if masinas:
        print("\nAutomašīnas sarakstā: ")
        for mobilis in masinas:
            print({mobilis['nosaukums']},{mobilis['marka']},{mobilis['gads']})
    else:
        print("\nNav automašīnas sarakstā")

def atjaunot_masinu(nsk,marka,gads):
    for mobilis in masinas:
        if mobilis['nosaukums'] == nsk:
            mobilis['marka'] == marka
            mobilis['gads'] == gads
            print(f"Mašīna \"{nsk}\" ir atjaunināta")
        else:
            print(f"Mašīna \"{nsk}\" nav atrasta sarakstā.")

def izdzest_masinu(nosaukums):
    for mobilis in masinas:
        if mobilis['nosaukums'] == nosaukums:
            masinas.pop[mobilis]



def izvelne():
    while True:
        print("\n--------------------")
        print("1 - pievienot auto")
        print("2 - paradit auto")
        print("3 - atjaunināt auto informaciju")
        print("Jebko citu lai izietu")
        print("--------------------")
        opc = int(input("Izvēlies opciju: "))
        match(opc):
            case 1:
                nsk = input("Ievadi auto nosaukumu: ")
                marka = input("Ievadi auto marku: ")
                gads = input("ievadi auto ražošanas gadu: ")
                pieivienot_masinu(nsk,marka,gads)
            case 2:
                paradit_masinas()
            case 3:
                nsk = input("Ievadi auto nosaukumu, ko vēlies atjaunināt: ")
                marka = input("Ievadi jauno auto marku: ")
                gads = input("ievadi jauno auto ražošanas gadu: ")
                atjaunot_masinu(nsk,marka,gads)
            case 4:
                nosaukums = input("Ievadi tā auto nosaukumu ko vēlies iezdzēst: ")
                izdzest_masinu(nosaukums)
            case _:
                exit()
       

izvelne()