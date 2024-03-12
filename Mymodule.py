from string import punctuation, ascii_lowercase, ascii_uppercase, digits
from time import sleep
from os import path, remove

def registreerimine(kasutajad:list, paroolid:list) -> tuple:
    """
    Registreerib uue kasutaja.
    :param list kasutajad: Olemasolevate kasutajate nimekiri.
    :param list paroolid: Olemasolevate paroolide nimekiri.
    :rtype: tuple
    """
    while True:
        nimi = input("Mis on sinu nimi? ")
        if nimi not in kasutajad:
            while True:
                parool = input("Mis on sinu parool? ")
                if len(parool) >= 8 and any(c in punctuation for c in parool) \
                    and any(c in ascii_lowercase for c in parool) \
                    and any(c in ascii_uppercase for c in parool) \
                    and any(c in digits for c in parool):
                    kasutajad.append(nimi)
                    paroolid.append(parool)
                    break
                else:
                    print("Nõrk salasõna!")
            break
        else:
            print("Selline kasutaja on juba olemas!")
    return kasutajad, paroolid

def autoriseerimine(kasutajad:list, paroolid:list):
    """
    Autoriseerib kasutaja.
    """
    p = 0
    while True:
        nimi = input("Sisesta kasutajanimi: ")              
        if nimi in kasutajad:            
            while True:
                parool = input("Sisesta salasõna: ")
                p += 1
                try:
                    if kasutajad.index(nimi) == paroolid.index(parool):
                        print(f"Tere tulemast! {nimi}")
                        return
                except ValueError:
                    print("Vale nimi või salasõna!")
                    if p == 5: 
                        print("Proovi uuesti 10 sekundi pärast")
                        for i in range(10):
                            sleep(1)
                            print(f"On jäänud {10 - i} sekundit")
        else:
            print("Kasutajat pole")

def muuda_kasutaja_info(järjend: list) -> list:
    """
    Muudab kasutaja nime või parooli.
    """
    muutuja = input("Vana nimi või parool: ")
    if muutuja in järjend:
        indeks = järjend.index(muutuja)
        uus_muutuja = input("Uus nimi või parool: ")
        järjend[indeks] = uus_muutuja
    return järjend

def loe_failist(fail: str) -> list:
    """
    Loeb teksti failist.
    """
    järjend = []
    try:
        with open(fail, 'r', encoding="utf-8") as f:
            järjend = f.readlines()
    except FileNotFoundError:
        print(f"Faili {fail} ei leitud.")
    return [x.strip() for x in järjend]

def kirjuta_failisse(fail: str):
    """
    Salvestab teksti failisse.
    """
    n = int(input("Mitu sõna soovid lisada: "))
    sõnad = [input(f"{i+1}. sõna: ") for i in range(n)]
    with open(fail, 'w', encoding="utf-8") as f:
        f.write("\n".join(sõnad))

def ümber_kirjuta_fail(fail: str):
    """
    Ümberkirjutab teksti failisse.
    """
    tekst = input("Sisesta tekst: ")
    with open(fail, 'w', encoding="utf-8") as f:
        f.write(tekst)

def faili_kustutamine():
    """
    Kustutab faili.
    """
    failinimi = input("Mis faili soovid kustutada? ")
    if path.isfile(failinimi):
        remove(failinimi)
        print(f"Fail {failinimi} on kustutatud.")
    else:
        print(f"Faili {failinimi} ei leitud.")

def main():
    """
    Main funktsioon.
    """
    salasõnad = loe_failist("Salasõnad.txt")
    kasutajanimed = loe_failist("Kasutajad.txt")

    while True:
        print(kasutajanimed)
        print(salasõnad)
        print("1 - Registreerimine\n2 - Autoriseerimine\n3 - Nime või parooli muutmine\n"
              "4 - Unustasid parooli taastamine\n5 - Lõpetamine\n")
        vastus = input("Sisestage arv: ")

        if vastus == "1":
            print("Registreerimine")
            kasutajanimed, salasõnad = registreerimine(kasutajanimed, salasõnad)
        elif vastus == "2":
            print("Autoriseerimine")
            autoriseerimine(kasutajanimed, salasõnad)
        elif vastus == "3":
            print("Nime või parooli muutmine")
            vastus = input("Kas muudame nime, parooli või mõlemad: ")
            if vastus == "nimi":
                kasutajanimed = muuda_kasutaja_info(kasutajanimed)
            elif vastus == "parool":
                salasõnad = muuda_kasutaja_info(salasõnad)
            elif vastus == "mõlemad":
                print("Nime muutmine: ")
                kasutajanimed = muuda_kasutaja_info(kasutajanimed)
                print("Parooli muutmine: ")
                salasõnad = muuda_kasutaja_info(salasõnad)
        elif vastus == "4":
            print("Unustasid parooli taastamine")
        elif vastus == "5":
            print("Lõpetamine")
            break
        else:
            print("Tundmatu valik")

if __name__ == "__main__":
    main()
