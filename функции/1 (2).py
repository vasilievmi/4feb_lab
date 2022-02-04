def IsPointInSquare(x, y):
    return abs(x) <= 1 and abs(y) <= 1
x = 3
y = -7
print(IsPointInSquare(x, y))