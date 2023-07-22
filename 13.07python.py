# class kitob:
#     def __init__(self, nomi, muallifi, narxi, nashriyoti):
#         self.nomi=nomi
#         self.muallifi=muallifi
#         self.narxi=narxi
#         self.nashriyot=nashriyoti

#     def info(self):
#         print(f"""
# Kitob nomi:    {self.nomi}
# Kitob muallifi:{self.muallifi}
# Kitob narxi:   {self.narxi}
# Nashriyot:     {self.nashriyot}
# """)
# k1=kitob("Tubanlik","Aniod Bax",76000,"Chegirma")
# k2=kitob("Yer ostiga sayohat","Genrix",35000,"Nur")
# k3=kitob("Zilzila daxshati","Mark Quiston",100000,"Osiyo")
# k4=kitob("Turklar haqiqati","Esma Turk",120000,"Emran")
# k5=kitob("Samodaki jang","Tomas Klark",86000,"Urban")


# lst=[]
# for i in (k1, k2, k3, k4, k5):
#     if 'A'<=i.nashriyot[0]<='H':
#         print(kitob.info(i))

##--------------------------------------------

class Kompyuter:
    def __init__(self, nomi, rami, narxi, protsessori):
        self.nom=nomi
        self.ram=rami
        self.narx=narxi
        self.pr=protsessori
    def info(self):
        return f"""Kompyuter nomi:        {self.nom}
Kompyuter rami:        {self.ram}
Kompyuter narxi:      ${self.narx}
Kompyuter protsessori: {self.pr}"""
    
kom1=Kompyuter('Aser', 12, 1100, 'Intel Core i3')
kom2=Kompyuter('Lenova', 16, 1260, 'AMD FX-8320')
kom3=Kompyuter('Samsung', 8, 1000, 'Intel Core i2')
kom4=Kompyuter('Redmi', 4, 1310, 'Intel Core i5')

for i in (kom1, kom2, kom3, kom4):
    if 4<i.ram<16:
        print(Kompyuter.info(i))

