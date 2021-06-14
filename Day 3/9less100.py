num = int(input("Enter a number: "))
mod = num % 2
if num<100:

    if mod > 0:
            print("This is an odd number.")
    else:
            print("This is an even number.")
    
else:
            print("number is greater than or equal to 100")