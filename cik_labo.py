
from itertools import cycle
# naturāls skaitlis no 1 līdz N
# katrs citadaks
# sauc par labu ja dalās ar vismaz vienu no skaitļiem M1 vai M2

# Nosauc divus naturālus skaitļus ai un bi
# tad ir uzrakstiitais skaitlis z, un noņem visus žetonus, kas ir spēkā sakarībā ai <= z <= bi
#Spēles beigās vadītājam jāpasaka cik labo žetonu joprojām atrodas uz gaada

Skaitli = input().split(' ')
M1 = int(input("Ievadi 1. naturālo skaitli: "))
M2 = int(input("Ievadi 2. naturālo skaitli "))

N = int(input("Cik žetoni?"))

labie = []


for i in range(1, N + 1):
        mod1 = int(i%M1)
        mod2 = int(i%M2)
        if mod1 == 0 or mod2 == 0:
            labie.append(i)


Ngarums = len(labie)
print(labie)
print(Ngarums)

while True:
    
    gajieni=+1

    myIterator = cycle((1,2))
    karta = next(myIterator)
    
    print("--------------------------------")
    print("Ir", karta, ". spēlētāja gājiens")
    print("--------------------------------")

    ai = int(input("Ievadi ai naturālo skaitli: "))
    bi = int(input("Ievadi bi naturālo skaitli "))
    #z = range(ai,bi,1)
    z = [x for x in labie if not(ai<=x<=bi)]
    labie = z
    
    print("Labie ir:",labie)
    print("Gājienu skaits: ", gajieni)
    if labie == []:
         print("-------------------------------------------")
         print("Spēles beigas!")
         print("Beidzamais bija", karta, ". spēlētāja gājiens.")
         print("Kopējais gājienu skaits:", gajieni)
         print("-------------------------------------------")
    #ai <= z <= bi
 



