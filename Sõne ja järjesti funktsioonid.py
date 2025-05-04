def list_operations():
    # Näide loendist
    fruits = ["õun", "banaan", "kiivi", "apelsin"]
    print("Algne puuviljade nimekiri:", fruits)

    # Elemendi lisamine loendi lõppu
    fruits.append("pirn")  # append lisab elemendi loendi lõppu
    print("Pärast 'pirn' lisamist:", fruits)

    # Loendi sorteerimine
    fruits.sort()  # sort järjestab loendi tähestikulises järjekorras
    print("Pärast sorteerimist:", fruits)

    # Elemendi eemaldamine
    fruits.remove("kiivi")  # remove eemaldab määratud elemendi
    print("Pärast 'kiivi' eemaldamist:", fruits)

    # Loendi pikkuse leidmine
    print("Puuviljade arv:", len(fruits))  # len tagastab loendi pikkuse


def string_operations():
    # Näide stringist
    text = "  Tere, kuidas läheb?  "
    print("Algne string:", repr(text))

    # Tühikute eemaldamine algusest ja lõpust
    trimmed = text.strip()  # strip eemaldab tühikud algusest ja lõpust
    print("Pärast strip():", repr(trimmed))

    # Väiketäheliseks muutmine
    lower_text = trimmed.lower()  # lower muudab stringi väiketähtedeks
    print("Pärast lower():", lower_text)

    # Sõna asendamine
    replaced = lower_text.replace("tere", "tsau")  # replace asendab alamstringi teisega
    print("Pärast sõna asendamist:", replaced)

    # Stringi jagamine sõnadeks
    words = replaced.split()  # split jagab stringi sõnadeks
    print("Pärast split():", words)


def main():
    while True:
        print("Menüü:")
        print("1 - Töö loenditega")
        print("2 - Töö stringidega")
        print("0 - Välju")

        choice = input("Vali tegevus: ")

        if choice == "1":
            list_operations()
        elif choice == "2":
            string_operations()
        elif choice == "0":
            print("Programmist väljutakse.")
            break
        else:
            print("Vale valik. Palun proovi uuesti.")

# Peaprogrammi käivitamine
main()