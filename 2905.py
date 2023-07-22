
#def my_sum(lst):
#     sum=0
#     for i in lst:
#         sum+=i
#     return sum
# print(my_sum([7, 9, 11, 45, 12]))

# def my_max(lst):
#     max=lst[0]
#     for i in range(len(lst)):
#         if max<lst[i]:
#             max = lst[i]
#     return max

# def my_min(lst):
#     min=lst[0]
#     for i in range(len(lst)):
#         if min>lst[i]:
#             min=lst[i]
#     return min

# print(my_min([7, 8, 9, 11, 34]))
# #def my_min(lst):

# lst=[[1,2,3],
#     [-3,4,7],
#     [5,7,-5]]

# max_list = lambda lst: max(lst, key=sum)
# print(max_list(lst)

# son = lambda x: x**2 if x%2==0 else x**3
# print(son(int(input(">>> "))))


# def fact(n): #berilgan sonni faktorialini rekursiv funksiya orqali topish
#    if n == 1:
#        return n
#    else:
#        return n*fact(n-1)

# print(fact(int(input(">>> "))))


# def is_power_of_two(a,b):
#         if 2**b==a:
#             return True
#         elif 2**b>a:
#             return False
#         else:
#             return is_power_of_two(a,b+1)
        
# print(is_power_of_two(int(input(">>> ")), 1))


# def addDigit(n):#raqamlar yigindisi bir xonali son bulmaguncha qo'shadi
#     if n < 10:
#         return n
#     else:
#         return addDigit(sum(int(i) for i in str(n)))
    
# print(addDigit(int(input(">>> "))))
    

# def mega(dictionary):
#     values = list(dictionary.values())
#     for i in range(0, len(values), 2):
#         if i < len(values) - 1:
#             values[i], values[i+1] = values[i+1], values[i]
#     mana_dict = dict(zip(dictionary.keys(), values))
#     return mana_dict
# print(mega({'Apple': 5, 'Banana': 2, 'Cherry': 7, 'Date': 8, 'Elderberry': 12}))


# sana = input(">>>> ") #raqamda kiritilgan oyni so'zda chiqarish.
# lst = sana.split('.')
# for i in range(len(lst)):
#     lst[i]=int(lst[i])
# lst1 = ['-yanvar', '-fevral', '-mart', '-aprel', '-may', '-iyun', '-iyul', '-avgust', '-sentabr', '-oktabr', '-noyabr', '-dekabr']
# for i in range(len(lst1)):
#     if lst[1]==i+1:
#         print(f"{lst[0]}{lst1[i]} 20{lst[2]}")


# son = '000001000' #bir raqamigacha nechta nol borligini aniqlash
# print(son.split())
# sum=0
# # for i in son:
# #     if i == '0':
#         sum+=1
#     else:
#         break
