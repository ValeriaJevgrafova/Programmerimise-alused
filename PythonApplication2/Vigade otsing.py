while True:
    try:
        c = float(input("Sisesta ristküliku 2. külje pikkus => "))
        if c <= 0:
            print("Külje pikkus peab olema positiivne arv.")
            continue
        break
    except ValueError:
        print("Sisesta kehtiv arv.")

S = b * c
print("Ristküliku pindala:", S)
P = 2 * (b + c) 
print("Ristküliku ümbermõõt:", P)
di = math.sqrt(b ** 2 + c ** 2) 
print("Ristküliku diagonaal:", round(di, 2))

print()

print("Ringi karakteristikud")

while True:
    try:
        r = float(input('Sisesta ringi raadiusi pikkus => '))
        if r <= 0:
            print("Raadius peab olema positiivne arv.")
            continue
        break
    except ValueError:
        print("Sisesta kehtiv arv.")

d = 2 * r
print("Ringi läbimõõt:", d)

S = math.pi * r ** 2 
print("Ringi pindala:", round(S, 2))
C = 2 * math.pi * r
print("Ringjoone pikkus:", round(C, 2))
