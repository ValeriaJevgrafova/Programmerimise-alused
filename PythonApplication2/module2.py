from random import *
#N�idis 1
arv=randint(0,10)
print(arv)
if arv>5:
    print("*************")
    print(f"Arv {arv} suurem kui 5")
    print("*************")
if arv>5: print(f"Arv {arv} suurem kui 5")

#N�idis 2
arv=randint(-10,10)
if arv>0:
    print("Positiivne")
else:
    print("Negatiivne") #viga!

if arv>0:
    print("Positiivne")
elif arv==0:
    print("0")
else:
    print("Negatiivne")

1 #Juku
# a.
nimi = input("Sisesta eesnimi: ")
if nimi == "Juku":
    print("L�hme Jukuga kinno.")

# b.
vanus = input("Sisesta oma vanus: ")

if vanus.isdigit():
    vanus = int(vanus)
    if vanus < 6:
        print("Tasuta pilet.")
    elif 6 <= vanus <= 14:
        print("Lastepilet.")
    elif 15 <= vanus <= 65:
        print("T�ispilet.")
    elif vanus > 65:
        print("Sooduspilet.")
    elif vanus < 0 or vanus > 100:
        print("Viga andmetes!")
else:
    print("Sisestatud vanus ei ole t�isarv!")