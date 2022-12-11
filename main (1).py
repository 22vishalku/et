import math
def isPerfectSquare(x):
	s = int(math.sqrt(x))
	return s*s == x
def isFibonacci(n):
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)
number=input().split(",")
number=[int(item) for item in number]
for i in number:
    if (isFibonacci(i) == True):
        print(i, "Valid")
    else:
        print(i, "Not Valid")

