'''
Write a function to print all the prime numbers between two numbers
'''
#NOT WORKING as expected
def prime(a,b):
    n =[]
    i = 2
    for x in range(a,b+1):
        while i < x:
            if x%i == 0:
                p = "is not prime"
                
            else:
                i += 1
        else:
            prime = True
            #p = "is prime"
            if prime:
                n.append(x)
    return n

print(prime(3, 7))