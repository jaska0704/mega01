# a=input("a ga qiymat bering: ")
# n=int(input("n ga qiymat bering: "))

# sum=0
# for i in range(1, n+1):
#     box = int(a * i)
#     sum+=box
# print(sum)


# a=input("a ga qiymat bering: ")
# n=int(input("n ga qiymat bering: "))

# sum=0
# for i in range(1, n+1):
#     sum+=int(a*i)
#     print(a*i, end=" ")
#     if i<n:
#         print("+", end=" ")
#     else:
#         print("= ", sum)


# son = input("Sonni kiriting: ")
# daraja = len(son)
# sum=0
# for i in range(daraja):
#     sum += pow(int(son[i]), daraja)

# if sum == int(son):
#     print(True, sum)
# else:
#     print(False, sum)


# import random
# secret_number = random.randint(1, 101)
# imkoniyat = 0
# lamp = True

# while lamp:
#     son = int(input("Songa qiymat bering: "))
#     if imkoniyat > 5:
#         print("imkoniyatingiz tugadi")
#         imkoniyat = 1
#         print()
#         son = int(input("Qaytadan o'ynaysizmi? yes[1] no[0]"))
#         if son == 1:
#             secret_number = random.randint(1, 101)
#             continue
#         else:
#             break

#     if secret_number == son:
#         print("Shapaloqlar topdiz tabriklaymiz")
#         print(f"Siz {imkoniyat} da topdingiz!!!")
#         imkoniyat = 1
#         print()
#         son = int(input("Qaytadan o'ynaysizmi? yes[1] no[0]"))
#         if son == 1:
#             secret_number = random.randint(1,101)
#             continue
#         else:
#             lamp = False
#     elif secret_number < son:
#         imkoniyat += 1
#         print("Kichikroq son kiriting")
#         print()
#     else:
#         imkoniyat += 1
#         print("Kattaroq son kiriting")
#         print()
# sonni topish o'yini