"""a) Make a simple calculator menu driven that can add, subtract, multiply
And divide using function.
b) To find factorial of a number using recursive function
c) To print Fibonacci series
i) using normal function
ii) using recursive function
c) Program to find max of two numbers using lambda function.
d) Write a program to print Employee information(use object variables
and class variables)"""


def add(a, b):  
    sum = a + b  
    print(a, "+", b, "=", sum)

def sub(a, b):  
    diff = a - b  
    print(a, "-", b, "=", diff)

def mul(a, b):  
    product = a * b  
    print(a, "*", b, "=", product)

def div(a, b):  
    quotient = a / b  
    print(a, "/", b, "=", quotient)  

while True:
    print("Choose the operation to be performed")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exit")
    opt=int(input("Enter the choice number:"))

    if opt == 1:
        a = int( input("Enter First Number: "))  
        b = int( input("Enter Second Number: "))  
        add(a, b)

    elif opt == 2:
        a = int( input("Enter First Number: "))  
        b = int( input("Enter Second Number: "))  
        sub(a, b)

    elif opt == 3:
        a = int( input("Enter First Number: "))  
        b = int( input("Enter Second Number: "))  
        mul(a, b)

    elif opt == 4:
        a = int( input("Enter First Number: "))  
        b = int( input("Enter Second Number: "))  
        div(a, b)    

    elif opt == 5:  
        break  
      
    else:  
        print( "Please enter a valid Input from the list")



        
