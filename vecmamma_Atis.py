cenaAbolu = 0.79
cenaCukura = 1.44
cenaCitronu = 2.29 * 0.130
cenaMandeks = 0.042
cenaKaneelis = 0.43 / 20



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
    cikCitronu = float(input("Cik citronu jau ir? (gb): "))
vaiMandeks = input("Vai mājās jau ir Mandeļu ekstrakta? (n/j): ")
if vaiMandeks == "j":
    cikMandeks = float(input("Cik daudz mandeļu ekstrakta jau ir? (ml)"))
vaiKaneelis = input("Vai mājās jau ir kanēlis? (n/j): ")
if vaiKaneelis == "j":
    cikKaneelis = input("Cik daudz kanēļa jau ir? (g): ")

print("---------------------------------------")
print("3 kg āboli")
print("1 kg cukurs")
print("500 ml ūdens")
print("1 gb citrons")
print("5 ml mandeļu ekstrakts")
print("10g kanēlis")
print("---------------------------------------")
receptesIzveele = input("Vai vēlaties ievadīt savu recepti, vai izmantot šo? (n/j): ")




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
print(citroni, "gb citronu")
print(Mandeks, "ml mandeļu ekstrakta")
print(kaneelis, "g kanēļa")


print("------------Maksa par sastāvdaļām--------")
kopAbolu = aaboli - cikAbolu
print("Aboli maksās", max(0, kopAbolu) * cenaAbolu * cikL, "€")
kopCukurs = cukurs - cikCukurs
print("Cukurs maksās", max(0, kopCukurs) * cenaCukura * cikL, "€")
kopCitroni = citroni - cikCitronu
print("Citroni maksās", max(0, kopCitroni) * cenaCitronu * cikL, "€")
kopMandeks = Mandeks - cikMandeks
print("Mandeļu ekstraksts maksās", max(0, kopMandeks) * cenaMandeks * cikL, "€")
kopKaneelis = kaneelis - cikKaneelis
print("Kanēlis maksās", max(0, kopKaneelis) * cenaKaneelis * cikL, "€" )

