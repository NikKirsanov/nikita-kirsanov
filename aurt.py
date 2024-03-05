from Mymodule import *

salasõna=["Parrol "]
kasutajanimed=[]
while True:
    print("1-registreerimine\n2-auoriserimine\n3-nime või parooli muutmine\n4-unustanu parooli tastamine\n5-lõpetamine")
    vastus=input("Sisestage arv")
    if vastus==1:
        print("Registreerimine")
        kasutajanimed,salasõnad=registreerimine(kasutajanimed,salasõnad)
    elif vastus==2:
        print("Autoriserimine")
    elif vastus==3:
        print("nime või parooli muutmine")
    elif vastus==4:
        print("unustanud parooli taastamine")
    elif vastus==5:
        print("lõpetamine")
        break
    else:
        print("Tundmatu valik")