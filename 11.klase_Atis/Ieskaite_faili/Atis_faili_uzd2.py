import csv

iedz_skaiti = []
# 1. uzd
def izveidot_csv():
    with open ("pilsetas.csv","w",encoding="utf8", newline='') as fails:
            #definē csv rakstītāju, prasa ievadu 5 iedz sk. un pilsētu nosaukumiem, tad pārbauda vai atbilst un ierkasta failā un iedz_sk sarakstā
            rakstnieks = csv.writer(fails)
            rakstnieks.writerow(["Nosaukums","Iedzīvotāju skaits"])
            for i in range (1, 6):
                nosaukums = input(f"Ievadi {i}. pilsētas nosaukumu: ")
                try:
                    iedz_sk = int(input(f"Ievadi {i}. pilsētas iedzīvotāju skaitu: "))
                except ValueError:
                    print("Iedz. skaitam jābut veselam skaitlim!")
                    iedz_sk = int(input(f"Velreiz ievadi {i}. pilsētas iedzīvotāju skaitu: "))
                iedz_skaiti.append(iedz_sk)
                rakstnieks.writerow([nosaukums,iedz_sk])
            print("Pilsētas ir ierakstītas csv failā!")

# 2. uzd
def lasit_csv():
    try:
        with open ("pilsetas.csv","r",encoding="utf8", newline='') as fails:
            reader = csv.reader(fails)
            print("**************")
            #Izprintē visas rindas bez []
            for rinda in reader:
                print(*rinda)
                print("----------------")
    except FileNotFoundError:
        print("Fails neeksistē!")

# 3. uzd
def aprekina_iedz_sk():
    kop_iedz_sk = 0
    # Saskaita visus kopas elementus un izvada kopējo summu, gribēju nolasīt no  CSV faila, bet ar vārdnīcām nav tik viegli
    for e in iedz_skaiti:
        kop_iedz_sk = kop_iedz_sk + e
    print(f"Kopējais iedzīvotāju skaits pa visām pilsētam ir {kop_iedz_sk}")


izveidot_csv()
lasit_csv()
aprekina_iedz_sk()