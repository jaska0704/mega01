import os
# student = {
#     'ism': '',
#     'familiyasi': '',
#     'yosh': ''
# }
# lst = []
# for i in range(int(input("Nechta studentni kirgizasiz: "))):
#     lst.append(student.copy())
#     for j in lst[i]:
#         if isinstance(lst[i][j], int):
#             lst[i][j]=int(input(">>>> "))
#         else:
#             lst[i][j]=input()
# print(lst) Bir nechta studentlarni listga joylash.

#2-usul
# student = {
#     'ism': '',
#     'familiyasi': '',
#     'yosh': ''
# }
# lst = []
# for i in range(int(input("Nechta studentni kirgizasiz: "))):
#     lst.append(student.copy())
#     lst[i]['ism'] = input("Ismingizni kiriting: ")
#     lst[i]['familiya'] = input("Familiyangizni kiriting: ")
#     lst[i]['yosh'] = int(input("yoshingizni kiriting: "))

#arrayda list va ustunlar o'rnini almashtirish
# lst = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# natija = []
# for i in range(len(lst)):
#     ustun = []
#     for j in range(len(lst[i])):
#         ustun.append(lst[j][i])
#     natija.append(ustun)
# print(natija)

# istalgan sonni ikkilik sanoq sistemasiga o'tkazish
# son=int(input("sonni kiriting: "))
# lst =[]
# while son>0:
#     lst.append(son%2)
#     son=son//2
# lst.reverse()
# print(lst)


# def qaytar(soz:str):
#     return soz[:len(soz)//2]+soz[(len(soz))//2::].upper()
# print(qaytar("income"))



# N9:
# Foydalanuvchi string kiritadi. Shu stringdagi har bitta so'zning dastlabki va oxirgi 
#harflarini katta harf qilib qo'ying.

# Input:     "hello world"
# Ouput:   "HellO WorlD"

# Input:     "chelsea is champion"
# Output:  "ChelseA IS ChampioN"
# def katta(soz: str):
#     sozlar = soz.split()
#     natija = ''
#     for i in sozlar:
#         if len(i) > 1:
#             harf = i[0].upper() + i[1:-1] + i[-1].upper()
#         else:
#             harf = i.upper()
#         natija += harf + ' '
#     return natija

# soz = input("Iltimos, stringni kiriting: ")
# natija = katta(soz)
# print("Natija:", natija)

#bir qatorda kalkulyator
#while True: print(eval(input('>>>> ')))

#berilgan sonni rim raqamiga aylantirish.
# def ArabtoRim(son: int):
#     Rim={1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X',
#          40:'XL', 50:'L', 90:'XC', 100:'C',
#          400:'CD', 500:'D', 900:'CM', 1000:'M'}
#     for key, value in reversed(Rim.items()):
#         q=son//key
#         son=son%key
#         while q!=0:
#             print(Rim[key], end="")
#             q-=1
# ArabtoRim(int(input(">>> ")))

#songacha tub sonlarni recursiv funksiya orqali chiqarish
# import math as m
# def tubmi(son: int):
#     for i in range(2, int(m.sqrt(son)+1)):
#         if not son%i:
#             return False
#     return True
# def recursive(son):
#     if son == 1:
#         return
#     recursive(son-1)
#     if tubmi(son):
#         print(son)
# recursive(20)

# print(int(eval("1-4+10"))) STR ICHIDAKI QIYMATLARNI HISOBLASH

#dctdaki eng katta 5 ta qiymatni olib chiqish
# dct={}
# for i in range(10):
#     [key, value] = input().split()
#     dct[key]=int(value)
# lst = list(dct.items())
# lst.sort(key=lambda tp: tp[1], reverse=True)
# print(lst[:5])

# kiritilgan so'zlarni birinchisini va oxirgisini teskari yozish
# soz="Python is awesome last year".split()
# soz[0]=soz[0][::-1]
# soz[-1]=soz[-1][::-1]
# print(*soz)

