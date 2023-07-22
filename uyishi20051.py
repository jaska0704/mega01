lst = [[], [1,2,3], [], [2,0,1,[]]]
for i in lst:
    if len(i)==0:
        for j in i:
            if len(j)==0:
             i.remove(j)
        lst.remove(i)
        
print(lst)