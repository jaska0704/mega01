# dct = {}
# for i in range(int(input(">>> "))):
#     a = input("Keyni kiriting: ")
#     dct[a] = input("Valueni kiriting: ")
# print(dct)
# student = {
#     "name"   : input("ismingizni kiriting: "),
#     "Familya" : input("Familyasini kiriting: "),
#     input(">>>> ") : int(input("Oxirgisi: "))
# }
# print(*student)
student = {
    'ism': '',
    'familya': '',
    'yoshi': 0
}
lst = []
for i in range(int(input("Nechta student kiritasiz: "))):
    lst.append(student.copy())
    for j in lst[i]:
        if isinstance(lst[i][j], int):
            lst[i][j] = int(input("Sonni kiriting: "))
        else:
            lst[i][j] = input()
print(lst)
    