total = 44
rez = (total * 0.8).__round__()
print("Для успешного окончания курса надо сдать {} домашек".format(rez))
assert rez == 35

x1, y1 = 1, 4
x2, y2 = 4, 6

import math
distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
print("Відстань між двома точками дорівнює:", distance.__round__(2))

var1 = 'pyThoN'
var1 = var1.lower().capitalize()
assert var1 == 'Python'
var1 = var1.upper()
assert var1 == 'PYTHON'
var1 = var1.lower()
assert var1 == 'python'
var1 = " python "
var1 = var1.strip()
assert var1 == 'python'

name = "Viktor"
print("Привет "+name)
print(f"Привіт {name},як справи?")
print("Це форматування за допомоги {0} формат".format("методу"))
print("Це моє ненависне %s" % "форматування")


price = 12
weight = 3.4121
rez = 0
rez = str((price * weight).__round__(2))
rez = "Итого: " + rez
print(rez)
assert rez == 'Итого: 40.95'

number = 12
username = "ираклий"
access_mask = 54
hour_price = 15.321
rez = 0
username = username.capitalize()
def dec_to_bin(access_mask):
    dec = access_mask
    bin = ''
    while dec > 0:
       bin = str(dec % 2) + bin #Число діиться на 2,решта від ділення перетворюється на сторку і записується в змінну {bin},[%]-рета з ділення
       dec = dec // 2           #В змінну {dec} pаписується ціле число з поділу цьго числа на 2.[//]-Цільсний поділ.
    return(bin)                 #Функція повертає отримане число але в бінарному коді
access_mask = dec_to_bin(access_mask)
hour_price = str(hour_price.__round__(2))
number = str(number).zfill(6)
rez = (number + " " + username + " " + access_mask + " " + hour_price)
print(rez)
assert rez == '000012 Ираклий 110110 15.32'


