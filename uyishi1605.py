# for i in range(100, 1000):
#     j=i%10
#     k=i//10%10
#     c=i/100
#     if j==k and j!=c or j!=k and j==c or k==c and j!=k :
#         print(i)   

# print(" ".join(input("sonni kiriting: ")))

# lst = list(map(int, input("sonni kiriting: ").split()))
# for i in range(len(lst)):
#     if int(str(lst[i])[0])%2==0:
#         print(lst[i])

# lst = "11/12/2019"
# lst=lst.split('/')
# lst.reverse()
# print("".join(lst))

# lst, lst2 = list(map(int, input("sonni kiriting: ").split())), []
# lst.sort()
# for i in range(min(lst), max(lst)+1):
#     lst2.append(i)  
# print(sum(lst2)-sum(lst))

# son, chegara = int(input("Raqamni kirgizing: ")), int(input("chegarani belgilang: "))
# lst = []
# for i in range(1, chegara+1):
#     lst.append(son*i)
# print(lst)

#lst = [8, 7, 9, 6, 5, 4, 31, 2, 1, 3]
# lst2 = []
# for i in lst:
#     lst2.append(str(i))
# lst.sort()
# print(lst)


# import random
# lst = []
# lst1 = []
# for i in range(20):
#     lst.append(random.randint(1,10))
#     if lst.count(lst[i])>1 and lst[i] not in lst1:
#         lst1.append(lst[i])
# print(lst)
# print(lst1)