# n=10
# if n%2!=0:
#     for i in range(1, n+1):
#         for k in range(1, i+1):
#             print(k, end="")
#             if k != i:
#                 print("+", end="")
#             else:
#                 print("=", end=f"{sum(list(range(1, k+1)))}")
#         print()
# else:
#     for i in range(n,0,-1):
#         for k in range(i,0,-1):
#             print(k, end="")
#             if k != 1:
#                 print("+", end="")
#             else:
#                 print("=", end=f"{sum(list(range(i,0,-1)))}")
#         print()

# dct_moshina = {}
# dct_davlat = {}
# with open("car_model.txt", encoding='utf-8') as f:
#     for i in f.read().split('\n'):
#         natija=i.split(',')
#         if natija[4] not in dct_moshina:
#             dct_moshina[natija[4]]=1
#         else:
#             dct_moshina[natija[4]]+=1
#         if natija[-1] not in dct_davlat:
#             dct_davlat[natija[-1]]=[natija[4]]
#         else:
#             dct_davlat[natija[-1]].append(natija[4])

# brand = max(dct_moshina, key=dct_moshina.get)
# print(brand)

# max_davlat=max(dct_davlat.items(), key=lambda x: x[1].count(brand))[0]
# min_davlat = min(dict(filter(lambda x: x[1].count(brand), dct_davlat.items())).items(), key=lambda x: x[1].count(brand))[0]
# print(max_davlat, min_davlat)
# for i in list(filter(lambda x: x[1].count(brand)==1, dct_davlat.items())):
#     print(i)

# class Talaba:
#     def __init__(self, ism, familiya, yosh) -> None:
#         self.ism = ism
#         self.f = familiya
#         self.yosh = yosh
#         self.kurs = 1
#         self.salomlash()

#     def imtixon_topshir(self):
#         self.update_kurs(int(input(f"{self.ism} Necha bal oldingiz: ")))

#     def update_kurs(object, ball):
#         object.yosh_update()
#         if ball > 60:
#             if object.kurs == 4:
#                 print("Siz tugatdingiz")
#             else:
#                 print(f"{object.ism} imtixondan o'tdingiz")
#                 object.kurs+=1
#         else:
#             print(f"{object.ism} imtixondan yiqildingiz")
#     def yosh_update(self):
#         self.yosh +=1
#     def salomlash(self):
#         print('Salom')
#     def ism_qaytar(self):
#         return self.ism
#     def tanish(self):
#         return f"Salom mening ismim: {self.ism_qaytar()}"
#     def info(self):
#         print(f"""
# Ismi:       {self.ism}
# Familiyasi: {self.f}
# Yoshi:      {self.yosh}
# Kursi:      {self.kurs}
# """)
# t1 = Talaba('Ergash', 'Eshmatov', 23)
# t2 = Talaba('Eshmat', 'Ergashev', 18)
# t1.info()
# t2.info()
# t1.imtixon_topshir()
# t2.imtixon_topshir()
# t1.info()
# t2.info()

# class Odam:
#     def __init__(self, name):
#         self.ism=name
#     def baqirish(self):
#         print(f"VOY DOOOOD Mening ismim {self.ism} edi")
# class Kuchuk:
#     def __init__(self, laqab):
#         self.laqab=laqab
#     def tishla(self, odam):
#         print(f"Vov-vov men {self.laqab}man")
#         odam.baqirish()
# od1=Odam('Eshmat')
# od2=Odam("Toshmat")
# od3=Odam("Botir")
# k1=Kuchuk("qoplon")
# k2=Kuchuk("bobik")
# k1.tishla(od2)

