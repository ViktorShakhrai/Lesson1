total = 44
rez = (total * 0.8).__round__()
print("Для успешного окончания курса надо сдать {} домашек".format(rez))
assert rez == 35

x1 = 1
y1 = 4
x2 = 4
y2 = 6
import  math
distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
print("Відстань між двома точками дорівнює:",distance.__round__(2))

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
print(f"Привіт{name},як справи?")


price = 12
weight = 3.4121
rez = 0
rez = str((price * weight).__round__(2))
rez = "Итого: "+ rez
print(rez)
assert rez == 'Итого: 40.95'

