total = 44
rez = (total * 0.8).__round__()
print("Для успешного окончания курса надо сдать {} домашек".format(rez))
assert rez == 35
