from itertools import cycle

# naturāls skaitlis no 1 līdz N
# katrs citadaks
# sauc par labu ja dalās ar vismaz vienu no skaitļiem M1 vai M2

# Nosauc divus naturālus skaitļus ai un bi
# tad ir uzrakstiitais skaitlis z, un noņem visus žetonus, kas ir spēkā sakarībā ai <= z <= bi
#Spēles beigās vadītājam jāpasaka cik labo žetonu joprojām atrodas uz gaada

Skaitli = input().split(' ')
M1 = int(Skaitli[1])
M2 = int(Skaitli[2])

N = int(Skaitli[0])
if N > 10000:
    exit()


labie = []


for i in range(1, N + 1):
        mod1 = int(i%M1)
        mod2 = int(i%M2)
        if mod1 == 0 or mod2 == 0:
            labie.append(i)



while True:
    
    gajieni=+1
    if gajieni > 1000:
         exit
    
    ievade = input().split(' ')

    ai = int(ievade[0])
    bi = int(ievade[1])
    #z = range(ai,bi,1)
    z = [x for x in labie if not(ai<=x<=bi)]
    labie = z
    
    print(len(labie))
    #ai <= z <= bi
 



