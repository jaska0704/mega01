Morse = {"-----": "0", ".----": "1", "..---": '2',
         "...--": "3", "....-": '4', ".....": '5',
         "-....": '6', "--...": '7', "---..": '8',
         "----.": '9'}
lst = "..--- ----- .---- ---.."

natija = ""
for i in lst.split():
    natija += Morse[i]
print(natija)
