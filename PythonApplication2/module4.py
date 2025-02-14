#2Pinginaabrid 
nimi1 = input("Sisesta esimene nimi: ")
nimi2 = input("Sisesta teine nimi: ")

if nimi1.isalpha() and nimi2.isalpha():
    print(f"{nimi1} ja {nimi2} on täna pinginaabrid!")
else:
    print("Üks vői mőlemad nimed ei koosne ainult tähtedest.")

#3Remont
pikkus = float(input("Sisesta toa pikkus (m): "))
laius = float(input("Sisesta toa laius (m): "))

pindala = pikkus * laius
print(f"Põranda pindala on: {pindala} m²")

remont = input("Kas soovid teha remonti? (jah/ei): ").lower()

if remont == "jah":
    hind_per_m2 = float(input("Kui palju maksab ruutmeeter (EUR): "))
    kokku = pindala * hind_per_m2
    print(f"Põranda vahetamise hind on: {kokku} EUR")

#4Allahindus
alghind = float(input("Sisesta toote alghind (EUR): "))

if alghind > 700:
    soodustus = alghind * 0.30
    uus_hind = alghind - soodustus
    print(f"30% soodustus! Uus hind on: {uus_hind} EUR")
else:
    print(f"Alghind on väiksem kui 700 EUR, seega soodustust ei rakendata.")

#5Temperatuur
temperatuur = float(input("Sisesta temperatuur (°C): "))

if temperatuur > 18:
    print("Temperatuur on üle 18 kraadi, toasoojus on hea!")
else:
    print("Temperatuur on madalam kui 18 kraadi, toasoojus on liiga madal.")

#6Pikkus
pikkus = float(input("Sisesta oma pikkus (cm): "))

if pikkus < 160:
    print("Oled lühike.")
elif 160 <= pikkus <= 180:
    print("Oled keskmine.")
else:
    print("Oled pikk.")

#7Pikkus ja sugu
pikkus = float(input("Sisesta oma pikkus (cm): "))
sugu = input("Sisesta oma sugu (mees/naine): ").lower()

if sugu == "mees":
    if pikkus < 170:
        print("Oled lühike mees.")
    elif 170 <= pikkus <= 185:
        print("Oled keskmine mees.")
    else:
        print("Oled pikk mees.")
else:
    if pikkus < 160:
        print("Oled lühike naine.")
    elif 160 <= pikkus <= 175:
        print("Oled keskmine naine.")
    else:
        print("Oled pikk naine.")

#8Poes
import random

tooted = {
    "piim": 1.5,
    "sai": 0.8,
    "leib": 1.0
}

ostud = {}
total_price = 0

while True:
    toode = input("Mida soovid osta (piim/sai/leib)? Kui lõpetada, kirjuta 'lõpeta': ").lower()
    if toode == 'lõpeta':
        break
    elif toode in tooted:
        kogus = int(input(f"Kui palju {toode} tahad osta? "))
        hind = tooted[toode] * kogus
        ostud[toode] = (kogus, hind)
        total_price += hind
    else:
        print("Toode ei ole saadaval.")
        
print("\nTšekk:")
for toode, (kogus, hind) in ostud.items():
    print(f"{toode.capitalize()}: {kogus} tk - {hind:.2f} EUR")

print(f"Kokku: {total_price:.2f} EUR")

#9Ruut
külg1 = float(input("Sisesta ruudu külg 1 (cm): "))
külg2 = float(input("Sisesta ruudu külg 2 (cm): "))

if külg1 == külg2:
    print("See on ruut.")
else:
    print("See ei ole ruut.")

#10Matemaatika
arv1 = float(input("Sisesta esimene arv: "))
arv2 = float(input("Sisesta teine arv: "))
tehe = input("Vali tehe (+, -, *, /): ")

if tehe == "+":
    print(f"Tulemus: {arv1 + arv2}")
elif tehe == "-":
    print(f"Tulemus: {arv1 - arv2}")
elif tehe == "*":
    print(f"Tulemus: {arv1 * arv2}")
elif tehe == "/":
    if arv2 != 0:
        print(f"Tulemus: {arv1 / arv2}")
    else:
        print("Jagamine nulliga ei ole lubatud!")
else:
    print("Vale tehe!")

#11Juubel
sünnipäev = int(input("Sisesta oma sünnipäev (aasta): "))

if sünnipäev % 10 == 0:
    print("Sul on juubel!")
else:
    print("Sul ei ole juubelit.")

#12Müük
hind = float(input("Sisesta toote hind (EUR): "))

if hind <= 10:
    soodustus = hind * 0.10
    lõpphind = hind - soodustus
    print(f"Toote lõpphind koos 10% soodustusega: {lõpphind} EUR")
else:
    soodustus = hind * 0.20
    lõpphind = hind - soodustus
    print(f"Toote lõpphind koos 20% soodustusega: {lõpphind} EUR")

#13Jalgpalli meeskond
vanus = int(input("Sisesta oma vanus: "))
sugu = input("Sisesta oma sugu (mees/naine): ").lower()

if sugu == "mees" and 16 <= vanus <= 18:
    print("Sobid jalgpallimeeskonda.")
elif sugu == "naine":
    print("Meeskonda saavad kandideerida ainult mehed.")
else:
    print("Sa ei sobi jalgpallimeeskonda.")

#14Busside logistika
inimesed = int(input("Sisesta inimeste arv: "))
bussi_suurus = int(input("Sisesta bussi suurus (kohtade arv): "))

busside_arv = inimesed // bussi_suurus
viimases_bussis = inimesed % bussi_suurus

if viimases_bussis > 0:
    busside_arv += 1

print(f"Vajalik busside arv: {busside_arv}, viimases bussis on {viimases_bussis} inimest.")
