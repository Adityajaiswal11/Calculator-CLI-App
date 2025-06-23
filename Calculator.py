import math
print("\t_____CALCULATOR_____")

#function for addition
def sum(a,b):
    a+=b
    return a

#function for subtraction
def sub(a,b):
    if a>b:
        a-=b
        return a
    else:
        b-=a
        return b

#function for multiplication
def mul(a,b):
    a*=b
    return a

#function for division
def div(a,b):
    q=a/b
    r=a%b
    print("\nThe quotient is : %s" %q)
    print("\nThe remainder is : %s" %r)

#function for Squareroot
def sqr(a):
    x= math.sqrt(a)
    return x

while(True):
    print("\n\nChoose the operation you want to perform: ")
    print("\n\t1.Addition")
    print("\n\t2.Subtraction")
    print("\n\t3.Multiplication")
    print("\n\t4.Division")
    print("\n\t5.Square Root")
    print("\n\t6.Exit")

    choice = int(input('>'))

    if choice==1:
        print("\n\nEnter the two Numbers: ")
        num1 = int(input('>'))
        num2 = int(input('>'))
        s=sum(num1,num2)
        print("The sum is : %s" %s)

    if choice==2:
        print("\n\nEnter the two Numbers: ")
        num1 = int(input('>'))
        num2 = int(input('>'))
        m=sub(num1,num2)
        print("The difference is : %s" %m)

    if choice==3:
        print("\n\nEnter the two Numbers: ")
        num1 = int(input('>'))
        num2 = int(input('>'))
        p=mul(num1,num2)
        print("The product is : %s" %p)

    if choice==4:
        print("\n\nEnter the two Numbers: ")
        num1 = int(input('>'))
        num2 = int(input('>'))
        d=div(num1,num2)
        print("The sum is : %s" %d)

    if choice==5:
        print("\n\nEnter the Number: ")
        num1 = int(input('>'))
        r=sqr(num1)
        print("The sum is : %s" %r)

    if choice==6:
        print("\nYou Choose to Exit.Bye....")
        break
        






