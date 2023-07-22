import os
os.system("cls")

#R1.berilgan set va listni qo'shish
# lst = ["blue", "green", "red"]
# st = {"yellow", "orange", "black"}
# st=st.union(lst)
# print(st)

#R2.ikkita setda ham bor qiymatlarni chiqarish
# set1 = {10,20,30,40,50}
# set2 = {30,40,50,60,70}
# print(set1.intersection(set2))

#R3.
# set1 = {10,20,30,40,50}
# set2 = {30,40,50,60,70}
# print(set1.union(set2))

#R4.berilgan listlarni dictga o'tkazish
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# k=0
# for i in range(len(keys)):
#     keys[i]=keys[i]+" "+str(values[i])
#     keys[i]=keys[i].split()
# print(dict(keys))

#R5
# sampleDict = {
#     "class":{
#         "student":{
#             "name":"Mike", "marks":{
#                 "physics":70, "history":80
#             }
#         }
#     }
# }
# print(sampleDict["class"]["student"]["marks"]["history"])

#R6.dictdan kerakli valueni topish
# sampleDict = {'a':100, 'b':200, 'c':300}
# for i in sampleDict:
#     if sampleDict[i]==200:
#         print('Bor')
#     else:
#         print("yo'q")

#R7.dictda keylarini almashtirib quyish 
# sampleDict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }
# sampleDict["location"]=sampleDict.pop("city")
# print(sampleDict)

#R8. listni dictga aylantirish
# lst = [
#      [1, 'Jean Castro', 'V'],
#      [2, 'Lula Powell', 'V'],
#      [3, 'Brian Howell', 'VI'],
#      [4, 'Lynne Foster', 'VI'],
#      [5, 'Zachary Simon', 'VII']
# ]
# dct={}
# for i in lst:
#     dct[i[0]]=[i[1],i[2]]
# print(dct)

#R9
# USER ={
#     "LOGIN": "Jonilider",
#     "PASSWORD": "olmacha246",
#     "NAME": "Zohir",
#     "AGE": 32
# }
# user = {
#     'Adress': {
#         'City': 'Navoiy',
#         'Street': 'Saroy',
#         'Hous': 'Kumushkon 35'
#     }
# }
#F
# log,pas = input("Login: "), input("Password: ")
# if log==USER["LOGIN"] and pas==USER["PASSWORD"]:
#     print()
#     print(f'''
#     Login: {USER["LOGIN"]}
#     Password: {USER["PASSWORD"]}
#     Name: {USER["NAME"]}
#     Age: {USER["AGE"]}
#     ''')
# else:
#     print("Qayta urunib ko'ring")
#     print()
# USER["Status"]="Active" #c
# USER["AGE"]=USER["AGE"]+1 #d
# USER.pop("Status") #g
# USER.update(user) #e
# USER.popitem() #i
# print(USER)

#j,k
# Foods = {
#     'osh': 25000,
#     'kabob': 16000,
#     'dimlama': 20000,
#     'mastava': 18000,
#     'lagmon': 23000
# }
# sum=0
# for i in Foods:
#     sum+=Foods[i]
# print(sum)

#R13
# lst = [9,9,9,9]
# natija=0
# for i in lst:
#     natija=natija*(10**len(str(i)))+i
# natija=natija+1
# natija=(" ".join(str(natija))).split()
# print(natija)

#amaliyot 1-masala
# lst = [(1,2),(2,3),(3,4)]
# for i in range(len(lst)):
#     lst[i]=list(lst[i])
# print(lst)

#2-masala
# lst = [(1,2),(2,3),(3,4)]
# lst1=[]
# for i in range(len(lst)):
#     lst[i]=list(lst[i])
#     lst1.append(sum(lst[i]))
# print(lst1)

#3-masala
# dct = {1: 10, 2: 20, 3:30, 4: 15, 5: 25}
# dct.pop(max(dct, key=dct.get))
# dct.pop(min(dct, key=dct.get))
# print(dct)

#4-masala
# dict1 = {1:10, 2:20}
# dict2 = {3:30, 4:40}
# dict3 = {9:90, 7:70}
# dct = {**dict1, **dict2, **dict3}
# print(dct)

#5-masala
# dct = {'data1':100,'data2':-54,'data3':247}
# print(sum(dct.values()))

# Data = [{
#   "model": "RDX",
#   "year": 2009
# }, {
#   "model": "LS",
#   "year": 2000
# }, {
#   "model": "GLK-Class",
#   "year": 2010
# }, {
#   "model": "Express 1500",
#   "year": 2005
# }, {
#   "model": "LR2",
#   "year": 2008
# }, {
#   "model": "XF",
#   "year": 2012
# }, {
#   "model": "MR2",
#   "year": 2005
# }, {
#   "model": "Malibu",
#   "year": 2007
# }, {
#   "model": "M-Class",
#   "year": 2010
# }, {
#   "model": "Routan",
#   "year": 2011
# }]
# sort_data = sorted(Data, key=lambda x: x['year'])
# for i in sort_data:
#     print(i['model'], i['year'])

