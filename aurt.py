from Mymodule import *

salasõnad = loe_failist("Salasõnad.txt")
kasutajanimed = loe_failist("полный_путь_к_файлу/Kasutajad.txt")

while True:
    print(kasutajanimed)
    print(salasõnad)
    print("1 - registreerimine\n2 - autoriseerimine\n3 - nime või parooli muutmine\n4 - unustasite parooli taastamine\n5 - lõpetamine\n")

    vastus = int(input("Sisestage arv: "))

    if vastus == 1:
        print("Registreerimine")
        kasutajanimed, salasõnad = registreerimine(kasutajanimed, salasõnad)
    elif vastus == 2:
        print("Autoriseerimine")
        autoriseerimine(kasutajanimed, salasõnad)
    elif vastus == 3:
        print("Nime või parooli muutmine")
        vastus = input("Kas muudame nime, parooli või mõlemad: ")
        if vastus == "nimi":
            kasutajanimed = nimi_või_parooli_muutmine(kasutajanimed)
        elif vastus == "parool":
            salasõnad = nimi_või_parooli_muutmine(salasõnad)
        elif vastus == "mõlemad":
            print("Nimi muutmine: ")
            # Selle osa kood puudub, palun täiendage vastavalt vajadusele
    elif vastus == 4:
        print("Unustasite parooli, taastamine")
        unustatud_parooli_taastamine(salasõnad, kasutajanimed)
    elif vastus == 5:
        print("Lõpetamine")
        break
    else:
        print("Vale valik. Proovige uuesti.")
