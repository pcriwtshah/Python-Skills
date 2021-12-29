# Find the square root
a = float(input("Enter the number to find the square root: "))
#a = float(raw_input("Enter the number to find the square root: "))
b = 0
while b*b <= a: #b**2
    c = b
    b += 0.001
#print("The square root of ", a, " is ", round(c))
print("The square root of %r is %r" %(a, round(c,3)))

# Find the cube root
a = float(input("Enter the number to find the cube root: "))
#a = float(raw_input("Enter the number to find the cube root: ")) #raw_inpu in python 2x
b = 0
while b*b*b <= a: #b**3
    c = b
    b += 0.001
#print("The cube root of " , a, " is ", round(c))
print("The cube root of %r is %r" %(a, round(c, 3)))
'''
Why would I use %r over %s?
Remember, %r is for debugging and is “raw representation” 
while %s is for display. I will not answer this question 
again, so you must memorize this fact. This is the #1 thing 
people ask repeat- edly, and asking the same question over 
and over means you aren’t taking the time to memorize what 
you should. Stop now, and finally memorize this fact.
'''

# # Practice with def to find the square root
# def sqrt(number):
#     b=0
#     while b*b <= number:
#         c = b
#         b +=0.001
#     print(round(c,3))

# sqrt(4)