#Find the gratest number from the four numbers
num1 = float(input("Enter the first number:\n"))
num2 = float(input("Enter the second number:\n"))
num3 = float(input("Enter the third number:\n"))
num4 = float(input("Enter the fourth number:\n"))

# if num1 > num2:
#     n1 = num1
# else:
#     n1 = num2

# if num3 > num4:
#     n2 = num3
# else:
#     n2 = num4

# if n1 > n2:
#     print(str(n1) + "is greatest")
# else:
#     print(str(n2) + "is greatest")

# Other way to do this by making list, tuple or set
#a = [num1, num2, num3, num4]
#a = (num1, num2, num3, num4)
a = {num1, num2, num3, num4}
print("The greatest number is",max(a))
print(type(a))