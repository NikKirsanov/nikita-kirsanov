from Mymodule import *

salasõnad = []
kasutajad = []

while True:
    print("1-registreerimine\n2-auoriserimine\n3-nime või parooli muutmine\n4-unustanu parooli tastamine\n5-lõpetamine")
    vastus = input("Sisestage arv: ")

    if vastus == '1':
        print("Registreerimine")
        kasutajad, salasõnad = registreerimine(kasutajad, salasõnad)
    elif vastus == '2':
        print("Autoriseerimine")
        autoriseerimine(kasutajad, salasõnad)
    elif vastus == '3':
        print("Nime või parooli muutmine")
        vastus = input("Kas muudame nime või parooli: ")
        
        if vastus == "nimi":
            kasutajad = nimi_või_parooli_muutmine(kasutajad)
        elif vastus == "parool":
            unustatud_parooli_taastamine(salasõnad, kasutajad)
        else:
            print("Vale valik!")

    elif vastus == '4':
        print("Unustanud parooli taastamine")
        unustatud_parooli_taastamine(salasõnad, kasutajad)

    elif vastus == '5':
        print("Lõpetamine")
        break

    else:
        print("Tundmatu valik")
