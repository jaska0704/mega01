import math
#def ManfiyMusbat(A:int):
#     if A>0:
#         return True
#     return False
# print(ManfiyMusbat(int(input("Son Kirit: "))))


# def list(lst:list):
#     lst = sorted(lst, reverse=True)
#     return tuple(lst)
# lst =  [1,2,3,4,5,6,7,8]
# print(list(lst))


# def Funcsiya(a):
#     if isinstance(a, (list, set , tuple, dict)):
#         return True
#     return False
# print(Funcsiya((3,4,5,6,6,2,4)))


# def turtburchak(a,b):
#     return (2*(a+b), a*b)
# print(turtburchak(5,6))
# print(type(turtburchak(5,6)))


# def kattasi(a,b):
#     return a if a>b else b
# print(kattasi(3,4))


# def katta(lst:list):
#     return max(lst)
# lst = [3, 6, 8, 1, 0]
# print(katta(lst))


#t7
# def kvadrat(son: int):
#     lst=[]
#     for i in range(son):
#         lst.append(int(input("sonni kiriting: "))**2)
#     return lst
# print(kvadrat(int(input("Nechta son kiritasiz: "))))

#T8
# def harflar(gap: str):
#     count, count1 = 0, 0
#     for i in gap:
#         if i.islower():
#             count+=1
#         elif i.isupper():
#             count1+=1
#     return [count1,count]
    
# print(harflar("Good Luck"))

#t9
# def sonlar(a,b):
#     lst=[]
#     if a<b:
#         for i in range(a, b):
#             if math.sqrt(i)%1==0:
#                 lst.append(int(math.sqrt(i)))
#         if lst==[]:
#             return None    
#         return lst
#     else:
#         return "Siz xato ketma-ketlik kiritdingiz"
# print(sonlar(int(input("Birinchi sonni kiriting: ")), int(input("Ikkinchi sonni kiriting: "))))

#T10
# def dct(n):
#     dict1 = {}
#     for i in range(1, n):
#         dict1[i]=i*i
#     return dict1
# print(dct(int(input(">>> "))))

#t11
# def listlar(lst:list):
#     for i in range(len(lst)):
#         lst[i]=sum(list(lst[i]))
#     return lst
# lst=[(1, 2), (2, 3), (3, 4)]
# print(listlar(lst))

#t12
# def listlar(lst:list):
#     for i in range(len(lst)):
#         lst[i]=list(lst[i])
#     return lst
# lst = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
# print(listlar(lst))

#t13
# def lists(list1, list2, list3):
#     dict1 = {}
#     for i, item in enumerate(list1):
#         dict1[i+1] = {item: None}
#     for i, item in enumerate(list2):
#         dict1[i+1] = {item: list3[i]}   
#     return dict1

# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# list3 = [True, False, True]

# result = lists(list1, list2, list3)
# print(result)

#t14
# def gap(soz:str):
#     dct={}
#     for i in soz:
#         count=0
#         for j in range(len(soz)):
#             if i == soz[j]:
#                 count+=1
#         dct[i]=count
#     return dct
# print(gap("w3resource"))  

#t15 bunda jami raqamlarni bittalab hisoblaganda
# def sonlar(lst: list):
#     lst2=[]
#     for i in range(len(lst)):
#         lst[i]=" ".join(str(lst[i])).split()
#         lst2+=lst[i]
#     for i in range(len(lst2)):
#         lst2[i]=int(lst2[i])
#     lst2.sort()
#     lst2.reverse()
#     natija=0
#     for i in lst2:
#         natija=natija*(10**len(str(i)))+i
#     return natija
# lst=[61, 228, 9]
# print(sonlar(lst))

#t15 bu shart buyicha
# def sonlar(lst: list):
#     lst2=[]
#     for i in range(len(lst)):
#         lst[i]=str(lst[i])
#     lst.sort()
#     lst.reverse()
#     natija=0
#     for i in lst:
#         natija=natija*(10**len(i))+int(i)
#     return natija
# print(sonlar([61, 228, 9]))

