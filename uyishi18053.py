# while i<=n:
#     i=j
#     while j>0:
#         j-=2
#     if j==1:
#         print(i)
#     i+=1
# for i in range(2,int(input("Sonni kiriting: "))+1):
#     j=i
#     while j>1:
#         j-=2
#     if j==1:
#         print(i)
text = input("Matnni kiriting: ")
numbers = [word for word in text if word.isdigit()]
if numbers:
    print("Matnda quyidagi sonlar mavjud: ")
    for number in numbers:
        print(number)
else:
    print("Matnda hech qanday son topilmadi.")