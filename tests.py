


def funkcija(x):
    "ievadi x"
    if (x == 1):
        return 1
    else:
        return 0



def klumes(funkcija):
        klumes = 0
        while funkcija != 1:
            funkcija
            print("viens")
            if funkcija == 0:
                klumes = klumes + 1
            if klumes > 3:
                print("Pārsniegts mēģinājumu skaits!")
                exit()
        return False

klumes(funkcija(0))