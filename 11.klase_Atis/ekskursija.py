#Inicializējam visus sarakstus
transportaSar = []
pieturuSar = []
attalumuSar = []
laikaSar = []
cenuSar = []


def datuIevade():
   x = 1
   while x == 1:
    print("------------------------------\nPieturu ievadīšana\n------------------------------\nIevadi pieturu nosaukumus (no-līdz)(piem. Jūrmala – Līvu Akvaparks)")
    pieturuNosaukums = input(": ")
    print("Kāds ir izvēlētais transporta veids? (autobuss, vilciens, kājām)")
    try:
        transportaVeids = input(": ") 
        if transportaVeids != "autobuss" and transportaVeids != "vilciens" and transportaVeids != "kājām":
            raise ValueError
    except ValueError: 
        print("Kļūda, izvēlies vai nu autobuss, vilciens, kājām!")
        transportaVeids = input(": ") 
        
    
    try:
        pieuturuAttalums = float(input("Kāds ir attālums starp šīm pieturām? (km)\n: "))
        if pieuturuAttalums < 1:
            raise ValueError
    except ValueError:
        print("Kļūdains attālums, ievadiet attālumu kilometros!")
        pieuturuAttalums = float(input("Kāds ir attālums starp šīm pieturām? (km)\n: "))
    
    
    
    if transportaVeids != "kājām":
        print("------------------------------\nAutobusa biļetes cenas var atrast 1188.lv,\nVilciena biļešu cenas var atrast vivi.lv\nKāda ir biļetes cena? (€)")
        try:
            bilesuCena = float(input(": "))
            if bilesuCena < 0:
                raise ValueError
        except ValueError:
            print("Ievadiet biļetes cenu €!")
            bilesuCena = float(input(": "))
    else:
        bilesuCena = 0

    
    try:
        pieturuLaiks = int(input("Cik ilgs laiks jāpavada transportā? (veselās min)\n: "))
        if pieturuLaiks < 0:
            raise ValueError
    except ValueError:
        print("Kļūdains transport laiks, ievadiet laiku veselās min!")
        pieturuLaiks = int(input("Cik ilgs laiks jāpavada transportā? (veselās min)\n: "))

    
    try:
        laiksStarp = int(input("Cik ilgu laiku pavadīs starp šo un nākamo transportu? (veselās min)\n: "))
        if laiksStarp < 0:
            raise ValueError
    except ValueError:
        print("Kļūdains starplaiks laiks, ievadiet laiku veselās min!")
        laiksStarp = int(input("Cik ilgu laiku pavadīsiet starp šo un nākamo transportu? (veselās min)\n: "))
    
    pieturuSar.append(pieturuNosaukums)
    transportaSar.append(transportaVeids)
    attalumuSar.append(pieuturuAttalums)
    laikaSar.append(pieturuLaiks+laiksStarp)
    cenuSar.append(bilesuCena)
    try:
        opcija = input("Vai vēlaties ievadīt vēl vienu pieturu? (jā/nē) (j/n)\n: ")
        if opcija != "jā" and opcija != "nē" and opcija != "j" and opcija != "n":
            raise ValueError
    except ValueError:
        print("Kļudaina izvēle, ievadiet jā, nē, n vai j!")
    
    if opcija == "nē" or opcija == "n":
        x = 0
        opcijuIzvelne()
    
