skaitlis1 = int(input('Ievadiet skaitli1:'))
skaitlis2 = int(input('Ievadiet skaitli2:'))

if skaitlis1 > 10 and skaitlis2 > 10 and skaitlis1 < 25 and skaitlis2 < 25:
    print('Tev izdevās izpildīt uzdevumu!')
elif skaitlis1 > 10 or skaitlis2 > 10 and skaitlis1 < 25 or skaitlis2 < 25:
    print('Jāpielabo uzdevuma izpildee!')
else:
    print('Neizdevās izpildīt!')
