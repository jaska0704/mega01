import math
# r=1
# lst = [5,8,12,-6,8,31,10,8,5]
# lst=list(map(lambda x: float(x), lst))
# print(lst)

# r=3
# hodimlar=[("Hakimov Doniyor", '19.09.2005', 8000000), ("Suxrob aka", '21.03.1996', 9000000)]
# lst=list(map(lambda x:x[0], hodimlar))
# lst1=list(map(lambda x:x[1], hodimlar))
# lst2=list(map(lambda x:x[2], hodimlar))
# print(lst, lst1, lst2)

# r=4
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list2 = [2, 4, 6, 10]
# list1=list(filter(lambda x: x not in list2, list1))
# print(list1)

# r=5
# search='gram'
# social = ["Instgram", "Facebook", "Telegram", "Tik-Tok", "Radiogram"]
# print(list(filter(lambda x:search in x, social)))

# def tubsonlar(son):
#     if son<2:
#         return []
#     elif son==2:
#         return [2]
#     else:
#         for i in range(3,son):
#             if son%i==0:
#                 return tubsonlar(son-1)
#             else:
#                 return tubsonlar(son-1) +[son]
# son=int(input("Sonni kiriting: "))
# print(tubsonlar(son))

# amaliyot=2
# def yaxlit(son):
#     if son<0:
#         return math.ceil(son)
#     else:
#         return math.ceil(son)
# lst=[-12, 4.5, 1.9, -5.1]
# print(list(map(yaxlit, lst)))

# amaliyot=3
# def yaxlit(son):
#     if son<0:
#         return math.ceil(son)
#     else:
#         return math.floor(son)
# lst=[-12.8, 4.5, 1.9, -5.1]
# print(list(map(yaxlit, lst)))

# amaliyot=4
# def yaxlit(son):
#     if son<0:
#         return son*2
#     else:
#         return son*-1
# lst=[-12, 4.5, 1.9, -5.1]
# print(list(map(yaxlit, lst)))

# amaliyot=6
# def butun(son):
#     if son==int(son):
#         return True
#     return False
# lst=[-12, 4.5, 1.9, -5.1, 9, -35]
# print(list(filter(butun, lst)))

# amaliyot=7
# def tublar(son):
#     i,a=2,0
#     while i<son:
#         if son%i==0:return False
#         i+=1
#     if son>1: return True
# lst=[1,2,3,4,5,6,7,8,9]
# print(list(filter(tublar, lst)))

amaliyot=8
l