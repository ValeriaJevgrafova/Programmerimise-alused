
#"�lesanne1"
from datetime import *
tana=date.today()
print(f"Tere! T�na on {tana}")

# 27/12/2022
tana = tana.strftime("%d/%m/%Y")
print(f"Tere! T�na on {tana}")

# # December 27, 2022
# tana = tana.strftime("%B %d, %Y")
# print(f"Tere! T�na on {tana}")

# # 12/27/22
# tana = tana.strftime("%m/%d/%y")

# # Dec-27-2022
# tana = taba.strftime("%b-%d-%Y")
from datetime import *
from calendar import *
tana=date.today()
print(f"Tere! T�na on {tana}")

# 27/12/2022
tana_ = tana.strftime("%d/%m/%Y")
print(f"Tere! T�na on {tana_}")
paevadekogus=monthrange(2025,1)[1]
print(f"Jaanuaris on {paevadekogus} p�eva")
p�evad=tana.day
onj��nud=paevadekogus-p�evadprint(f"Jaanuaris on j��nud {onj��nud} p�eva")
aastal�puni
print(f"Aasta l�puni on j��nud {}")

#"�lesanne2"
print("3 + 8 / (4 - 2) * 4 =", 3 + 8 / (4 - 2) * 4)
print("3 + 8 / 4 - 2 * 4 =", 3 + 8 / 4 - 2 * 4)

#"�lesanne3"b
import math

R = float(input("Sisesta ringi raadius R: "))

square_area = (2 * R) ** 2  
square_perimeter = 4 * (2 * R)  
circle_area = math.pi * R ** 2 
circle_circumference = 2 * math.pi * R 

print(f"Ruudu pindala: {square_area}")
print(f"Ruudu �mberm��t: {square_perimeter}")
print(f"Ringi pindala: {circle_area}")
print(f"Ringi �mberm��t: {circle_circumference}")

#"�lesanne4"

import math

earth_radius_km = 6378  
coin_diameter_cm = 25.75  
coin_diameter_m = coin_diameter_cm / 100 
earth_circumference_km = 2 * math.pi * earth_radius_km
earth_circumference_m = earth_circumference_km * 1000
num_coins = earth_circumference_m / coin_diameter_m

print(f"Maa �mberm��t ekvaatori kohal on {earth_circumference_km} km.")
print(f"�mber Maa l�heb {num_coins:.0f} 2-euroset m�nti.")

#"�lesanne5"
# kill-koll kill-koll
# killadi-koll
# kill-koll kill-koll
# killadi-koll
# kill-koll kill-koll kill-koll kill-koll 
a="kill-koll".capitalize()
b="killadi-koll".capitalize()
print(a*2,b,a*2,b,a*4)

#"�lesanne6"
# Rong see s�itis tsuhh tsuhh tsuhh,
# piilupart oli rongijuht.
# Rattad tegid rat tat taa,
# rat tat taa ja tat tat taa.
# Aga seal rongi peal,
# kas sa tead, kes olid seal?
# Rong see s�itis tuut tuut tuut,
# piilupart oli rongijuht.
# Rattad tegid kill koll koll,
# kill koll koll ja kill koll kill.

for line in song_lines:
    print(line.upper())

#"�lesanne 7"
try:
    a=float(input("A: "))
    b=float(input("B: "))
    if a>0 and b>0:
        print("Pindala ja �mberm��du rvutamine: ")
        S=a*b
        P=(a+b)*2
        print(f"S={S}, P={P}")
    else:
        print("Arvud peavad suurem kui 0 olla!")
except:
    print("Vale andmed!")

#"�lesanne8"
fuel = float(input("Sisesta tangitud k�tuse kogus liitrites: "))
distance = float(input("Sisesta l�bitud kilomeetrid: "))

fuel_consumption = (fuel / distance) * 100
print(f"K�tusekulu 100 km kohta on: {fuel_consumption:.2f} liitrit.")

#"�lesanne9"
speed = 29.9 
minutes = float(input("Sisesta minutid: "))
distance = speed * (minutes / 60) 
print(f"Rulluisutaja j�uab {distance:.2f} km {minutes} minutiga.")

#"�lesanne10"
minutes = int(input("Sisesta aeg minutites: "))

hours = minutes // 60
remaining_minutes = minutes % 60

print(f"{minutes} minutit on {hours}:{remaining_minutes:02d}.")