# s=1
# fayl=open("people_count.txt", "r")
# players=fayl.read().split("\n")
# for i in range(len(players)):
#     ism=players[i].split(",")[0]
#     familya=players[i].split(",")[1]
#     davlat=players[i].split(",")[-1]
#     print(ism, familya, davlat)
# fayl.close()

# s=2
# fayl=open("languages.txt", "r", encoding="utf-8")
# aholi=fayl.read().split("\n")
# for i in range(len(aholi)):
#     if int(aholi[i].split(",")[1])>1000000:
#         print(aholi[i])

# s3=1
# fayl=open("product_material.txt", "r", encoding="utf-8")
# aholi=fayl.read().split("\n")
# for i in range(len(aholi)):
#     sum=float(aholi[i].split(",")[3][1::])
#     if sum>=500 and sum<=1000:
#         print(aholi[i].split(",")[1], aholi[i].split(",")[2], sum)

# s3=2
# fayl=open("product_material.txt", "r", encoding="utf-8")
# aholi=fayl.read().split("\n")
# lst=[]
# nomi=input("Material nomi: ")
# for i in range(len(aholi)):
#     material=(aholi[i].split(",")[2])
#     if material==nomi:
#         if aholi[i].split(",")[4]=='true':
#             lst.append(float(aholi[i].split(",")[3][1::]))
# lst.sort()
# print(lst)

# s3=3
# fayl=open("product_material.txt", "r", encoding="utf-8")
# aholi=fayl.read().split("\n")
# for i in range(len(aholi)):
#     material=(aholi[i].split(",")[2])
#     if aholi[i].split(",")[4]=='false' and float(aholi[i].split(",")[3][1::])>1000:
#         print(material)

# s4=1       
# fayl=open("cinema.txt", "r", encoding="utf-8")
# aholi=fayl.read().split("\n")
# soat=int(input("soatni kiriting: "))
# for i in range(len(aholi)):
#     if int(aholi[i].split(",")[5][:-3])>soat:
#         print(aholi[i])
    
# s4=2
# fayl=open("cinema.txt", "r", encoding="utf-8")
# aholi=fayl.read().split("\n")
# for i in range(len(aholi)):
#     if int(aholi[i].split(",")[3])>2000:
#         janr=aholi[i].split(",")[2].split("|")
#         if 'Comedy' in janr or 'Drama' in janr or 'Romance' in janr:
#             print(aholi[i].split(",")[1], aholi[i].split(",")[4])

# s4=3
# fayl=open("cinema.txt", "r", encoding="utf-8")
# aholi=fayl.read().split("\n")
# for i in range(len(aholi)):
#     if int(aholi[i].split(",")[5][:-3])>17:
#         janr=aholi[i].split(",")[2].split("|")
#         if 'Horror' in janr:
#             print(aholi[i])

# s5=1
# fayl=open("booking_data.txt", "r", encoding="utf-8")
# aholi=fayl.read().split("\n")
# summa=float(input("Hisobni kiriting: "))
# for i in range(len(aholi)):
#     sum=float(aholi[i].split(",")[5][1::])
#     if sum>summa-50 and sum<summa+100:
#         print(aholi[i])

# s5=3
# fayl=open("booking_data.txt", "r", encoding="utf-8")
# aholi=fayl.read().split("\n")
# for i in range(len(aholi)):
#     if aholi[i].split(",")[3]=='US' and int(aholi[i].split(",")[4][:-3])<20:
#         print(aholi[i])

#s7=1
# fayl=open("car_model.txt", "r", encoding="utf-8")
# aholi=fayl.read().split("\n")
# ayollar,erkaklar=0,0
# for i in range(len(aholi)):
#     ayollar+=aholi[i].split(',').count('Female')
#     erkaklar+=aholi[i].split(',').count('Male')
# print(f"Erkaklar ayollardan {100-(ayollar*100//erkaklar)}% ga ko'p ekan!")

# s7=2
# fayl=open("car_model.txt", "r", encoding="utf-8")
# aholi=fayl.read().split("\n")
# lst,lst1,lst2=[],[],[]
# k=0
# for i in range(len(aholi)):
#     if aholi[i].split(',')[4] not in lst:
#         lst.append(aholi[i].split(',')[4])
# for i in range(len(aholi)):
#     aholi[i]=aholi[i].split(',')
#     lst1+=aholi[i]
# for i in lst:
#     coun=0
#     coun+=lst1.count(lst[k])
#     lst2.append(coun)
#     k+=1
# print(max(lst2), lst[0])


