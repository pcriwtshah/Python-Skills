#n! = n*(n-1)!
#Defining the function
def factorial_recursive(n):
    if n==1 or n==0:
        return 1
    return n*factorial_recursive(n-1)

#Using the function
print(factorial_recursive(6))
