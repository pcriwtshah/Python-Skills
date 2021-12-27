#This program will define a function to check if the number is prime.

#Defining the function
'''
# NOT WORKING
def isprime(x):
    for i in range(2,x):
        if x%i == 0:
            print(x, "is not prime")
            break
        else:
            print(x, "is prime")
'''
def isprime(x):
    i = 2
    while i < x:
        if x%i == 0:
            p = "is not prime"
        else:
            i += 1
    else:
        p = "is prime"
    return p    

print(isprime(11))













'''
Write a function to print all the prime numbers between two numbers
'''