'''
def isprime(x):
    for i in range(2,x):
        if x%i == 0:
            print(x, "is not prime")
        else:
            i += 1
    else:
        print(x, "is prime")

isprime(5)
isprime(4)
isprime(3)
isprime(2)
isprime(1)
isprime(6)
'''
"DO NOT PUT PRINT() IN DEF; NOT WORKING"

num = int(input("Enter the number\n"))

def isprime(x):
    prime = True
    for i in range(2, x):
        if(num%i) == 0:
            prime = False
            break

    if prime:
        #y = f"The number {num} is prime"
        return 'Prime'
    else:
        #y = f"The number {num} is not prime"
        return 'Not Prime'

print(f'The {num}' is {isprime(num)})