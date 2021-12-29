a = {1, 3, 5, 7,8} #No repetition items allowed
print(type(a))
print(a)

#Create empty sets
a = {} #This will create empty dictionary not empty sets
print(type(a))
b = set() #This creates empty set
print(type(b))
print(b)

#Add values to empty set
b.add(4)
b.add(5)
print(b)

#Add tuple to the set
b.add((7, 8, 9))
print(b)
#print(b[1]) # set object doesnot support indexing
#b.add({6:7}) # cannot add dictionary to set because it is unhashable
#b.add([12, 13, 14])  # cannot add list to set because it is unhashable

#To find the length of set 
print(len(b))

b.add(6)
b.add(7)
b.add(9)
#To remove an element 
b.remove(4)
print(b)

#print(b.remove(4)) #This will show error
#To remove an arbitrary element
print(b.pop())
'''
#To clear set
print(b.clear()) #This does not work
b.clear()
print(b)
'''

#Find the union of sets
a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(type(a))
print(a.union(b))

#Find the intersection of sets
print(a.intersection(b))
'''
#user input numbers to create set
x = input("Enter 5 numbers: ")
y= {x[0], x[1], x[3], x[4], x[5], x[2]}
print(y)
print(type(y))
'''
#Other way to do this
x1 = int(input("Enter the number 1"))
x2 = int(input("Enter the number 2"))
x3 = int(input("Enter the number 3"))
x4 = int(input("Enter the number 4"))
x5 = int(input("Enter the number 5"))
x6 = int(input("Enter the number 6"))
p = {x1, x2, x3, x4, x5, x6}
print(p)
print(type(p))

#list and dict cannot be the element of the set
#tuple can be the element of the set but cannot be changed because there is no way to access it.
