import random as random
import csv

saraksts = ["bolis", "Dole", "Kore"]

kopa = []

            

#uzd2 - nolasit tekstu no faila
def nolasit_failu():
        teksts = []
        try:
            with open("fails.txt",'r', encoding="utf8", newline='') as file:
                    saturs = (file.read())
                    file.close
                    print("Dati ielasīti!")
                    print(saturs)
        except FileNotFoundError:
            print(f"Fails {file} nav atrasts!")
        


def nolasit_ar_atstarpi():
        try:   
            with open("fails.txt",'r', encoding="utf8", newline='') as file:    
                kopa = file.readlines()
                kartots = sorted(kopa, reverse=True)
                print(kartots)
                file.close
        except FileNotFoundError:
                print(f"Fails nav atrasts!")
        try:   
            with open("fails.txt",'w', encoding="utf8", newline='') as file:    
            
                file.writelines(kartots)
                file.close
        except FileNotFoundError:
                print(f"Fails nav atrasts!")


def atrast():
    koatrast = input("Ievadi vārdu ko atrast: ")
    skaitamais = 0
    try:
        with open("fails.txt",'r', encoding="utf8", newline='') as file:    
                for i in file:
                        if i.strip() == koatrast.strip():
                            skaitamais = skaitamais+1
                if skaitamais == 0:
                    print(f"{koatrast.strip()} nav atrasts!")
                else:
                    print(f"{koatrast.strip()} atrasts {skaitamais} reizes!")
        file.close
    except FileNotFoundError:
        print("Fails no hablo!")


def ierakstit_faila():
        with open("fails.txt",'w', encoding="utf8", newline='') as file:
                    '''for ntais in range (1,7):
                        vards = input(f"Ievadi {ntais}. vārdu: ")
                        file.write(f"{vards}\n")
                    file.close
                    '''
                    for elementi in saraksts:
                        file.write(f"{elementi}\n")
                    print(f"Sarakstam pievienoti {len(saraksts)} elementi.")
                    file.close

#atrast()
#ievadiit vardu, ko meklet faila udn informeet vai ir


#ierakstit_faila()
#nolasit_ar_atstarpi()


#sakartot faila esosos datus dilstosaa seciiba
#Funkcija, kas izveido csv failu un ieraksta 30 rindiņas

def izveidot_csv():
    with open ("fails.csv","w",encoding="utf8", newline='') as fails:
            rakstnieks = csv.writer(fails) 
            rakstnieks.writerow(["ID","Vārds","Vecums"])
            rakstnieks.writerows([[1,"Alise",18],[2,"Jānis",28],[3,"Ance",35]])
            print("Fails ir izveidots!")

def lasit_csv():
    try:
        with open ("fails.csv","r",encoding="utf8", newline='') as fails:
            reader = csv.reader(fails)
            for rinda in reader:
                print(*rinda)
    except FileNotFoundError:
        print("Fails neeksistē!")

izveidot_csv()
lasit_csv()

#Pievienot jaunu id, vārdu, vecumu ar input

def pievienot_csv():
    with open ("fails.csv","a",encoding="utf8", newline='') as fails:
            rakstnieks = csv.writer(fails) 
            id = input("Ievadi id!: ")
            vards = input("Ievadi vārdu!: ")
            vecums = input("Ievadi vecumu!: ")

            rakstnieks.writerow([id,vards,vecums])
            print("Fails ir izveidots!")
pievienot_csv()