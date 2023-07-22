# import random as r
# class MyList(list):
#     def random(self, N, Rand_min, Rand_max):
#         self.n=N
#         self.min=Rand_min
#         self.max=Rand_max
#         for i in range(self.n):
#             super().append(r.randint(self.min, self.max))
#             super().sort(reverse=True)
# a1=MyList()
# a1.random(10, r.randint(-100,0), r.randint(0,100))
# print(a1)

##--------------------------------------------------
#masala=1
# class Soldat(list):
#     def __init__(self, ismi: str, familiyasi:str, yoshi: int, vazni: int, buyi:int) -> None:
#         self.ism=ismi
#         self.fam=familiyasi
#         self.yosh=yoshi
#         self.vazn=vazni
#         self.buy=buyi
#     def __str__(self):
#         return f"""Ismi: {self.ism}
# Familiyasi: {self.fam}"""

# s1 = Soldat("Salim", "To'ychiyev", 19, 78, 180)
# s2 = Soldat("Bozorov", "Laziz", 21, 68, 171)
# s3= Soldat("Badirov", "Keldiyor", 23, 55, 165)
# s4= Soldat("Samadov", "Diyorbek", 19, 54, 148)
# soldatlar = [s1, s2, s3, s4]

# for i in soldatlar:
#     print()
#     if i.yosh>18 and i.buy<150 and i.vazn<75:
#         print(f"Piyoda Qo'shinlari:\n{i}")
#     else:
#         print(f"Tank Qo'shinlari:\n{i}")
##--------------------------------------------------------------
#masala=2
# class Uchburchak:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c

#     def sigishkvadratga(self, kvadrat):
#         if (self.a >= kvadrat.x and self.a <= kvadrat.x + kvadrat.y) and (self.b >= kvadrat.y and self.b <= kvadrat.y + kvadrat.y):
#             return True
#         else:
#             return False

# class Kvadrat:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def sigishuchburchakga(self, uchburchak):
#         if (self.x >= uchburchak.a and self.x <= uchburchak.a + uchburchak.b) and (self.y >= uchburchak.b and self.y <= uchburchak.b + uchburchak.c):
#             return True
#         else:
#             return False

# uchburchak = Uchburchak(1, 2, 3)
# kvadrat = Kvadrat(3, 3)

# if uchburchak.sigishkvadratga(kvadrat):
#     print("Uchburchak kvadratni ichiga sig'di")
# else:
#     print("Uchburchak kvadratni ichiga sig'madi")

# if kvadrat.sigishuchburchakga(uchburchak):
#     print("Kvadrat uchburchakni ichiga sig'di")
# else:
#     print("Kvadrat uchburchakni ichiga sig'madi")
##--------------------------------------------------------------------
#metod=1
#class Cars:
#     def __init__(self, id, firstname, lastname, gender, brand, year, color, country):
#         self.id = id
#         self.firstname = firstname
#         self.lastname = lastname
#         self.gender = gender
#         self.brand = brand
#         self.year = year
#         self.color = color
#         self.country = country

# class Nisbat:
#     def hisob(self):
#         erkak=0
#         ayol=0
#         for i in carslist:
#             if i.gender=='Male':
#                 erkak+=1
#             else:
#                 ayol+=1
#         if erkak>ayol:
#             return f"Erkaklar ayollardan {(erkak*100/len(carslist))-(ayol*100/len(carslist))}%ga ko'p"
#         elif erkak==ayol:
#             return "Ular teng"
#         else:  
#             return f"Ayollar erkaklardan {(ayol*100/len(carslist))-(erkak*100/len(carslist))}%ga ko'p"
            
# carslist = [
#     Cars(1, "John", "Doe", "Male", "Toyota", 2015, "Black", "Japan"),
#     Cars(2, "Emma", "Smith", "Female", "Toyota", 2018, "White", "Japan"),
#     Cars(3, "Michael", "Johnson", "Male", "BMW", 2019, "Silver", "Germany"),
#     Cars(4, "Emily", "Williams", "Females", "BMW", 2017, "Blue", "Germany"),
#     Cars(5, "Daniel", "Brown", "Male", "Ford", 2020, "Red", "USA"),
#     Cars(6, "Emilye", "William", "Females", "BMW", 2019, "Blue", "Germany")]

# result = Nisbat()
# print(result.hisob())
##------------------------------------------------------------------------------------
#metod=2
# class Cars:
#     def __init__(self, id, firstname, lastname, gender, brand, year, color, country):
#         self.id = id
#         self.firstname = firstname
#         self.lastname = lastname
#         self.gender = gender
#         self.brand = brand
#         self.year = year
#         self.color = color
#         self.country = country

#     def kopmashinadavlat():
#         brands = {}
#         countries = {}

#         for car in carslist:
#             brand = car.brand
#             country = car.country
#             if brand in brands:
#                 brands[brand] += 1
#             else:
#                 brands[brand] = 1
#             if country in countries:
#                 countries[country] += 1
#             else:
#                 countries[country] = 1

#         maxbrand = max(brands, key=brands.get)
#         maxcountry = max(countries, key=countries.get)
#         mincountry = min(countries, key=countries.get)

#         return f"Eng ko'p mashina {maxbrand} markasi bo'lib, uning mashinalari {maxcountry} davlatida ko'p joylashgan. " \
#                f"Kam mashinalari esa {mincountry} davlatida joylashgan."
    
# carslist = [
#     Cars(1, "John", "Doe", "Male", "Toyota", 2005, "Black", "Japan"),
#     Cars(2, "Emma", "Smith", "Female", "Toyota", 2008, "White", "Japan"),
#     Cars(3, "Michael", "Johnson", "Male", "BMW", 2000, "Silver", "Germany"),
#     Cars(4, "Emily", "Williams", "Female", "BMW", 2001, "Blue", "Germany"),
#     Cars(5, "Daniel", "Brown", "Male", "Ford", 2020, "Red", "USA"),
#     Cars(6, "Emilye", "William", "Females", "BMW", 2009, "Blue", "Germany")]

# result = Cars.kopmashinadavlat()
# print(result)
##------------------------------------------------------------------

# metod=3
# class Cars:
#     def __init__(self, id, firstname, lastname, gender, brand, year, color, country):
#         self.id = id
#         self.firstname = firstname
#         self.lastname = lastname
#         self.gender = gender
#         self.brand = brand
#         self.year = year
#         self.color = color
#         self.country = country
       
# carslist = [
#     Cars(1, "John", "Doe", "Male", "Toyota", 2005, "Black", "Japan"),
#     Cars(2, "Emma", "Smith", "Female", "Toyota", 2008, "White", "Japan"),
#     Cars(3, "Michael", "Johnson", "Male", "BMW", 2000, "Silver", "Germany"),
#     Cars(4, "Emily", "Williams", "Females", "BMW", 2003, "Blue", "Germany"),
#     Cars(5, "Daniel", "Brown", "Male", "Ford", 2020, "Red", "USA"),
#     Cars(6, "Emilye", "William", "Females", "BMW", 2019, "Blue", "Germany")]

# for i in carslist:
#     print()
#     if i.year<=2005:
#         print(f"""#################
              
# Kimdan: Auto Test Corp
# Kmga: {i.firstname} {i.lastname}
# Joriy Davlat: {i.country}

# Hurmatli {i.firstname} {i.lastname}! {i.brand} tomonidan
# {i.year}da ishlab chiqarilgan {i.color} rangli avtoulovingiz
# Texnik Holatini tekshirtirish maqsadida mahalliy
# Auto Test Corp ofisiga murojat qilishingizni so'raymiz!

# ####################""")