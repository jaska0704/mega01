class phone:
    def __init__(self,telefon) -> None:
        self.tel=telefon
        
class operator(phone):
    def __init__(self, telefon) -> None:
        super().__init__(telefon)
        for i in telefon:
            print(f'operator raqami {i[5:7]}')
class unical(phone):
    def __init__(self, telefon:list) -> None:
        self.b=telefon
        for i in self.b:
            for j in i[8:].split():
                 for v in j:
                    if self.b.count((v))==1:
                        print(i)
                    
                   
phones=[
'+998 33 651 31 24',
'+998 33 677 41 04',
'+998 33 566 62 04',
'+998 33 742 82 45',
'+998 62 299 67 26',
'+998 33 554 13 04',
'+998 55 909 84 80',
'+998 90 474 95 41',
'+998 90 061 55 33',
'+998 88 796 23 94',
'+998 33 571 33 62',
'+998 33 404 57 99',
'+998 33 301 37 38',
'+998 88 117 73 49',
'+998 33 211 04 23',
'+998 55 906 58 43',
'+998 55 909 42 11',
'+998 33 835 00 54',
'+998 62 299 75 40',
'+998 88 621 52 65',
'+998 88 895 68 28',
'+998 88 605 56 87',
'+998 71 982 19 12',
'+998 33 124 79 13',
'+998 88 636 74 68',
'+998 55 903 88 20',
'+998 33 297 52 01',]
a=phone(phones)
a1=operator(phones)
a2=unical(phones)


# 2 masala
# class ism:
#     def __init__(self,ism:list) -> None:
#         self.ism=ism
#     def saralash(self):
#         self.ism=(sorted(self.ism, key=lambda x: x.split()[1]))
#         print(self.ism)               
# Names=[
# 'Vivian Kidd',
# 'Bradyn Grant',
# 'Alexis Strickland',
# 'Madeleine Dunn',
# 'Emanuel Deleon',
# 'Charlotte Moody',
# 'lan Wells',
# 'Greyson Sellers',
# 'Abril Cordova',
# 'Julissa Wolf',
# 'Gabrielle Osborne',
# 'Brian Webster',
# 'Ethen Charles',
# 'Ashtyn Cowan',
# 'Brycen Benson',
# 'Thomas Sexton',
# 'Brynlee Park',
# 'Keaton Pena',
# 'Lily Ochoa',
# 'Jaycee Glass',
# 'Anderson Stark',
# 'Alexandria Harper',
# 'Derek Cooley',
# 'Savannah Coleman',
# 'Chase Cantu',
# 'Maverick Gonzales',
# 'Wyatt Browning', 
# 'Brenden Walter' ]
# a1=ism(Names)
# a1.saralash()