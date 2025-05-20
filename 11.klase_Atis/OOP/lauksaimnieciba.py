import datetime
import json

# Noklusējuma datu struktūra
dati = {
    "nosaukums": "",
    "augi": [],
}
nosaukums = ""

def pareiza_ievade(zina: str, variants: int): # Funkcija, kas nodrošina pareizu ievadi un to atgriež
    """
    0 - teksta ievade
    1 - pozitīvi veseli skaitļi
    2 - datums DD/MM/YY
    """ 
    match variants:
        case 0: # Pilnīgi jebkāda teksta ievade
            return input(f'{zina}: ')
        case 1: # Tikai pozitiīvi veseli skaitļi
            while True:
                ievade = input(f'{zina} [>0]: ')
                try:
                    skaitlis = int(ievade)
                    if skaitlis > 0:
                        return skaitlis
                    else:
                        raise ValueError
                except ValueError:  
                    print('! Ievade drīkst būt tikai vesels pozitīvs skaitlis. Mēginiet vēlreiz.')
        case 2: # Tikai datums formātā DD/MM/YY
            while True:
                try:
                    ievade = input(f'{zina} [DD/MM/YYYY]: ')
                    return datetime.datetime.strptime(ievade, "%d/%M/%Y").date()
                except ValueError:
                    print('! Ievade drīkst būt tikai datums formātā DD/MM/YY. Mēginiet vēlreiz.')

class Augs:
    def __init__(self, platiba: float, iestadisanas_datums: datetime.date):
        self.platiba = platiba
        self.iestadisanas_datums = iestadisanas_datums
    
    def aprekinat_razas_ienesigumu(self):
        return self.cena * self.platiba # Izmantojot apakšklases
    
class Kartupeli(Augs):
    nosaukums = "Kartupeļi"
    def __init__(self, platiba: float, iestadisanas_datums: datetime.date):
        super().__init__(platiba, iestadisanas_datums)
        self.cena = 0.4
        self.laistisanas_periods = 7

class Tomati(Augs):
    nosaukums = "Tomāti"
    def __init__(self, platiba: float, iestadisanas_datums: datetime.date):
        super().__init__(platiba, iestadisanas_datums)
        self.cena = 0.4
        self.laistisanas_periods = 2
        
class Gurki(Augs):
    nosaukums = "Gurķi"
    def __init__(self, platiba: float, iestadisanas_datums: datetime.date):
        super().__init__(platiba, iestadisanas_datums)
        self.cena = 0.4
        self.laistisanas_periods = 1
 
def formatet_augus(saraksts_ar_augiem: list): # Pārveido sarakstu ar Augs objektiem par sarakstu ar vārdnīcām kuru varēs ievietot JSON failā
    parveidotie_augi = []
    for augs in saraksts_ar_augiem:
        parveidotie_augi.append({"nosaukums": augs.nosaukums, "platiba": augs.platiba, "iestadisanas_datums": datetime.date.isoformat(augs.iestadisanas_datums)})
    return parveidotie_augi

kulturaugi = [Kartupeli, Tomati, Gurki]
audzetie_augi = []

def izvelne():
    print("--------\n[ Lauksaimniecības plānošanas programma ] \n1 - Iziet un saglabāt \n2 - Modificēt platības \n3 - Aplūkot laistīšanas kalendāru \n4 - Veikt ražas cenas aprēķinu\n5 - Pievienot platību")
    darbiba = pareiza_ievade("Lūdzu izvēlieties darbību (1, 2, 3, 4, 5)", 1)
    match darbiba:
        case 1:
            iziet_un_saglabat() # Te saglabā jsonaā un iziet
        case 2:
            modifice_platibas() #ir
        case 3:
            aplukot_laistisanas_kalendaru() 
        case 4:
            razas_cenu_aprekinasana()
        case 5:
            pievienot_platibu()
        case _:
            izvelne()

def pievienot_platibu():
    print('| Platības pievienošana |') 
    
    pieejamie_kulturaugi = [] # Izveido sarakstu ar augiem, kuri vēl netiek audzēti pārbaudot to tipu
    print(audzetie_augi)
    if audzetie_augi != []:
        for pieejams_kulturaugs in kulturaugi:
            if pieejams_kulturaugs not in [type(kulturaugs) for kulturaugs in audzetie_augi]:
                pieejamie_kulturaugi.append(pieejams_kulturaugs)
    else:
        pieejamie_kulturaugi = kulturaugi
    
    for augs in pieejamie_kulturaugi:
        print(f'Nr {pieejamie_kulturaugi.index(augs) + 1}: {augs.nosaukums}')
    #Prasa ievadīt augus
    izveletie_augi = pareiza_ievade("Ievadiet kultūraugus, ko vēlaties pievienot, izmantojot identifikatorus, piem. 1, 2, 4", 0)
    #Šos augus sadala sarakstā
    izveletie_augi = izveletie_augi.split(", ")    
    #No katra elementa atņem 1, lai sanāktu indeksi, dotajam sarkastam ar visiem kultūraugiem.
    izveletie_augi = [pieejamie_kulturaugi[int(x) - 1] for x in izveletie_augi]
    for augs in izveletie_augi:
        print(f"--------\nIevadiet {augs.nosaukums}:")
        audzetie_augi.append(augs(pareiza_ievade("Ievadiet platību", 1), pareiza_ievade("Ievadiet iestādīšanas datumu", 2)))
    
    izvelne()