def redigetDatus():
    for i in range(0, len(pieturuSar)):
        print(f"Nr. {i+1}, ", end="")
    print("Pieturas: ", end ="")
    print(",".join(pieturuSar))
    print("") 
    print("Transportlīdzekļi: ", end ="")
    print(",".join(transportaSar)) 
    print("")
    print("Attālumi km: ", end ="")
    print(",".join(map(str, attalumuSar))) 
    print("")
    print("Laiki min: ", end ="")
    print(",".join(map(str, laikaSar))) 
    print("")
    print("Cenas €: ", end ="")
    print(",".join(map(str, cenuSar))) 
    
    opcija = int(input("Izvēlies kuru pieturu vēlies mainīt? (ievadi tās pieturas nr.)\n: "))
    opcija = opcija - 1
    print("------------------------------\nPieturas rediģēšana\n------------------------------")
    print("Ievadi jauno pieturu nosaukumus (no-līdz)(piem. Jūrmala – Līvu Akvaparks)")
    pieturuNosaukums = input(": ")
    print("Kāds ir izvēlētais transporta veids? (autobuss, vilciens, kājām)")
    try:
        transportaVeids = input(": ") 
        if transportaVeids != "autobuss" and transportaVeids != "vilciens" and transportaVeids != "kājām":
            raise ValueError
    except ValueError: 
        print("Kļūda, izvēlies vai nu autobuss, vilciens, kājām!")
        transportaVeids = input(": ") 
        
    
    try:
        pieuturuAttalums = float(input("Kāds ir attālums starp šīm pieturām? (km)\n: "))
        if pieuturuAttalums < 1:
            raise ValueError
    except ValueError:
        print("Kļūdains attālums, ievadiet attālumu kilometros!")
        pieuturuAttalums = float(input("Kāds ir attālums starp šīm pieturām? (km)\n: "))
    
    print("------------------------------\nAutobusa biļetes cenas var atrast 1188.lv,\nVilciena biļešu cenas var atrast vivi.lv\nKāda ir biļetes cena? (€)")
    
    if transportaVeids != "kājām":
        try:
            bilesuCena = float(input(": "))
            if bilesuCena < 0:
                raise ValueError
        except ValueError:
            print("Ievadiet biļetes cenu €!")
            bilesuCena = float(input(": "))
    else:
        bilesuCena = 0
    
    
    try:
        pieturuLaiks = int(input("Cik ilgs laiks jāpavada transportā? (veselās min)\n: "))
        if pieturuLaiks < 0:
            raise ValueError
    except ValueError:
        print("Kļūdains transport laiks, ievadiet laiku veselās min!")
        pieturuLaiks = int(input("Cik ilgs laiks jāpavada transportā? (veselās min)\n: "))

    
    try:
        laiksStarp = int(input("Cik ilgu laiku pavadīs starp šo un nākamo transportu? (veselās min)\n: "))
        if laiksStarp < 0:
            raise ValueError
    except ValueError:
        print("Kļūdains starplaiks laiks, ievadiet laiku veselās min!")
        laiksStarp = int(input("Cik ilgu laiku pavadīsiet starp šo un nākamo transportu? (veselās min)\n: "))
    
     
    pieturuSar[opcija] = pieturuNosaukums
    transportaSar[opcija] = transportaVeids
    attalumuSar[opcija] = pieuturuAttalums
    laikaSar[opcija] =  pieturuLaiks+laiksStarp
    cenuSar[opcija] = bilesuCena

    print("------------------------------\nDati rediģēti veiksmīgi!")
    print("Pieturas:", end ="")
    print(",".join(pieturuSar)) 
    print("Transportlīdzekļi:", end ="")
    print(",".join(transportaSar)) 
    print("Attālumi km:", end ="")
    print(",".join(map(str, attalumuSar))) 
    print("Laiki min:", end ="")
    print(",".join(map(str, laikaSar))) 
    print("Cenas €:", end ="")
    print(",".join(map(str, cenuSar))) 
    print("------------------------------")

    opcijuIzvelne()

def marsrutaDetalas():
    try:
        skolenuSkaits = int(input("Ievadiet skolēnu skaitu\n: "))
        if skolenuSkaits < 1:
            raise ValueError
    except ValueError:
        print("Kļūdains skolēnu skaits, ievadiet veselu skaitli!")

    
    for i in range(0, len(pieturuSar)):
        print(f"{pieturuSar[i]}| {transportaSar[i]}| {attalumuSar[i]} km| {cenuSar[i]} € uz cilvēku | {round(float(cenuSar[i]) * float(skolenuSkaits), 2)} € kopā| {laikaSar[i]} minūtes|")
        print("------------------------------")
        kopLaiks = 0
        kopIzmaksas = 0
        kopIzmaksasUzVienu = 0

        for t in laikaSar:
            kopLaiks = kopLaiks + t

        for n in cenuSar:
            kopIzmaksasUzVienu = kopIzmaksasUzVienu + n

        kopIzmaksas = kopIzmaksasUzVienu * skolenuSkaits

    print(f"Kopējais ekskursija laiks: {kopLaiks} min\nKopējās ekskursijas izmaksas: {round(kopIzmaksas, 2)} €\nKopējās izmaksas uz vienu cilvēku: {round(kopIzmaksasUzVienu, 2)} €")
    print("------------------------------")
    exit()



#Izvēlnes funkcijas deklarācija
def opcijuIzvelne():
    print("Izvēlne:\n------------------------------\n1 - Ievadīt pieturu datus\n2 - Rediģēt pieturu datus\n3 - Aprēķināt un izvadīt kopējo pieturu maršrutu, datus\n4 - iziet\n------------------------------")
    try:
        opcija = int(input("Ievadiet izvēli: "))
        if opcija < 1 or opcija > 4:
            raise ValueError
    except ValueError:
        print("Kļūdaina izvēle, izvēlaties skaitli no 1 līdz 4!")
        opcija = int(input("Ievadiet izvēli: "))
    
    match opcija:
        case 1:
            datuIevade()
        case 2:
            redigetDatus()
        case 3:
            marsrutaDetalas()
        case 4:
            exit()

print("------------------------------\nEkskursijas maršruta plānotājs\n------------------------------\n")
opcijuIzvelne()