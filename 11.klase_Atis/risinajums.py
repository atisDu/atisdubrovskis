import csv

iedz_skaiti = []

def izveidot_csv():
    with open ("pilsetas.csv","w",encoding="utf8", newline='') as fails:
            #definē csv rakstītāju, prasa ievadu 5 iedz sk. un pilsētu nosaukumiem, tad pārbauda vai atbilst un ierkasta failā un iedz_sk sarakstā
            rakstnieks = csv.writer(fails)
            rakstnieks.writerow(["Pilsēta","Iedzīvotāju skaits"])
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

izveidot_csv()        