print("---------------------------------------")
print("--------Ievārijuma kalkulators---------")
print("---------------------------------------")
cenIzveele = input("Vai vēlies izmantot aptuvenās cenas sastāvdaļām, vai ievadīt? (apt/iev): ")
if cenIzveele == "apt":
    cenaAbolu = 0.79
    cenaParCukura = 1.44
    cenaIevCukura = 1.99
    cenaCitronu = 2.29 
    cenaMandeks = 0.24
    cenaKaneelis = 0.43 / 20
else:
    cenaAbolu = float(input("Ievadi cenu papildus āboliem kg: "))
    cenaParCukura = float(input("Ievadi cenu parastajam cukuram kg: "))
    cenaIevCukura = float(input("Ievadi cenu ievārijuma cukuram kg: "))
    cenaCitronu = float(input("Ievadi cenu citroniem kg: "))
    cenaMandeks = float(input("Ievadi cenu mandeļu ekstraktam ml: "))
    cenaKaneelis = float(input("Ievadi cenu kanēlim kg: "))





cikCukurs = 0
cikCitronu = 0
cikMandeks = 0
cikKaneelis = 0

print("------------Sastāvdaļu ievade----------")
cikAbolu = float(input("Cik daudz ābolu ir? (kg): "))
kadsCukurs = input("Kādu cukuru vēlaties izmantot? parasto/ievārijuma (p/i): ")
vaiCukurs = input("Vai mājās jau ir cukurs? (n/j): ")
if vaiCukurs == "j":
    cikCukurs = float(input("Cik daudz cukura jau ir? (g): "))
vaiCitronu = input("Vai mājās jau ir citronu? (n/j): ")
if vaiCitronu == "j":
    cikCitronu = float(input("Cik citronu jau ir? (kg): "))
vaiMandeks = input("Vai mājās jau ir Mandeļu ekstrakta? (n/j): ")
if vaiMandeks == "j":
    cikMandeks = float(input("Cik daudz mandeļu ekstrakta jau ir? (ml)"))
vaiKaneelis = input("Vai mājās jau ir kanēlis? (n/j): ")
if vaiKaneelis == "j":
    cikKaneelis = float(input("Cik daudz kanēļa jau ir? (g): "))

"""
print("---------------------------------------")
print("3 kg āboli")
print("1 kg cukurs")
print("500 ml ūdens")
print("1 gb citrons")
print("5 ml mandeļu ekstrakts")
print("10g kanēlis")
print("---------------------------------------")
receptesIzveele = input("Vai vēlaties ievadīt savu recepti, vai izmantot šo? (n/j): ")
"""



print("------------Receptes ievade------------")
cikL = float(input("Cik l ievārijuma vēlaties pagatavot?"))
aaboli = float(input("Cik kg ābolu ir prasīti receptē? (kg): "))
if aaboli > cikAbolu:
    print("Tev nepietiek ābolu, vēl nepieciešami:", aaboli - cikAbolu, "kg.")
cukurs = float(input("Cik daudz cukura vajadzīgs cukuram? (kg): "))
if cukurs > cikCukurs:
    print("Būs jāpiepērk", cukurs - cikCukurs, "kg cukura.")
udens = float(input("Cik daudz ūdens ir vajadzīgs? (ml): "))
citroni = float(input("Cik daudz citroni vajadzīgi? (gb): "))
if citroni > cikCitronu:
    print("Būs jāpiepērk", citroni - cikCitronu, "kg citronu.")
Mandeks = float(input("Cik daudz mandēļu ekstrakta ir vajadzīgs? (ml):"))
if Mandeks > cikMandeks:
    print("Būs jāpiepērk", Mandeks - cikMandeks, "ml mandeļu ekstrakta.")
kaneelis = float(input("Cik daudz kanēļa vajadzīgs? (g): "))
if kaneelis > cikKaneelis:
    print("Būs jāpiepērk", kaneelis - cikKaneelis, "g kanēļa.")


print("------------Receptes izvade------------")
print(aaboli, "kg āboli")
print(cukurs, "kg cukura")
print(udens, "ml ūdens")
print(citroni, "kg citronu")
print(Mandeks, "ml mandeļu ekstrakta")
print(kaneelis, "g kanēļa")

Aabols = max(0, cikAbolu / aaboli) # piemeram 9, noapalojiet lidz 0
Acukurs = max(0, cikCukurs / cukurs)
Acitroni = max(0, cikCitronu / citroni)
Amandeks = max(0, cikMandeks / Mandeks)
Akaneelis = max(0, cikKaneelis / kaneelis)

litri = min(Aabols, Acukurs, Acitroni, Amandeks, Akaneelis)

print("Ar šobrīd pieejamajām sastāvdaļām varēs uztaisīt:", litri, "l ievārijuma.")




print("------------Maksa par sastāvdaļām--------")
kopAbolu = aaboli - cikAbolu
print("Aboli maksās", max(0, kopAbolu) * cenaAbolu * cikL, "€")
kopCukurs = cukurs - cikCukurs

if kadsCukurs == "p":
    print("Cukurs maksās", max(0, kopCukurs) * cenaParCukura * cikL, "€")
elif kadsCukurs == "i":
    print("Cukurs maksās", max(0, kopCukurs) * 0.3 * cenaIevCukura * cikL, "€")


kopCitroni = citroni - cikCitronu
print("Citroni maksās", max(0, kopCitroni) * cenaCitronu * cikL, "€")
kopMandeks = Mandeks - cikMandeks
print("Mandeļu ekstraksts maksās", max(0, kopMandeks) * cenaMandeks * cikL, "€")
kopKaneelis = kaneelis - cikKaneelis
print("Kanēlis maksās", max(0, kopKaneelis) * cenaKaneelis * cikL, "€" )

