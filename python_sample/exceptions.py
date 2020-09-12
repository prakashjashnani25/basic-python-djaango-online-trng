import sys

try:
	x = int(input("X: "))
	y =int(input("y: "))
except ValueError:
	print("Error : Enter  Numberr Only")
	sys.exit(2)

try:
	result = x/ y
except ZeroDivisonError:
	print("Error: Cannot Divide by 0.")
	sys.exit(1)

print(x," / " ,y ,"=",result)


