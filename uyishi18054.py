import random
i=1
while i<=3:
    if int(input("Sonni kiriting: "))==random.randint(1,5):
        print("Winner")
        break
    else:
        print("Looser")