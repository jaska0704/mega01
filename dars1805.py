import os
os.system("cls")
"""son=int(input("sonni kiriting: "))
if son%3==0 and son%5==0: print("FizzBuzz")
elif son%3==0: print("Fizz")
elif son%5==0: print("Buzz")
else: print("FizzBuzz"[::-1])"""

a, n, m=(input()),0,0
i=0
while len(a)>i:
    if a[i].isdigit():
        n+=1
    elif a[i].isalpha():
        m+=1
    i+=1 
print("Raqam: ", n)
print("Harf: ", m)
