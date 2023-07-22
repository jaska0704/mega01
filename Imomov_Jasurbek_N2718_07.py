# import math

# class Calculator:
#     def __init__(self, N):
#         self.__N = N

#     def plus(self, num=1):
#         self.__N += num

#     def minus(self, num=1):
#         self.__N -= num

#     def multiply(self, num=2):
#         self.__N *= num

#     def divide(self, num=1):
#         self.__N /= float(num)

#     def sqrt(self):
#         self.__N = math.sqrt(self.N)

#     def pow(self, power=2):
#         self.__N = self.__N ** power

#     def mod(self, num=1):
#         self.__N %= num

#     def get_answer(self):
#         return self.__N
# calc=Calculator(10)
# calc.plus(5)
# calc.plus()
# calc.mod(2)
# calc.plus()
# calc.multiply(100)
# calc.multiply()
# calc.minus(40)
# calc.minus()
# #print(calc.N)
# print(calc.get_answer())

# masala=2
# class Mashina:
#     def __init__(self, nomi, turi, ishlab_chiqarilgan_yili, narxi=4000):
#         self.nom=nomi
#         self.tur=turi
#         self.sana=ishlab_chiqarilgan_yili
#         self.narx=narxi
#     def metod(self, lst:list):
#         lst=sorted(lst, key=lambda x: x.sana)
#         for i in lst:
#             print(f"""Nomi: {i.nom}
# Turi: {i.tur}
# Ishlab chiqarilgan sana: {i.sana}
# Narxi: {i.narx}$""")
# m1=Mashina('Pego', 'Yengil avto', 2008, 14000)
# m2=Mashina('Porshe', 'Yengil avto', 2022, 121000)
# m3=Mashina("Jentra", "Yengil avto", 2019,)
# m4=Mashina('Ford', "Yuk avto", 2016, 12990)
# lst=[m1,m2,m3,m4]
# lst=(m1.metod(lst))

# masala=3
# class Countries:
#     def __init__(self, davlat_nomi, poytaxti, aholi_soni, yer_maydoni, yurt_boshi):
#         self.nomi=davlat_nomi
#         self.poytaxt=poytaxti
#         self.aholi=aholi_soni
#         self.maydon=yer_maydoni
#         self.prizident=yurt_boshi
#     def metod(self, lst:list):
#         lst=sorted(lst, key=lambda x: x.nomi)
#         for i in lst:
#             print()
#             print(f"""Davlat nomi: {i.nomi}
# Poytaxti: {i.poytaxt}
# Aholi soni: {i.aholi}
# Yer maydoni: {i.maydon} km kvadrat
# Yurt boshi: {i.prizident}""")
            
# m1=Countries('Marokash', 'Rabot', 38_400_000, 446_500, 'Muhammad VI')
# m2=Countries('Daniya', 'Kopengagen', 5_590_000, 43_043, 'Margret II')
# m3=Countries("Usa", "Washington", 331_449_281, 9_833_520, 'Joe Biden')
# m4=Countries('Saudiya Arabistoni', "Ar-Yiyod", 36_948_000, 1_960_582, 'Salmon ibn Abdulaziz')
# lst=[m1,m2,m3,m4]
# lst=(m1.metod(lst))

