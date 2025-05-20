#1. uzdevums
def ierakstit_pilsetas():
        with open("pilsetas.txt",'w', encoding="utf8", newline='') as file:
                    #Prasa nosaukumus 10 pilsētām
                    for i in range (1, 11):
                        pilseta = input(f"Ievadi {i}. pilsētu: ")
                        #Ja ievadīta pilsēta ir tukša, tā tiek prasīta vēlreiz
                        if pilseta.strip() == "":
                            pilseta = input(f"Nederīgs nosaukums, vēlreiz ievadi {i}. pilsētu: ")
                        file.write(f"{pilseta}\n")
                    print(f"Failam pievienotas 10 pilsētas!")
                    file.close
# 2. uzdevums
def paradit_visu_saturu():
        try:   
            with open("fails.txt",'r', encoding="utf8", newline='') as file:    
                #Katram elementam (rindiņai) failā izmanto strip() metodi un izprintē to jaunā līnijā
                for i in file:
                    print(i.strip())
                print("--------------")
                file.close

        except FileNotFoundError:
                print(f"Fails nav atrasts!")

# 3. uzdevums
def paradit_pilsetas_un_kartot():
        pilsetas = []
        try:   
            #Izvada katru rindu bez tukšumiem, pievieno to sarakstam
            with open("pilsetas.txt",'r', encoding="utf8", newline='') as file:    
                for i in file:
                    o = i.strip()
                    print(o)
                    pilsetas.append(o)
                #Sakārto pilsētas alfabēta secībā
                kartots = sorted(pilsetas)
                print(kartots)
                file.close
        except FileNotFoundError:
                print(f"Fails nav atrasts!")

# 4. uzdevums
def ierakstit_un_parbaudit_pilsetas():
        with open("pilsetas.txt",'a+', encoding="utf8", newline='') as file:
                    ievaditas = []
                    #Prasa ievadi 3 pilsētām
                    for i in range (1, 4):
                        pilseta = input(f"Ievadi {i}. pilsētu: ")
                        #Katrai ievadei pārbaude vai faila jau neeksistē tā un ja eksistē prasa lietotājam elreiz ievadīt datus
                        for x in ievaditas:
                            if x.strip() == pilseta.strip():
                                print("Pilsēta jau eksistē!")
                                pilseta = input(f"Vēlreiz ievadi {i}. pilsētu: ")
                        ievaditas.append(pilseta)
                    print(f"Ievadītas {len(ievaditas)} pilsētas:\n{ievaditas}")                        
                    file.close

ierakstit_pilsetas()
paradit_visu_saturu()
paradit_pilsetas_un_kartot()
ierakstit_un_parbaudit_pilsetas()
