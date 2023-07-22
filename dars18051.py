son1, son2 = 0, 1  #songacha bo'lgan fibonachchi sonlarni chiqarish
chegara=int(input(">>>> "))
# print(son1, end=" ")
# while son2<=chegara:
#         print(son2, end=" ")
#         son1, son2 = son2, son1+son2
i,m=2,0
while i<chegara:
    if chegara%i==0:
        m+=1
    i+=1
if m==0:
    print("tub son")
else:
    print("tub emas")