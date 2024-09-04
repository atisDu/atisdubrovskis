import math
# Visu iemet while cilpaa, lai ja nav nopirkts viss kas sarakstā, tad programma atkārtojas

while True:
    # ievadit preces daudzumu un izčeko vai ir zolīds skaitlis
    precesdaudz = int(input("Ievadi preces daudzumu (gb): "))
    if precesdaudz < 0:
        break

    # ievadit preces cenu un izčeko vai ir zolīds skaitlis

    precescena = float(input("Ievadi preces cenu (€): "))
    if precescena < 0:
        break

            # ievadit preces nosaukumu

    precesvards = input("ievadi preces nosaukumu: ")

    kopcena = precesdaudz * precescena
    vai = input("Vai ir nopirkts viss, kas sarakstā? (n/j): ")
    if vai == "n":
        break
    # čeks
    print("-----čeks------")
    # izbliež pamatvērtības, tka bez atlaidēm
    print(precesvards, "\nPreces dauduzms:", precesdaudz, "\nCena par vienu preci:", precescena, "\nPreces cena bez atlaides:", kopcena)
    print("--ar atlaidēm--")
    # tad ar atalaidem attiecigi, vel noapaplo lidz 2 cipariem aiz komata
    print("Ar 30% atlaidi:", round(kopcena - kopcena * 0.3, 2))
    #Izcheko vai ir karte, ja ir tad dod vel atlaides, un ari tas attiecig noapaplo un sarekina 
    karte = input("Vai tev ir karte? (n/j): ")
    if karte == "j":
        print("Ar 40% atlaidi, jo ir karte:", round(kopcena - kopcena * 0.4, 2))
        print("Ar 50% atlaidi, jo ir karte:", round(kopcena - kopcena * 0.5, 2))
    else:
        print("Ar 20% atlaidi, jo nav karte:", round(kopcena - kopcena * 0.2, 2))

        # tad ja vienads vai varak par 3 precem, tad pieskir vel atlaidiiti, vel noapaplo lidz 2 cipariem aiz komata
    if precesdaudz >= 3:
        print("Ar 30% atlaidi, jo ir 3 vai vairāk preces:", round(kopcena - kopcena * 0.4, 2))
    #Katra otra ir bezmaksas, to dabon, ja izdala daudzumu uz pusi un tad noapalao uz leju, un ari noapalo visu lidz 2 cipariem aiz komata
    print("Cena, ja katra otrā prece ir par brīvu:", round(math.floor(precesdaudz / 2) * precescena, 2))
    print("---------------")
    break
    #ja viss ir nopirkts tad beidz citadak turpina

