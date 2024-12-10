import csv
import operator

skoleni = []

try:
    with open("skoleni.csv",'r', encoding="utf8", newline='') as file:
        reader = csv.DictReader(file)
        for rinda in reader:
            skoleni.append(rinda)
            print(f"Vārds: {rinda['Vārds']}, Uzvārds: {rinda['Uzvārds']}, Vid. vērt. {rinda['Vid. vērtējums']}")
        sakartoti_skoleni = sorted(skoleni, key=lambda x:x[2])
        key=operator.itemgetter(2),
except FileNotFoundError:
    print("Fails neeksistē!")
    exit()

for i in range (0, len(skoleni)):
    print(f"{sakartoti_skoleni[i]}")

'''
try:
    with open("skoleni.csv",'w', encoding="utf8", newline='') as file:
        fieldnames = ["Vārds","Uzvārds","Vid. vērtējums"]
        rakstnieks = csv.DictWriter(file, fieldnames) 
        #rakstnieks.writeheader()
        #rakstnieks.writerows(skoleni)
except FileNotFoundError:
    print("Fails neeksistē!")
    exit()

for rinda in skoleni:
    print(f"{rinda['Vārds']} \n")
'''