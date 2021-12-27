def abs(x):
    if x >= 0:
        a = x
    else:
        a = -1*x
    return a
num = int(input("Enter the number\n"))
print("The absolute value of", num, "is", abs(num))

'''
float has issue with - and int has issue with decimal numbers
'''