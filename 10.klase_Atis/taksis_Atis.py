import os

cilveki = int(input("Cik pasažieru vajag aizvest? (maks. 3): "))
if cilveki > 3:
    print("Taksī nevar būt vairāk kā 3 pasažieri!")
    exit()
pulkstens = int(input("Cikos tu brauksi ar taksi? (ievadi veselās stundās, piem. 15:00 kā 5): "))
if pulkstens >= 21 and pulkstens <= 24 and pulkstens <= 6 and pulkstens >= 0:
    print("Tiks piemērots nakts tarifs!")
    laiks = "nakts"
else:
    laiks = "diena"
stavieta = input("Vai Jūs atrodaties stacijā un redzat, ka taksis ir stāvvietā? (n/j): ")
if stavieta == "j":
    print("Būs piemērota tikai nolīgšanas cena! = 2 eur")
    izsaukcena = 0
else:
    izsaukcena = 2.5
gaidisana = input("Ievadiet gaidīsanas laiku, veselās minūtēs: ")
gaidcena = gaidisana * 0.15
print("Gaidīšanas cena būs", gaidcena, "Eur.")
attalums = input("Cik tālu jābrauc?: ")
if laiks ==- "nakts":
    cenakm = 0.77
    attalcena = attalums * cenakm
elif laiks == "diena":
    cenakm = 0.37
    attalcena = attalums * cenakm
else:
    "Pulksteņa laiks ievadīts nepareizi!"
    exit()

os.system('cls')
print("Kopējās izmaksas\nNolīgšana: 2.00 Eur.\nIzsaukšana:", izsaukcena, "Eur.\nCena par gaidīšanu:", gaidcena, "Eur.\nCena par km:", cenakm, "Eur.\nCena par attālumu:", attalcena, "Eur.\nKopējā cena:", 2 + izsaukcena + gaidcena + attalcena )
