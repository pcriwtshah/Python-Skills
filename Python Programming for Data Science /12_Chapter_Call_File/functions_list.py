#Defining the square root function
def sqrt(number):
    '''Return the square root of a number'''
    b=0
    while b*b <= number:
        c = b
        b +=0.001
    return round(c,3)

#Defining the function
def curt(number):
    '''Return the cube root of a number'''
    b=0
    while b*b*b <= number:
        c = b
        b +=0.001
    return round(c,3)

#Define the square function
def sq(x):
    '''Return the square of a number'''
    x = x*x
    return x

#Defining the factorial function
def factorial(n):
    '''Return the factorial of a number'''
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product

#This function will check if the number is prime.
def isprime(x):
    '''
    if x == 2:
        a = 'prime'
        break
    '''
    for i in range(2,x):
        if x%i == 0:
            a = 'not prime'
            break
        else:
            a = 'prime'
    return a

#Defining the sum function
def sum(a,b):
    return a+b

#Defining the absolute value function
def abs(x):
    if x >= 0:
        a = x
    else:
        a = -1*x
    return a