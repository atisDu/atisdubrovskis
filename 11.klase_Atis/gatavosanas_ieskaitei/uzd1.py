def ierakstit_faila():
    with open("fails.txt",'w', encoding="utf8", newline='') as file:
                vards = input("Ievadi tekstu: ")
                file.write(vards)
                file.close
                print("Dati ierakstīti!")
            

#uzd2 - nolasit tekstu no faila
def nolasit_failu():
    teksts = []
    with open("fails.txt",'r', encoding="utf8", newline='') as file:
        try:
                saturs = (file.read())
                file.close
                print("Dati ielasīti!")
                print(saturs)
        except FileNotFoundError:
            print(f"Fails {file} nav atrasts!")
nolasit_failu()