x = input()
y = []
y.extend(x)
while '@' in y:
	y.remove('@')
print(*y, sep='')	