data = [
    {"full_name":"Eugene Elsmor","company":"Kazu","position":"Electrical Engineer","salary":"$4440.86"},
    {"full_name":"Joni Stredder","company":"JumpXS","position":"Environmental Tech","salary":"$870.05"},
    {"full_name":"Terri-jo Fulham","company":"Tagchat","position":"Assistant Media Planner","salary":"$1992.55"},
    {"full_name":"Priscilla Pandya","company":"Youopia","position":"Help Desk Operator","salary":"$3715.95"},
    {"full_name":"Wolfy Swanborough","company":"Topiclounge","position":"Recruiter","salary":"$1045.61"},
    {"full_name":"Raleigh Ratter","company":"Zoozzy","position":"Graphic Designer","salary":"$602.41"},
    {"full_name":"Anastasia Winward","company":"Avaveo","position":"Cost Accountant","salary":"$3641.42"},
    {"full_name":"Dorry Vasyunichev","company":"Fivebridge","position":"Junior Executive","salary":"$2035.05"},
    {"full_name":"Richy Cleft","company":"Jamia","position":"Sales Associate","salary":"$912.98"},
    {"full_name":"Zack Record","company":"Oyonder","position":"Social Worker","salary":"$2492.23"},
    {"full_name":"Lissy Newns","company":"Riffwire","position":"Developer II","salary":"$1177.79"},
    {"full_name":"Audrye Churchyard","company":"Photospace","position":"Environmental Tech","salary":"$4125.83"},
    {"full_name":"Timothy Seligson","company":"Riffpath","position":"Compensation Analyst","salary":"$1271.94"},
    {"full_name":"Brandie Rogeon","company":"Riffpath","position":"Analyst Programmer","salary":"$1911.09"},
    {"full_name":"Dane Rugg","company":"Twimm","position":"Associate Professor","salary":"$2200.72"},
    {"full_name":"Mick Jeduch","company":"Realblab","position":"Executive Secretary","salary":"$1154.20"},
    {"full_name":"Rowland Christofol","company":"Mycat","position":"Senior Cost Accountant","salary":"$1119.94"},
    {"full_name":"Sibella Abrahams","company":"Minyx","position":"Internal Auditor","salary":"$4023.25"},
    {"full_name":"Layne Thomel","company":"Centimia","position":"Research Associate","salary":"$4073.17"},
    {"full_name":"Demetris Clemenzi","company":"Tagopia","position":"Human Resources Manager","salary":"$1530.37"},
    {"full_name":"Kerstin Devon","company":"Katz","position":"Senior Quality Engineer","salary":"$1305.61"},
    {"full_name":"Brandon Burgwyn","company":"Mydeo","position":"Physical Therapy Assistant","salary":"$1325.58"},
    {"full_name":"Dyana Crosby","company":"BlogXS","position":"Payment Adjustment Coordinator","salary":"$1501.54"},
    {"full_name":"Harald Voller","company":"Riffpedia","position":"Accountant I","salary":"$4397.60"},
    {"full_name":"Nollie Phipard-Shears","company":"Aimbo","position":"Legal Assistant","salary":"$3172.57"},
    {"full_name":"Gaynor Dannohl","company":"Leexo","position":"Administrative Assistant II","salary":"$3035.89"},
    {"full_name":"Tome Bensen","company":"Yamia","position":"Assistant Professor","salary":"$3677.10"},
    {"full_name":"Jessey Anshell","company":"Bubblemix","position":"Registered Nurse","salary":"$2782.66"},
    {"full_name":"Valentijn Melbury","company":"Bluejam","position":"Statistician I","salary":"$1308.43"},
    {"full_name":"Rochelle Andrejevic","company":"Rhyzio","position":"VP Product Management","salary":"$1734.61"}
]
# a = float()
# lst = []
# for i in data:
#     for j in i.items():
#         if j[0]=='salary':
#             if float(a)<float(j[1][1:]):
#                 a = float(j[1][1:])
#                 print(a)

#                 b=i
# print(f"Eng katta oylik oluvchi shaxs {b}\nva uning oyligi: {a}")


# dct={}
# for i in data:
#     for j in i.items():
#         if j[0]=='salary':
#             key=float(j[1][1:])
#             dct[key]=i
# dct=(sorted(dct.items(), key=lambda x:x[0], reverse=True))
# n=0
# for k in dct:
#     if n<5:
#         print(f"eng katta oylik oluvchi {n+1}chi kishi {k[1]}")
#         n+=1


# dct={}
# for i in data:
#     for j in i.items():
#         if j[0]=="salary":
#              dct[float(j[1][1:])]=i
# print(f"Eng kam oylik oluvchi kishi {min(dct:=(sorted(dct.items(), key=lambda x: x[0])))[1]}")


# dct={}
# for i in data:
#     for j in i.items():
#         if j[0]=="salary":
#             dct[float(j[1][1:])]=i
# dct=sorted(dct.items(), key=lambda x: x[0])
# for k in dct:
#     if k[0]<1000:
#         print(f"Oyligi 1000$ dan kam ishchiga 1000$ topishi uchun {int(1000-k[0])}$ yetmaydi.")


# dct=[]
# for i in data:
#     for j in i.items():
#         if j[0]=="salary" and float(j[1][1:])<1000:
#             print(float(j[1][1:])+1000)