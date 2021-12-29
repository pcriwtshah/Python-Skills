#This program will define a function to check if the number is prime.

#Defining the function

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
