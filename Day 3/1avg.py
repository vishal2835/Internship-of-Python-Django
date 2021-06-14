# Python program to find average of five numbers using function by vishal prajapati

def avg_num(num1, num2, num3, num4, num5):   #user-defined function
    avg = (num1 + num2 + num3+ num4 + num5) / 5   #calculate average
    return avg    #return value

# take inputs
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))
num3 = float(input('Enter third number: '))
num4 = float(input('Enter four number: '))
num5 = float(input('Enter fifth number: '))

# function call
average = avg_num(num1, num2, num3, num4, num5)

# display result
print('The average of numbers = ',average)