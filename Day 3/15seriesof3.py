# Python program to print all EVEN numbers within an interval
x = int(input("Enter the value of x?"))  
y = int(input("Enter the value of y?"))
if x%2==0:
	for num in range(x, y + 2, 3):
		print(num)
else:
	for num in range(x+1, y + 2, 3):
		print(num)
