#This program will check if the number is prime.

num = int(input("Enter the number\n"))
prime = True
for i in range(2,num):
    if(num%i) == 0:
        prime = False
        break

if prime:
    print(f"The number {num} is prime")
else:
    print(f"The number {num} is not prime")