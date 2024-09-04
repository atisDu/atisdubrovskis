import math

#Podestu standarta izmērs 200x100 , gan pasutijuma izmeeros 

#Vienas loksnes izmērs 1250x2500

#pdesti ir taisnstūri, kas izveidoti no sešām plaāksnēm
#savās tarpā sastiprināti ar divpadsmit profiliem
#sturos nostiprināti ar astoņiem sūra savienojumiem

def materialuUzskaite(tips):
    derigs = {"finieris", "liste", "sturis"}
    if tips not in derigs:
        print("Pieņemti tikai parametri - finieris, liste vai sturis")
        exit()
    str(tips)

    if tips == "finieris":
        return 1250 * 2500 * 6
    elif tips == "liste":
        return 12
    else:
        return 8





def materialuAprekins(garums, platums, augstums, skaits):
    round(garums,1)
    round(platums,1)
    round(augstums,1)

    global finDaudz
    global listuDaudz
    global sturuDaudz

    finDaudz = (garums * platums * 2 + garums * augstums * 2 + augstums * platums * 2) * skaits / materialuUzskaite("finieris")
    listuDaudz = materialuUzskaite("liste")
    sturuDaudz = materialuUzskaite("sturis")
    print("-----------------------------------------------")
    print("Būs nepieciešamas", finDaudz, "finiera saplākšņu.")
    print("Būs nepieciešamas", listuDaudz, "līstes.")
    print("Būs nepieciešamas", sturuDaudz, "stūru.")


materialuAprekins(float(input("Ievadi podesta garumu: ")), float(input("Ievadi podesta platumu: ")), float(input("Ievadi podesta augstumu: ")), int(input("Ievadi podestu skaitu: ")))

def materialuCena(finDaudz, listuDaudz, sturuDaudz):
    print("-----------------------------------------------")
    finBiez = int(input("Ievadi finiera biezumu mm: "))
    if finBiez < 12 or finBiez > 21:
        print("Finiera biezums var būt starp 12 un 21 mm!")
        exit()
    
    
    if finBiez == 12:
        finCena = 68.5
    elif finBiez == 15:
        finCena = 78.00
    elif finBiez == 18:
        finCena = 86.5    
    else: 
        finCena = 97

    listuCena = 5.58
    listuKopCena = listuDaudz * listuCena
    finKopCena = finCena * finBiez
    
    sturuCena = 0.3
    sturuKopCena = sturuCena * sturuDaudz
    print("-----------------------------------------------")
    print("Cena par vienu finiera plāksni:", round(finCena,3), "$.")
    print("Cena par vienu līsti:", round(listuCena,3), "$.")
    print("Cena par vienu stūri:", round(sturuCena,3), "$.")
    print("-----------------------------------------------")
    print("Finiera plākšņu cena būs", round(finKopCena,3), "$")
    print("Līstu cena būs", round(listuKopCena,3), "$")
    print("Stūru cena būs", round(sturuKopCena, 3), "$")
    print("-----------------------------------------------")
    print("Kopējās izmaksas ir:", finKopCena + listuKopCena + sturuKopCena)

materialuCena(finDaudz, listuDaudz, sturuDaudz)