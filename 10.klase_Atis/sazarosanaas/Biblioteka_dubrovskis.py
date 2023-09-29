
#zurnals vai gramata

# pieprasit vai ne

#vai esi nodevis

# Gramnatas kas nav piepraiitas uz 30 dienaam perosnaalamn, 15 studentiem
#Visas publikaacijas kas ir pieprasiitas izsniedz uz 3 dienam
# žurnālus kas nav pieprasiiti isnieez uz 10 deian,
# Kas ir nepaklausiigi nedod ne grasi
vaiEsiNepaklausigs = input("Vai pie tevis atrodas kāds laikā nenodots izdevums? [nē/jā]: ")
if vaiEsiNepaklausigs == "j":
    print("Grāmata netiek izsniegta")
    

pieprasijums = input("Vai publikācija ir pieprasīto uzdevumu sarakstā? [nē/jā]: ")
if pieprasijums == "j":
    print("Publikāciju izsniedz uz 3 dienām.")

veids = input("Vai publikācija ir grāmata? [nē/jā]:")
StuPers = input("Vai tu esi perosnāls? [nē/jā]: ")
if veids == "j" and StuPers == "j":
    print("Grāmatu izsniedz uz 30 dienām") 
elif veids == "j" and StuPers == "n":
    print("Grāmatu izsniedz uz 15 dienām")
else:
    print("grāmatu izsniedz uz 10 dienām")
