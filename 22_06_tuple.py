# list_masala 1
# lst = list(map(int, input("sonni kiriting: ").split()))
# lst.sort()
# print(lst[-2])

# list_masala 2
# tpl = tuple(map(int, input("sonni kiriting: ").split()))
# tpl = list(tpl)
# tpl.sort()
# print(tpl[1])

#list_masala 3
# lst = list(map(int, input("sonni kiriting: ").split()))
# lst.sort()
# lst.reverse()
# print(lst)

# #list_masala 4
# lst = [5,8,12,-6,8,31,10,8,5]
# takror=0
# for i in lst:
#     count = lst.count(i)
#     if count>takror:
#         takror=count
#         son=i
# print(son)

#list_masala 6
# lst = [5,8,12,-6,8,31,18,8,5]
# max=0
# for i in lst:
#     if not i%2:
#         if i>max:
#             max=i
# print(max)

#list_masala 7
# lst = [5,8,12,-6,-81,31,18,-8,-5]
# manfiy = [i for i in lst if i<0]
# musbat = [i for i in lst if i>0]
# manfiy.sort()
# musbat.sort()
# musbat.reverse()
# print(*manfiy, *musbat)

#list_masala 8
# lst, count = [1, True, 'Salom', [1, 2, 3], 'Nimadur', 44, 3.14], 0
# for i in lst:
#     if type(i)==int:
#         count+=1
# print(count)

#list_masala 9
# lst = ['salom', "Bola", True, 12, 'Aziz', '12.9', 60.06, 'False']
# for i in lst:
#     if type(i)==str and i[0].isupper():
#         print(i)

#list_masala 10
# lst = [True, "Salom", 5, 5.6]
# for i in range(len(lst)):
#     lst[i]=type(lst[i])
# print(lst)

#Q12
# lst = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
# count=0
# for i in lst:
#     if type(i)==int:
#         count+=1
# print(count)

#Q13
# lst = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, 12.22]
# max=0
# for i in lst:
#     if isinstance(i, int) or isinstance(i, float):
#         if i>max:
#             max=i
# print(max)

#Q14
# lst = [9,9,9,9]
# natija=0
# for i in lst:
#     natija=natija*(10**len(str(i)))+i
# natija=natija+1
# natija=(" ".join(str(natija))).split()
# print(natija)

#Q15
# lst = [1,2,3,14]
# count, son=0,0
# for i in lst:
#     if i>count:
#         count=i
#         son+=1
# if son==len(lst):
#     print("tartibli")
# else:
#     print("tartibsiz")

#Q16
# lst = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (), ('d',)]
# lst = [i for i in lst if i]
# print(lst)
