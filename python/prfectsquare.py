import math
def isPerfectSquare(x):
	if(x >= 0):
		sr = int(math.sqrt(x))
		return ((sr*sr) == x)
	return false
x = 225
if (isPerfectSquare(x)):
	print("TRUE")
else:
	print("FALSE")
