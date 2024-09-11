vardi = ["Šausmīgi", "Bēdīgi","Vāji","Gandrīz vāji","Viduvēji","Gandrīz labi","Labi","Ļoti labi","Teicami","Izcili"]


def galvena():
    while True:
        try: 
            rez = float(input("Ievadi testa rezultātu (0-100): "))
            if rez >= 0 and rez <= 100:
                if rez <= 10:
                    atzime = 1
                elif rez <= 20:
                    atzime = 2
                elif rez <= 30:
                     atzime = 3
                elif rez <= 40:
                    atzime = 4
                elif rez <=53:
                    atzime = 5
                elif rez <= 66:
                    atzime = 6
                elif rez <= 76:
                    atzime = 7
                elif rez <= 86:
                    atzime = 8
                elif rez <= 94:
                    atzime = 9
                elif rez <= 100:
                    atzime = 10
                vardiski = vardi[atzime-1]
                print(f"Rezultāts: {round(rez,2)}% - {vardiski} (atzīme: {atzime})")
            else:
                print("Ievadi skaitli 1-100.")
        except ValueError:
            print("Nederīga ievade: Lūdzu ievadiet skaitli.")
    
galvena()
