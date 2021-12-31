'''
#This program write the multiplication table for 2 times
for i in range(1,11):
    x = 2*i
    print("2 X", i, "=", x)
print("\n\n")

#This program write multiplication table from 1 times to 10 times
for i in range(1, 11):
    for j in range(1, 11):
        x = i*j
        print(i, "X", j, "=", x)
    print("\n\n")
'''
'''
#This program write the multiplication table for 2 times using while loop
i = 1
while i < 11:
    x = 2*i
    print("2 X", i, "=", x)
    i += 1

#This program write multiplication table from 1 times to 10 times
#This is not working. Find out why?
i = 1
j = 1
while i < 11:
    while j < 11:
        x = i*j
        print(i, "X", j, "=", x)
        j += 1
    i += 1
print("Done")
'''
#Other way to do this
num = int(input("Enter the number\n"))
for i in range(1,11):
    #print(str(num) + "X" + str(i) + "=" + str(i*num))# concatenate str
    print(f"{num}X{i} = {num*i}") #other way to write above statement called fstring
