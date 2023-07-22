# n=10
# str1, str2 = input('1-string>> '), input('2-string>> ')
# print(list(filter(lambda x: x in str2, list(str1))))

# n=33
# gap=input('Gapni kiriting: ')
# for i,x in enumerate(gap):
#     if x.isdigit():
#         print(i)
#         break
#     elif len(gap)-1==i:
#         print('yoq')

# f=34
# gap=input("gapni kiriting: ")
# for i,x in enumerate(gap):
#     if x.isupper():
#         print(i)
#         break
#     elif len(gap)-1==i:
#         print('yoq')

# n=5
# gap=input("gapni kiriting: ")
# ad=" "
# d=int(input("sonni kiriting: "))
# for i,x in enumerate(gap):
#     if i!=d:
#         ad+=x
# print(ad)

# O=13
# lst=[7, 8, 1, 3, 4, 6, 7, 5]
# lst1=lst.copy()
# lst1=[lst1[i]**2 if i%2==0 else lst1[i]**3 for i in range(len(lst1))]
# print(lst1)

# O=14
# lst, lst1, lst2 = [2, 8, 5], [3, 7, 1], [10, -6, 2]
# print(lst+lst1+lst2)

numbers = (5, -3, 4, -2, 4, 1, -9, 8, -6, 7, 0, 4)
son=-9
lst=[]
for i in range(len(numbers)):
    if son==numbers[i]:
        lst.append(i)
print(max(lst))