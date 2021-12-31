#This program will calculate the sum of first n natural numbers.

num = int(input("Enter the number: "))
sum = 0
for i in range(1, num + 1):
    sum = sum + i

print(f"The sum of first {num} natural number is {sum}")