# class C:
#     pass
# setattr(C, 'x', 11)
# C.y='hello world'
# print(getattr(C,'y').upper())
##---------------------------------------------------------------
# class D: #classda atributlarni o'chirish
#     x: int=34
#     y: float=15.6
# del D.x
# print(getattr(D, 'x', 'Impossible'))
# delattr(D, 'y')
# print(D.__dict__)
##------------------------------------------------------------------
# class Person:
#     age = 18
#     height = 175
# person_1=Person()
# person_2=Person()
# person_1.hair_color = 'black'
# person_2.hair_color = 'white'
# person_1.height = 165
# print(person_1.__dict__, person_2.__dict__, Person.__dict__, sep='\n')
##-----------------------------------------------------------------  
# class Cat:
#     age: int = 2
#     breed: str = 'Bengal'
# tom = Cat()
# tom.age=1 #har qanday holatda ham globalning qiymati o'zgarmaydi
# setattr(tom, 'age', 1)
# print(getattr(Cat, "breed"), getattr(Cat, 'age'), sep='\n')
##----------------------------------------------------------------
# class Car:
#     speed: float = 98.0
#     color: str = 'red'
# del Car.speed
# print(getattr(Car, 'speed', 'unaqasi yoq'), Car.color, sep='\n')
##-----------------------------------------------------------
# class A: #a va b kimga tegishli ekanligini aniqlash
#     pass
# class B:
#     pass
# a=A()
# b=B()
# print(isinstance(a, A), isinstance(b, A))
##-------------------------------------------------------------
# class A:
#     pass
# A.state = "example"
# print(A.__dict__)
# a=A()
# print(isinstance(a, A))
# print(a.__dict__)
##------------------------------------------------------------
# import math
# import operator as op
# class Circle:
#     radius = 5
# class Rectangle:
#     width = 5
#     height = 7
# print(math.pi*Circle.radius**2)
# print(op.mul(Rectangle.width, Rectangle.height))
##----------------------------------------------------------
# class Cat: #bunda 14 ta oq rangli mushuk yaratib, songida 2 ni rangini qora qilib quydik
#     color: str = 'white'
#     amount = 14

# arr = [Cat() for i in range(14)]
# arr[0].color=arr[1].color='black'
##-----------------------------------------------------------------
# import pprint #dict malumotlarini chiroyli korinishda chiqaradi
# pprint.pprint(tuple.__dict__)
##------------------------------------------------------------
# import pprint as pp
# import random as r
# class Boy:
#     age: int = 15
#     height: int = 160

# arr=[Boy() for i in range(5)]
# index=r.randrange(0,5)
# arr[index].height=165
# arr_height=[arr[index].height for index in range(5)]

# boy = r.choice(arr)
# del boy
# print(boy)
##------------------------------------------------------
# languages = ['english', 'french', 'deutsch']
# class Country:
#     population: int=5e6
#     regime: str='democracy'
#     square: int=3e5

# arr = [Country() for i in range(3)]
# for count, country in enumerate(arr):
#     country.language = languages[count]
# print([arr[index].language for index in range(3)])
##-----------------------------------------------
# import pprint
# result=[]
# class Auto: #ro'yxat orasidan class ichidaki parametrlariga tug'ri kelgan carni ekranga chiqaramiz. 
#     color: str = 'black'
#     engine: str = '1.6'
# lst =['Renault Logan 1.6 black',
#       'Kia Rio 1.6 white',
#       'Chevrolet Cobalt 2.0 black',
#       'Skoda Octavia 1.8 black',
#       'Honda Civic 1.6 black',
#       'Toyota Camry 2.0 red',
#       'Peugeo 307 1.6 purple',
#       'Ford Focus 1.6 white',
#       'Mazda 3 1.8 black']
# for i in lst:
#     car = i.split()
#     if car[2]==Auto.engine and car[3]==Auto.color:
#         liked_car = Auto()
#         liked_car.model=car[0]+' '+car[1]
#         result.append(liked_car.model)
#         print(liked_car.model)
# print(result)
##----------------------------------------------

class Talaba:
    def __init__(self, ism) -> None:
        self.ism=ism
        self.nechta_kurs=0
    
    def ism_qaytar(self):
        return self.ism
    
    def salomlash(self):
        return "Assalom...."

class Kurs:
    def __init__(self, nom, ustoz) -> None:
        self.nomi = nom
        self.ustozi = ustoz
        self.talabalar_royxati = []
        self.talabalar_miqdori = 0

    def add_student(self, obj: Talaba):
        if obj.nechta_kurs == 0:
            self.talabalar_royxati.append(obj.ism)
            self.talabalar_miqdori +=1
        else:
            print("bir vaqtda ikki kursda o'qish mumkin emas")
    
    def remove_student(self, obj: Talaba):
        if obj.ism_qaytar() in self.talabalar_royxati:
            self.talabalar_royxati.remove(obj.ism_qaytar())
            self.talabalar_miqdori-=1
            obj.nechta_kurs=0
    
    def __str__(self) -> str:
        return f"""
Kurs nomi: {self.nomi}"""









