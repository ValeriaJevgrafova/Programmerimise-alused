import random
import string

# Funktsioon parooli automaatseks genereerimiseks
def generate_password():
    str0 = ".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    str4 = str0 + str1 + str2 + str3
    ls = list(str4)
    random.shuffle(ls)
    psword = ''.join([random.choice(ls) for x in range(12)])
    return psword

# Funktsioon kasutaja parooli genereerimiseks, kui ta ise tahab
def salasona(k: int):
    sala = ""
    for i in range(k):
        t = random.choice(string.ascii_letters)  # Suured ja väikesed tähed
        num = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])  # Numbrid
        t_num = [t, str(num)]  # Täht ja number
        sala += random.choice(t_num)
    return sala

# Funktsioon, et kontrollida parooli kehtivust
def is_valid_password(password):
    if len(password) < 8:
        return False
    has_digit = any(char.isdigit() for char in password)
    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_special = any(char in ".,:;!_*-+()/#¤%&" for char in password)
    return has_digit and has_lower and has_upper and has_special

# Loendid sisselogimiste ja paroole jaoks
users = []
passwords = []

# Funktsioon registreerimiseks
def register():
    username = input("Sisesta uus kasutajanimi: ")
    
    if username in users:
        print("Kasutajanimi on juba olemas!")
        return
    
    choice = input("Kas soovid automaatset parooli genereerimist? (jah/ei): ").lower()
    
    if choice == "jah":
        password = generate_password()
        print(f"Automaatne parool: {password}")
    else:
        password = input("Sisesta oma parool: ")
        while not is_valid_password(password):
            print("Parool ei ole kehtiv! Parool peab sisaldama numbreid, suuri ja väikeseid tähti ning erimärke.")
            password = input("Sisesta oma parool: ")
    
    users.append(username)
    passwords.append(password)
    print("Kasutaja on edukalt registreeritud!")

# Funktsioon autoriseerimiseks
def authorize():
    username = input("Sisesta kasutajanimi: ")
    password = input("Sisesta parool: ")
    
    if username in users:
        user_index = users.index(username)
        if passwords[user_index] == password:
            print("Autoriseerimine õnnestus!")
        else:
            print("Vale parool!")
    else:
        print("Kasutajat ei leitud!")

# Funktsioon parooli muutmiseks
def change_password():
    username = input("Sisesta kasutajanimi, mille parooli soovid muuta: ")
    
    if username in users:
        new_password = input("Sisesta uus parool: ")
        while not is_valid_password(new_password):
            print("Parool ei ole kehtiv! Parool peab sisaldama numbreid, suuri ja väikeseid tähti ning erimärke.")
            new_password = input("Sisesta uus parool: ")
        
        user_index = users.index(username)
        passwords[user_index] = new_password
        print("Parool on edukalt muudetud!")
    else:
        print("Kasutajat ei leitud!")

# Funktsioon unustatud parooli taastamiseks
def forgot_password():
    username = input("Sisesta kasutajanimi, mille parooli unustasid: ")
    
    if username in users:
        user_index = users.index(username)
        print(f"Teie parool on: {passwords[user_index]}")
    else:
        print("Kasutajat ei leitud!")

# Põhiprogramm
def main():
    while True:
        print("\nVali tegevus:")
        print("1. Registreerimine")
        print("2. Autoriseerimine")
        print("3. Parooli muutmine")
        print("4. Unustasin parooli")
        print("5. Lõpetamine")
        
        choice = input("Valik: ")
        
        if choice == "1":
            register()
        elif choice == "2":
            authorize()
        elif choice == "3":
            change_password()
        elif choice == "4":
            forgot_password()
        elif choice == "5":
            print("Programm lõpeb.")
            break
        else:
            print("Vale valik! Palun proovi uuesti.")

if __name__ == "__main__":
    main()