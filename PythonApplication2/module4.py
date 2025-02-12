#2Pinginaabrid 
nimi1 = input("Sisesta esimene nimi: ")
nimi2 = input("Sisesta teine nimi: ")

if nimi1.isalpha() and nimi2.isalpha():
    print(f"{nimi1} ja {nimi2} on täna pinginaabrid!")
else:
    print("Üks või mõlemad nimed ei koosne ainult tähtedest.")
