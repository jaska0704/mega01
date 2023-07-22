# s=input()#so'zda har bir harfning nechtaligini hisoblaydi
# d={}
# for i in s:
#     if i.isalpha:
#       d[i] = d.get(i, 0)+1
# for i in sorted(d):
#     print(i, d[i])

# contacts = {
#     'John Kennedy': {
#         'birthday': "29 may 1917", "city": "Brookline",
#         'phone': None, 'children': 5
#     },
#     "Arnold Schwarzenegger": {
#         'birthday': "30 july 1947", 'city': "Gradec",
#         'phone': "555-555-555", 'children': 3
#     },
#     "Donald Trump": {
#         'birthday': "14 july 1946", 'city': "New York",
#         'phone': "777-777-777", 'children': 4
#     }
# }
# kishilar = ['John Kennedy', "Arnold Schwarzenegger", "Donald Trump"]
# for shaxs in kishilar:
#     # city = contacts[shaxs]["city"]
#     # birthday = contacts[shaxs]["birthday"]
#     # phone = contacts[shaxs]["phone"]
#     # children = contacts[shaxs]["children"]
#     print(shaxs)
#     for data in contacts[shaxs]:
#         print(data, ':', contacts[shaxs][data])

# a=[1, 'hello', 3, [10,20,30], False, 5]
# b=tuple([1, 'hello', 3, [10,20,30], False, 5])
# print(a.__sizeof__())
# print(b.__size

lst = ['salom','kim','nima']
lst2 = ['23','24','32']
for i in range(len(lst)):
    dct = {lst[i] = lst2[i]}
print(dct)