# for i in range(1,11):
#     print()
#     for j in range(1,10):
#         print(j*i, end=" ")

# lst = ['salom', 'Kema', 'katta', 'sana', 'Temir']
# for i in lst:
#    if i[0].lower()=="k":
#       print(i)

# birlik = {0:'', 1:'bir', 2:'ikki', 3:'uch', 4:"to'rt", 5:'besh', 6:'olti', 7:'yetti', 8:'sakkiz', 9:"to'qqiz"}
# onlik = {0: '', 1: 'o`n', 2: 'yigirma', 3: 'o`ttiz', 4: 'qirq', 5: 'ellik', 6: 'oltmish', 7: 'yetmish', 8: 'sakson', 9: 'to`qson'}
# yuzlik = {0: '', 1: 'yuz', 2:'ikki yuz', 3:'uch yuz', 4:"to'rt yuz", 5:'besh yuz', 6:'olti yuz', 7:'yetti yuz', 8:'sakkiz yuz', 9:"to'qqiz yuz"}
# son=int(input("sonni kiriting: "))
# son1 = son%10
# son2 = son//10%10
# son3 = son//100
# print(son3)
# print(yuzlik[son3], onlik[son2], birlik[son1])
# print(len(onlik[son2])+len(birlik[son1])+len(yuzlik[son3]))

# son = int(input(">>>> ")) faktorialni topish
# sum, natija=1, 0
# for i in range(1, son+1):
#     sum=sum*i
# print(sum)

# lst = [11, 22, 30, 40, 15, 16, 7, 28, 9, 10]
# son=int(input("sonni kiriting: "))
# for i in range(len(lst)):
#     for j in range(len(lst)):
#         if son == lst[j]+lst[i]:
#             print(f"birinchi son indexi:{j}\nikkinchi sonni indexsi:{i}")
            