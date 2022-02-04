import math
def distance(x1, y1, x2, y2):
    r = (x1-x2)**2+(y1-y2)**2
    return math.sqrt(r)
x1 = 0
y1 = 0
x2 = 1
y2 = 1
print(distance(x1, y1, x2, y2))