#This program will define a function to check if the number is prime.


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
    
print(isprime(11))