#t16
# def diction(lst: list):
#     dct={}
#     for i in lst:
#         dct[i[0]]=[i[1],i[2]]
#     return dct
# lst = [
#      [1, 'Jean Castro', 'V'],
#      [2, 'Lula Powell', 'V'],
#      [3, 'Brian Howell', 'VI'],
#      [4, 'Lynne Foster', 'VI'],
#      [5, 'Zachary Simon', 'VII']
# ]
# print(diction(lst))

#t17
# def juftlar(lst:list):
#     for i in lst:
#         if int(str(i)[0])%2==0:
#             print(i)
# lst = [123, 456, 789, 852, 12, 42, 61, 369]
# juftlar(lst)

# n=1
# def maksimal(lst:list):
#     lst.sort()
#     return lst[-2]
# lst = [123, 456, 789, 852, 12, 42, 61, 369]
# print(maksimal(lst))

# n=2
# def minimal(lst:list):
#     lst.sort()
#     return lst[1]
# lst = [123, 456, 789, 852, 12, 42, 61, 369]
# print(minimal(lst))

# n=3
# def sorteD(lst:list):
#     lst.sort()
#     print(lst)
# lst = [123, 456, 789, 852, 12, 42, 61, 369]
# sorteD(lst)

# n=4
# def takror(lst):
#     takrorlar = {}
#     max_takrorlar_soni = 0
#     max_takrorlanadigan_qiymat = None
    
#     for i in lst:
#         if i in takrorlar:
#             takrorlar[i] += 1
#         else:
#             takrorlar[i] = 1
        
#         if takrorlar[i] > max_takrorlar_soni:
#             max_takrorlar_soni = takrorlar[i]
#             max_takrorlanadigan_qiymat = i
    
#     return max_takrorlanadigan_qiymat

# lst = [2, 2, 1, 2, 3, 2, 2, 4, 5, 4, 4, 4]
# eng_takror_qiymat = takror(lst)
# print(f"Eng ko'p takrorlangan qiymat: {eng_takror_qiymat}")

# def son(lst:list):
#      new_dct = {}                 
#      for i in set(lst):
#           new_dct[i] = lst.count(i)                     
     
#      return sorted(new_dct.items(), key=lambda x: x[1], reverse= True)[0][0]

# lst = [1,2,3,3,4,5,5,5,7,7,6,7,7,8]
# print(son(lst))

# n=5
# def son(lst:list):
#      new_dct = {}                 
#      for i in set(lst):
#           new_dct[i] = lst.count(i)                     #N_S4
     
#      return sorted(new_dct.items(), key=lambda x: x[0], reverse= True)[-1][-1]

# lst = [1,1,2,3,3,4,5,5,5,5,5,6,7,7,8]
# print(son(lst))

# n=6
# def maksimal(dct:dict):
#    maX = max(list(dct.values())) 
#    return maX
# dct = {1: 10, 2: 20, 3:30, 4: 15, 5: 25}
# print(maksimal(dct))

# n=7
# def maksimal(dct:dict):
#    maX = max(list(dct.keys())) 
#    return maX
# dct = {1: 10, 2: 20, 3:30, 4: 15, 5: 25}
# print(maksimal(dct))

# n=8
# def format(dct: dict):
#     print(dct.items())
# dct = {1: 10, 2: 20, 3:30, 4: 15, 5: 25}
# format(dct)

# n=9
# def uzgarish(dct: dict):
#     dct[2]=25
#     print(dct)
# dct = {1: 10, 2: 20, 3:30, 4: 15, 5: 25}
# uzgarish(dct)

#n=11
# def qiymat(lugat):
#     for kalit, qiymat in lugat.items():
#         lugat[kalit] = 0
#     return lugat
# dct = {
#     'key': 'kalit',
#     'book': 'kitob',
#     'dog': 'it',
#     'help': 'yordam'
# }
# print(qiymat(dct))

# n=12
# def max(lst: list):
#     son=-1
#     for i in lst:
#         if i%2==0 and i>son:
#             son=i
#     return son
# lst = [123, 450, 789, 85, 121, 421, 61, 369]
# maxi=max(lst)
# print(maxi)

# n=13
# def sett(seet: set):
#     minn=0
#     for i in range(len(seet)-1):
#         if seet[i]<seet[i+1]:
#             minn=seet[i]
#     return minn
# set=(123, 450, 789, 85, 121, 421, 61, 369)
# print(sett(set))
