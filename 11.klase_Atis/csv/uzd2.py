import csv

csv_file='darbinieki.csv'

darbinieki=[
    {"Vārds":"Anna",'Amats':'Skurstenslauķis','Alga':'900'},
    {"Vārds":"Jānis",'Amats':'Aukle','Alga':'50000'},
    {"Vārds":"Zigfrīds",'Amats':'Ģītārists','Alga':'-2'},
    {"Vārds":"Bolis",'Amats':'Polis','Alga':'gh'}
]

with open(csv_file,'w', encoding="utf8", newline='') as file:
        fieldnames = ["Vārds","Amats","Alga"]
        rakstnieks = csv.DictWriter(file, fieldnames) 
        rakstnieks.writeheader()
        rakstnieks.writerows(darbinieki)

try:
    with open(csv_file, "r", encoding="utf8", newline='') as file:
        reader = csv.DictReader(file)
        for rinda in reader:
            try:
                if int(rinda["Alga"]) < 0 or rinda["Alga"].isdigit() == "False" and int(rinda["Alga"] > 1000): 
                    print(f"rindā alga nav derīgs skaitlis! Nederīgā alga; {rinda['Alga']}.")
                else:
                    print(f"Vārds: {rinda['Vārds']}, Amats: {rinda['Amats']}, Alga: {rinda['Alga']}")
            except ValueError:
                print(f"Kļūda! Nederīga vērtība!")
except FileNotFoundError:
    print(f"Fails {csv_file} neeksistē!")
    exit()
    
#parbaudit vai alga ir ielikts ka skaitlis derigs
#ja nav tad bridinajumu
#ja fails darbinieki.csv neeksistē, tad izdrukāt kļūdu

#uzd3 - jaunā failā
#no faila skoleni.csv noteikt kurs skolens ieguvis visaugstaako
# vidējo vērtējumu, parādīt skolēna vārdu un vertējumu