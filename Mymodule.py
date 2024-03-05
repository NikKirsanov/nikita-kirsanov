from string import punctuation

def registreerimine(kasutajad: list, paroolid: list) -> tuple:
    """tagastab kasutajad ja poroolid:
    :param list kasutajad: kasutaja järjendid
    :param list paroolid: parooli järjendid
    :rtype: tuple
    """
    while True:
        nimi = input("Mis on sinu nimi? ")
        if nimi not in kasutajad:
            while True:
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
                        break
                    else:
                        print("Nõrk salasõna")
                else:
                    print("Parool peab olema vähemalt 8 tähemärki pikk")
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
        nimi=input("Sisesta kasutajanimi: ")
        parool=input("Sisesta salasõna: ")
        p+=1
        if kasutajad.index(nimi)==paroolid.index(parool):
            print(f"Tere tulemast! {nimi}")
        else:
            print("Vale nimi või salasõna")
            if p==5:
                print("Proovi uuesti 10 sek pärast")
                for i in range(10):
                    sleep(1)
                    print(f"On jäänud {10-i} sek")
