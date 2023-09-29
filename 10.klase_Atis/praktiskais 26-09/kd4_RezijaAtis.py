#Lieotājam jāievada skaitlis 1
skaitlis1 = int(input('Ievadiet skaitli1:'))
#Lieotājam jāievada skaitlis 2
skaitlis2 = int(input('Ievadiet skaitli2:'))

#Atkarībā no ievadītajiem skaitļiem izprintē
if skaitlis1 > skaitlis2:
    print("Starpība ir:",skaitlis1 - skaitlis2)
elif skaitlis1 < skaitlis2:
    print("Summa ir:", skaitlis1 + skaitlis2)
else:
    print('Abi skaitļi ir vienādi!')