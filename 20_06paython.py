import os
os.system("cls")
# Q1
# lst = [True, "salom", 5, 5.6]
# for i in range(len(lst)):
#     lst[i]=type(lst[i])
# print(lst)

#Q2
# lst = [[2, 15, 4], [19, 24, 11], [7, 9, 5], [10, 3, 1]]
# for i in range(len(lst)):
#     for j in range(len(lst[i])):
#         if j%2==1:
#             lst[i][j]=lst[i][j]**2
# print(lst)

#Q3
# lst =   [7, 8, 1, 3, 4, 6, 7, 5]
# lst = [lst[i]**2 if i%2==0 else lst[i]**3 for i in range(len(lst))]
# print(lst)

#Q4
# lst =[3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9 , 7, 1]
# lst1 = []
# lst2 = []
# for i in range(len(lst)):
#     if lst[i] > 0:
#         lst1.append(lst[i])
#     else:
#         lst2.append(lst[i])    
# lst = lst1 + lst2
# print(lst)

#Q5
# numbers = (5, -3, 4, -2, 1, -9, 8, -6, 4, 7, 0)
# numbers = list(numbers)
# n=int(input("sonni kiriting: "))
# lst = []
# for i in range(len(numbers)):
#     if numbers[i] != n:
#         lst.append(numbers[i])
        
# print(tuple(lst))

#Q6
# lst = [[5, 3, 7], [1, 4, 9], [2, 8, 6]]
# for i in range(len(lst)):
#     lst[i] = sum(lst[i])
# print(max(lst))

#Q7
# lst1 = [2, -1, 5, -3, 8, -4, 6, 7, 9]
# lst2 = [1, 6, 7, -3, -9, -4, -5]
# new = list(set(lst1) & set(lst2))
# print(new)

#Q8
# lst = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# lst[2][2].insert(2, 7000)
# print(lst)

#Q9
# lst = [2, 1, -4, -9, 0, -5, 8, 3]
# for i in lst:
#     if i == max(lst):
#         lst.remove(i)
# print(max(lst))

#Q10
# lst = [2, 5, 1, 4, 3, 2, 1, 6, 8, 5, 7, 9]
# lst1 = []
# for i in lst:
#     if i not in lst1:
#         lst1.append(i)
# print(lst1)

#Q11
# lst, lst2 = [11, 33, 50], []
# for i in lst:
#     lst2.append(str(i))
# print("".join(lst2))

#Q12
# lst = [1, 1, 3, 4, 4, 5, 6, 7]
# lst2 = [0, 1, 2, 3, 4, 4, 5, 7, 8]
# lst = lst + lst2
# print(sum(lst)/len(lst))
