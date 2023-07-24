import time
import random

class Pult():
    def __init__(self, tv_holat='Off', tv_ovoz=0, kanal_list = ['BBC', 'MY5', 'FTV', 'Yoshlar', 'Sport TV'], kanal='BBC') -> None:
        print("Pult kiritilmoqda.....")
        self.tv_holat=tv_holat
        self.tv_ovoz=tv_ovoz
        self.kanal_list=kanal_list
        self.kanal=kanal
    
    def __str__(self) -> str:
        return f"""Tv Holati: {self.tv_holat}
Ovozi: {self.tv_ovoz}
Kanal Listi: {self.kanal_list}
Hozirgi kanal: {self.kanal}"""
    
    def ovoz_ozgartirish(self):
        while True:
            soniya = 5
            belgi = input("+ || - birini tanlang")
            if belgi=="+":
                if self.tv_ovoz <= 5:
                    self.tv_ovoz += 1
                    print(f"Ovoz -- {self.tv_ovoz}")
                    soniya = 5
                    continue
            elif belgi == "-":
                if self.tv_ovoz != 0:
                    self.tv_ovoz -= 1
                    print(f"Ovoz -- {self.tv_ovoz}")
                    soniya = 5
                    continue
            else:
                print("Ovoz yangilash tugatildi.")
                break
            for i in range(5):
                time.sleep(1)
                soniya -=1
                print(".")
            if soniya <= 0:
                print("#---------------------------#")
                break
    
    def tv_power(self):
        if self.tv_holat == "On":
            print("Tv o'chirilmagan........")
            self.tv_holat = "Off"
        else:
            print("Tv yoqilmagan.......")
            self.tv_holat = "On"

    def random_kanal(self):
        random_kanal = random.randint(0, len(self.kanal_list)-1)
        self.kanal = self.kanal_listP(random_kanal)
        