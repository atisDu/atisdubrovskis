from itertools import cycle

# naturāls skaitlis no 1 līdz N
# katrs citadaks
# sauc par labu ja dalās ar vismaz vienu no skaitļiem M1 vai M2

# Nosauc divus naturālus skaitļus ai un bi
# tad ir uzrakstiitais skaitlis z, un noņem visus žetonus, kas ir spēkā sakarībā ai <= z <= bi
#Spēles beigās vadītājam jāpasaka cik labo žetonu joprojām atrodas uz gaada

while True:
    
    
    myIterator = cycle(range(2))
    

    print("Ir", next(myIterator), ". spēlētāja gājiens")


    M1 = int(input("Ievadi 1. naturālo skaitli:"))
    M2 = int(input("Ievadi 2. naturālo skaitli "))

    N = int(input("Cik žetoni?"))

    labie = []

    for i in range(1, N + 1):
        if M1%i == 0 or M2%i == 0:
            labie.append(i)


    Ngarums = len()
