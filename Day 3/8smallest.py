# Python program to find the
# minimum of two numbers


def minimum(a, b):
	
	if a <= b:
		return a
	else:
		return b
	
# Driver code
a = int(input("Enter a number: ")) 
b = int(input("Enter a number: ")) 
print(minimum(a, b))
