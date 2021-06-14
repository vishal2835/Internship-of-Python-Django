x = int(input("Enter the value of x?"))  
y = int(input("Enter the value of y?"))  
print("before swapping numbers x and y: %d   %d\n" %(x,y))  
#swapping without using third variable#  
x = x + y     
y = x - y    
x = x - y     
print("After swapping numbers x and y: %d   %d\n"%(x,y))  