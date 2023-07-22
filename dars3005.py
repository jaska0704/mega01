# Lst = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'L', 'Q', 'U']
# def listni_bolish(n, lst):
#     return[lst[i:i+n] for i in range(0, len(lst), n)]

# chegara = int(input("Listni bo'lish uchun raqamni kiriting: "))
# new_list = listni_bolish(chegara, Lst)
# print(new_list)
def vpn(n:int):
    lst = []
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            lst.append("FizzBuzz")
        elif i % 3 == 0:
            lst.append("Fizz")
        elif i % 5 == 0:
            lst.append("Buzz")
        else:
            lst.append(str(i))
    return lst
