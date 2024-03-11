from string import punctuation
from time import sleep
import random

def registreerimine(kasutajad: list, paroolid: list) -> tuple:
    """Tagastab kasutajad ja paroolid:
    :param list kasutajad: kasutaja järjendid
    :param list paroolid: parooli järjendid
    :rtype: tuple
    """
    while True:
        nimi = input("Mis on sinu nimi? ")
        if nimi not in kasutajad:
            while True:
                valik = input("Kas soovid luua parooli ise (sisesta 'ise') või lasta seda genereerida (sisesta 'genereeri')? ")
                if valik.lower() == "ise":
                    parool = input("Mis on sinu parool? ")
                    flag_p = False
                    flag_l = False
                    flag_u = False
                    flag_d = False
                    
                    if len(parool) >= 8:
                        parool_list = list(parool)
                        for p in parool_list:
                            if p in punctuation:
                                flag_p = True
                            elif p.islower():
                                flag_l = True
                            elif p.isupper():
                                flag_u = True
                            elif p.isdigit():
                                flag_d = True
                                
                        if flag_p and flag_l and flag_u and flag_d:
                            kasutajad.append(nimi)
                            paroolid.append(parool)
                            print("Kasutaja edukalt registreeritud!")
                            break
                        else:
                            print("Nõrk salasõna")
                    else:
                        print("Parool peab olema vähemalt 8 tähemärki pikk")
                elif valik.lower() == "genereeri":
                    parool = generate_password()
                    kasutajad.append(nimi)
                    paroolid.append(parool)
                    print("Kasutaja edukalt registreeritud! Genereeritud parool:", parool)
                    break
                else:
                    print("Vale valik, proovi uuesti!")
            break
        else:
            print("Selline kasutaja on juba olemas!")

    return kasutajad, paroolid

def autoriseerimine(kasutajad:list,paroolid:list):
    """Funktsioon kuvab ekraanile "Tere tulemas!" kui kasutaja on olemas nimekirjas
        Nimi on järjendis kasutajad
        Salasõna on paroolide järjendis
        Nimi ja salasõna indeksid on võrdsed
    param list kasutajad:...
    param list paroolid:...
    """
    p=0
    while True:
        nimi = input("Sisesta kasutajanimi: ")
        
        if nimi in kasutajad:
            parool = input("Sisesta salasõna: ")
            p += 1
            try:
                if kasutajad.index(nimi) == paroolid.index(parool):
                    print(f"Tere tulemast! {nimi}")
                    break
            except:
                print("Vale nimi või salasõna!")
                if p == 5:
                    print("Proovi uuesti 10 sek pärast")
                    for i in range(10):
                        sleep(1)
                        print(f"On jäänud {10-i-1} sek")
                else:
                    print("Kasutajat pole")

def nimi_või_parooli_muutmine(kasutajad: list) -> list:
    """Funktsioon võimaldab kasutajal muuta oma kasutajanime või parooli
    :param list kasutajad: kasutaja järjendid
    :rtype: list
    """
    while True:
        nimi = input("Mis on sinu kasutajanimi? ")
        if nimi in kasutajad:
            uus_nimi = input("Sisesta uus kasutajanimi: ")
            if uus_nimi not in kasutajad:
                kasutajad[kasutajad.index(nimi)] = uus_nimi
                print("Kasutajanimi edukalt muudetud!")
                break
            else:
                print("Selline kasutajanimi on juba olemas, vali mõni teine!")
        else:
            print("Sellist kasutajat ei leitud, proovi uuesti!")
    return kasutajad

def unustatud_parooli_taastamine(paroolid: list, kasutajad: list) -> None:
    """Funktsioon võimaldab kasutajal unustatud parooli taastada
    :param list paroolid: parooli järjendid
    :param list kasutajad: kasutaja järjendid
    """
    while True:
        nimi = input("Mis on sinu kasutajanimi? ")
        if nimi in kasutajad:
            print("Sinu parool on:", paroolid[kasutajad.index(nimi)])
            break
        else:
            print("Sellist kasutajat ei leitud, proovi uuesti!")

def generate_password():
    """Funktsioon genereerib juhusliku tugeva parooli
    :rtype: str
    """
    password = ''
    for _ in range(12):
        password += str(random.randint(0, 9))
    return password

def loe_failist(fail: str) -> list:
    järjend = []

    with open(fail, 'r', encoding="utf-8") as f:


        for rida in f:
            järjend.append(rida.strip())

    return järjend