def modifice_platibas():
    if audzetie_augi == []:
        print("! Nav platību, ko modificēt!")
        izvelne()
    print("| Platības |")
    for augs in audzetie_augi: # 1 - Zemenes 2 - Mellenes 3 - Tomāti
        print(f'{audzetie_augi.index(augs) + 1} - {augs.nosaukums}')
    izveletaa_platiba = pareiza_ievade("Izvēlieties platību, ko modificēt", 1) 
        #No elementa atņem 1, lai sanāktu indekss, dotajam sarkastam ar visiem kultūraugiem.
    izveletaa_platiba -=2 
    
    darbiba = pareiza_ievade("Izvelieties darbību, ko vēlaties veikt (1 - dzēst, 2 - atjaunināt laukumu)", 1)
    match darbiba:
        case 1:
            audzetie_augi.pop(izveletaa_platiba)
            print("[ Paldies! ]")
        case 2:
            #paņem 
            audzetie_augi[izveletaa_platiba].platiba = pareiza_ievade("Ievadiet jauno platību (ha)", 1)
            print("[ Paldies! ]")
    # If an exact match is not confirmed, this last case will be used if provided
        case _:
            print("Izvēlieties darbību 1 vai 2!")
    izvelne()   

def aplukot_laistisanas_kalendaru():
    print(f"| Laistīšanas kalendārs nedēļai |\n| Šodiena: {datetime.date.today().strftime('%d/%m/%Y')} |")
    for augs in audzetie_augi:
        # if sodienas datums - iestadisanas datums = pilnais stada vecums. stada vecums noapalots lidz nakamajam % 7 == 0 intervālam, kas ir lielaks vai vienads ar šodienas datumu
        starpiba = datetime.date.today() - augs.iestadisanas_datums 
        #Izrēķina atlikumu dienu skaitam, kas pagajušas kopš iestādīšanas un atgriež nākamo laistīšanas periodu
        if starpiba.days >= 0:
            if starpiba.days % augs.laistisanas_periods == 0:
                print(f"{augs.nosaukums} - {datetime.date.today().strftime('%d/%m/%Y')}")
            else:
                dienas_lidz = augs.laistisanas_periods - (starpiba.days % augs.laistisanas_periods)
                print(f"{augs.nosaukums} - {(datetime.date.today() + datetime.timedelta(days=dienas_lidz)).strftime('%d/%m/%Y')}")
        else:
            print(f"{augs.nosaukums} - {augs.iestadisanas_datums}")
    izvelne()

def razas_cenu_aprekinasana():
    kop_cena = 0
    print(f"| Ražas cenu aprēķināšana |\n| Cenas par m^2: |")
    for augs in audzetie_augi:
        print(f"{augs.nosaukums} - {round(augs.cena, 3)} m^2")
    print(f"| Kopējās kultūraugu platību cenas |")
    for augs in audzetie_augi:
        print(f"{augs.nosaukums} - {augs.platiba} m^2 - kopējā cena: {round(augs.platiba * augs.cena, 3)}€")
        kop_cena = kop_cena + augs.platiba * augs.cena
    print(f"Kopējā lauksaimniecībā audzēto augu kopējā vērtība: {round(kop_cena, 3)}€")
    izvelne() 

def iziet_un_saglabat():
    dati["nosaukums"] = nosaukums
    dati["augi"] = formatet_augus(audzetie_augi)
    with open("dati.json", "w", encoding="utf-8") as fails:
        json.dump(dati, fails)
    print('[ Paldies! Dati saglabāti. ]')

def galvena():
    try: # Ja lauksaimniecības datubāze jau pastāv
        with open("dati.json", "r", encoding="utf8") as fails: # To atver un augus pārveido par objektiem
            neformateti_dati = json.load(fails)
            # Saglabā nosaukumu
            nosaukums = neformateti_dati["nosaukums"]
            # Katram augam izveido vajadzīgo objektu
            for neformatets_augs in neformateti_dati["augi"]:
                match neformatets_augs["nosaukums"]:
                    case Kartupeli.nosaukums:
                        audzetie_augi.append(Kartupeli(neformatets_augs["platiba"], datetime.date.fromisoformat(neformatets_augs["iestadisanas_datums"])))
                    case Tomati.nosaukums:
                        audzetie_augi.append(Tomati(neformatets_augs["platiba"], datetime.date.fromisoformat(neformatets_augs["iestadisanas_datums"])))
                    case Gurki.nosaukums:
                        audzetie_augi.append(Gurki(neformatets_augs["platiba"], datetime.date.fromisoformat(neformatets_augs["iestadisanas_datums"])))
    except FileNotFoundError: # Ja nepastāv
        print("Datubāze neeksistē, ievadiet uznēmuma parametrus!")
        nosaukums = input("Ievadiet uzņēmuma vai Z/S nosaukumu: ")
        print("Kultūraugi:")
        izveletie_augi = []
        for augs in kulturaugi:
            print(f'Nr {kulturaugi.index(augs) + 1}: {augs.nosaukums}')
        #Prasa ievadīt augus
        izveletie_augi = pareiza_ievade("Ievadiet audzētos kultūraugus, izmantojot identifikatorus, piem. 1, 2, 4", 0)
        #Šos augus sadala sarakstā
        izveletie_augi = izveletie_augi.split(", ")    
        #No katra elementa atņem 1, lai sanāktu indeksi, dotajam sarkastam ar visiem kultūraugiem.
        izveletie_augi = [kulturaugi[int(x) - 1] for x in izveletie_augi]
        for augs in izveletie_augi:
            print(f"--------\nIevadiet {augs.nosaukums}:")
            audzetie_augi.append(augs(pareiza_ievade("Ievadiet platību", 1), pareiza_ievade("Ievadiet iestādīšanas datumu", 2)))

        dati["nosaukums"] = nosaukums
        dati["augi"] = formatet_augus(audzetie_augi)
        with open("dati.json", "w", encoding="utf-8") as fails:
            json.dump(dati, fails)
    izvelne()
            
galvena()
