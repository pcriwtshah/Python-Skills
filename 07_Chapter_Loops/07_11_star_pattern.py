num = int(input("How many lines of pattern do you need?"))

for i in range(1 , num +1):
    print("*"*i)
print("\n")
n =6
for i in range(n):
    print(" " * (n-i-1), end="")
    print("*" * (2*i + 1), end="")
    print(" " * (n-i-1))