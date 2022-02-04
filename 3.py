import math
strC = input("Введите строку-> ")
strC1 = strC[-(int(len(strC)/2))::]
strC2 = strC[0:math.ceil((len(strC)/2)):]
print(strC1+strC2)

