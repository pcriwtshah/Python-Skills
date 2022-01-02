#Some cool stuff you can do with list

a = [3, 2, 6, 7, 4, 12, 9, 10, 15]
print(a)
a1 = a.sort() # the sorted list will not be assigned to list a1. Instead a will be sorted.
#print(a1)
#a.sort()
print(a)

#To create a sorted list
a1 = a[0:]
a1.sort()
print(a1)

#Reverse the list
b = [3, 2, 6, 7, 4, 12, 9, 10, 15]
b.reverse()
print(b)

#To add an element at the end of the list
b = [3, 2, 6, 7, 4, 12, 9, 10, 15]
b.append(1212)
print(b)

#To add an  element somewhere in the list but not at the end
b.insert(3,121) #at index 3 add 121
print(b)

#To pop out an element fromt he list
b.pop(3) #remove an element at index 3
print(b)

#remove element from the list
b.remove(4)
print(b)

#Look python docs for more methods for list under section 5. Data Structures> 5.1 More on lists


#To add an element at the end of the empty list
x = []
x.append(1212)
print(x)