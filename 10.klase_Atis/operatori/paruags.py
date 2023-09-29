import random
a = 1
b = -10
d = 0

def funkcija():
    while a < 5:
        bac = random.randint(-100000,1000000)
        if bac == 2:
            print("brute", bac)

funkcija()