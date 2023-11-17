import time;
#Importē laiku, lai varētu pagulēt

#Prasa ievadīt lietotājvārdu un paroli, kā arī apstājas ja kādā no laukiem tiek ievadīts stop, un pārbauda vai parole ir 5 rakstzīmes gara
lietotajs = input("Lūdzu, izdomā savu lietotājvārdu: ")
if lietotajs == "stop":
    print("Programmas beigas!")
    exit()
parole = input("Lūdzu, izdomā savu paroli: ")
if parole == "stop":
    print("Programmas beigas!")
    exit()
print("-------------------------------")

#Deklarē meģinajuma skaita mainīgo
checkmegi = 0

#Funkcija kas pārbauda lietotājvārdus un paroles, tāpāt arī skatās vai nav ierakstīts stop, un ja parole vai vards anv ievadīts pareizi, tad tiek pieskaitīts +1 mēģināums un kad tiek pārsniegti 5 mēģinājumi programma apstājas
def checks():
    #globālis, jo deklarētais iepriekš ir globālis, bet iekš funkcijā meklē lokāli ar tādu pašu nosaukumu
    global checkmegi

    chklietotajs = input("Ievadi lietotājvārdu:")
    if chklietotajs == "stop":
        print("Programmas beigas!")
        exit()
    chkparole = input("Ievadi paroli: ")
    if len(parole) == 5:
        print("Parolei ir jābūt 5 rakstzīmes garai!")
    if chkparole == "stop":
        print("Programmas beigas!")
        exit()
    #Pārbauda vai ievadītais sakrīt, ja nē, tad izpilda funkciju vēlreiz
    if parole != chkparole or lietotajs != chklietotajs:
        print("Lietotājvārds vai parole nepareiza!")
        time.sleep(1)
        checkmegi += 1
        print("Ir atlikuši vēl", 5 - checkmegi, "mēģinājumi!")
        if checkmegi > 4:
            print("Mēģinājumi beigušies!")
            exit()
        else:
            checks()
#izpilda augšējo
checks()
print("-------------------------------")
print("Pieslēgšanās veiksmīga!")
print("-------------------------------")
def checkpirmais():
    #globālis, jo deklarētais iepriekš ir globālis, bet iekš funkcijā meklē lokāli ar tādu pašu nosaukumu
    global pirmais
    pirmais = int(input("Ievadi 1. veselo skaitli: "))
    if pirmais < 0:
        print("Skaitlis nevar būt negatīvs!")
        checkpirmais()
#Izpilda augšējo
checkpirmais()

def checkotrais():
    #globālis, jo deklarētais iepriekš ir globālis, bet iekš funkcijā meklē lokāli ar tādu pašu nosaukumu
    global otrais
    otrais = int(input("ievadi 2. veselo skaitli: "))
    if otrais < 0:
        print("Skaitlis nevar būt negatīvs!")
        checkotrais()
#Izpilda augšējo
checkotrais()

#Čeko vai nav pirmais mazāks par otro
if pirmais > otrais:
    print("0")
    exit()

# sarēķina un izvada secīgo summu
summa = sum(range(pirmais, otrais))
print("-------------------------------")
print("Šo skaitļu secīgi pieaugošā summa būs:", summa)










