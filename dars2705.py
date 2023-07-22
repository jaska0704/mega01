# def sum_dict(d1, d2):
#     for i in d2:
#         if i in d1:
#             d1[i]+=d2[i]
#         else:
#             d1[i]=d2[i]
#     return d1
# d1={'a':100,'b':200,'c':300}
# d2={'a':300,'b':200,'d':400}
# print(sum_dict(d1,d2))


# def son(n):
#     if n==int(str(n)[::-1]):
#      return "Polindrom son"
#     else:
#      return "Polindrom son emas" 
# print(son(int(input(">>> "))))


# def uzgargan_son(k:int, n:int):
#     print(int(str(k)+str(n)))

# uzgargan_son(4, 6789)

# def suzlar(ab):
#     for i in range(3):
#         suz=input("soz kirit: ")
#         if suz in ab:
#             print(ab)
#             ab=ab.replace(suz, '*'*len(suz))
#     return ab
# print(suzlar("salom bolalar kimdur jama nimadur qachon sen va u kim jamshid"))

# def son(n):#kiritilgan sonni bir xona bir xona surib chop etish
#     num=str(n)
#     for i in range(len(num)):
#         print(int(num[i:]+num[:i]), end=", ")

# son(int(input("Sonni kiriting: ")))
# def roman_numeral(number):
#     roman_map = { 1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I' }
#     result = ''
#     for value, i in roman_map.items():
#         count = number // value
#         result += i * count
#         number -= value * count
#     return result

# # num = input("Istalgan son kiriting: ")
# # num_str = str(num)
# print(roman_numeral(int(input("<>>> "))))
# number=31
# roman_map = { 1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I' }
# result = ''
# for value, i in roman_map.items():
#     count = number // value
#     result += i * count
#     number -= value * count
#     print(number)
# print(result)