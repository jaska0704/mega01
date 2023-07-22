import os
os.system("cls")
# n=int(input("Sonni kiriting: "))
# for i in range(n):
#     print('|' + " "*i + "\\")
# print("|" + "_"*n + "\\")

# masala if1
# n=int(input("Sonni kiriting: "))
# if n>0:
#     print(n+1)
# else:
#     print(n)

# masala if2
# n=int(input("Sonni kiriting: "))
# if n>0:
#     print(n+1)
# else:
#     print(n-2)

# n=int(input("Sonni kiriting: "))
# if n>0:
#     print(n+1)
# elif n<0:
#     print(n-2)
# else:
#     print(n=10)

# masala if4
# a,b,c = int(input("a sonni kiriting: ")),int(input("b sonni kiriting: ")),int(input("c sonni kiriting: "))
# count=0
# if a>0: count+=1
# if b>0: count+=1
# if c>0: count+=1
# print(count)

# masala if5
# a,b,c = int(input("a sonni kiriting: ")),int(input("b sonni kiriting: ")),int(input("c sonni kiriting: "))
# count, manfiy=0, 0
# if a>0: count+=1
# else: manfiy+=1
# if b>0: count+=1
# else: manfiy+=1
# if c>0: count+=1
# else: manfiy+=1
# print(f"musbatlar: {count}\nmanfiylar: {manfiy}")

# masala if6
# a,b=int(input("a sonni kiriting: ")), int(input("b sonni kiriting: "))
# if a>b: print(a)
# else: print(b)

#masala if7
# a,b=int(input("a sonni kiriting: ")), int(input("b sonni kiriting: "))
# if a<b: print("kichik sonning tartib raqami: 1")
# else: print("kichik sonning tartib raqami: 2")

#masala if8 
# a,b=int(input("a sonni kiriting: ")), int(input("b sonni kiriting: "))
# if a<b: print(f"Katta: {b} va Kichik: {a}")
# else: print(f"Katta: {a} va Kichik: {b}")

# masala if9
# a,b=int(input("a sonni kiriting: ")), int(input("b sonni kiriting: "))
# if a>b:
#     a,b=b,a
#     print(f"A teng: {a}\nB teng: {b}")
# else: print(f"A teng: {a}\nB teng: {b}")

# vazifa 1
# for i in range(1, 801):
#     print(i)

# vazifa 2
# for i in range(1000, 0, -1):
#     print(i)

# vazifa 3
# for i in range(400, 501):
#     print(i)

# vazifa 4
# for i in range(300, 149, -1):
#     print(i)

# vazifa 5
# for i in range(250, -401, -1):
#      print(i)

# vazifa 6
# for i in range(-500, 201):
#      print(i)

# vazifa 7
# for i in range(1, 140):
#     if i%2==0:
#         print(i)

# vazifa 8
# for i in range(100, 240):
#     if i%2:
#         print(i)

# vazifa 9
# for i in range(40, 180):
#     if i%7==0:
#         print(i)

# vazifa 10
# for i in range(50, 440):
#     if i%11==0:
#         print(i)

# vazifa 11
# for i in range(1, 140):
#     if not i%5 and not i%9:
#         print(i)

# vazifa 12
# for i in range(1, 4000):
#     if not i%11 and not i%3 and not i%9:
#         print(i)

# vazifa 13
# for i in range(20, 420):
#     if not i%5 and i%10:
#         print(i)

# vazifa 14
# for i in range(1, int(input("sonni kiriting: "))):
#     print(i*i)

# vazifa 15
# n=int(input("sonni kiriting: "))
# for i in range(1, n):
#     if i*i<=n:
#         print(i*i)

#rasmdaki nol va birlar
# n=int(input(">>>>"))
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         if (i+j)%2==0:
#             print("1 ", end="")
#         else:
#             print("0 ", end="")
#     print()

#shaxmat doskasi  misoli
# son1=int(input("1 sonni kiriting: "))
# son2=int(input("2 sonni kiriting: "))
# if (son1+son2)%2==0:
#     print("oq")
# else:
#     print("qora")

#vazifa p2
# sum=0
# n=int(input("5 xonali son kiriting: "))
# for i in range(5):
#     sum+=n%10
#     n//=10
# print(sum)

# vazifa P3
# count=0
# for i in range(1,int(input("Sonni kiriting: "))):
#     if not i%2:
#         count+=1
# print(count)

# vazifa P4
# n, sum=int(input(">>>> ")), 0
# for i in range(n):
#     if i<n-1:
#         print("1"*(i+1) + "+", end="")
#     else:
#         print("1"*(i+1), end="")
#     sum+=int("1"*(i+1))
# print("=",sum)

# vazifa P5
# for i in range(1, 1001):
#     count=0
#     for j in range(1, i+1):
#         if i%j==0:
#             count+=1
#     if count==9:
#         print(i)

# vazifa P6
# for i in range(1, 100):
#     if str(i).count("3"):
#         print(i)

# for i in range(1, 1000):
#     sum=0
#     for j in range(1, i+1):
#         if not i%j:
#             sum+=j
#             som=0
#         for k in range(1, sum):
#             if not sum%k:
#                 som+=k
#     if som==i:
#         print(i, sum)  bu chiqmadi
