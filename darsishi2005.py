abs=[12, 67, 45, 34, 1, 2, "salom", 6]
max,min,sum=abs[0],abs[0],0
for i in abs:
    if isinstance(i, int):
        if min>i:
           min=i
        elif max<i:
            max=i
        sum+=i
print(sum)
print(max)
print(min)