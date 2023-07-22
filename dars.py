natija = "salom bolalar kim nima qachon".split()
print(natija)
a=[2,2,2]
if len(a)!=1 and min(a)!=max(a):
   for i in a:
      if i==max(a):
        a.remove(i)
   print(max(a))
else:
    print("None")
lst=list()
for i in range(10):
    lst.append(int(input()))
print(lst)
n=int(input("satrni kirgizing: "))
m=int(input("chegarani kiriting: "))
while n<m:
    lst[n], lst[m] = lst[m], lst[n]
    n+=1
    m-=1
print(lst)
#lst=[[10,20], [40], [30,56,25], [10,20], [33], [40]]
# for i in lst:
#     if lst.count(i)>1:
#         lst.remove(i)
# print(lst:=sorted(lst))