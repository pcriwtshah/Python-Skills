#Some cool stuff you can do with list

'''
List Methods:
list.index()
list.append()
list.extend()
list.insert()
list.remove()
list.count()
list.pop()
list.reverse()
list.sort()
list.copy()
list.clear()
'''
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

#To count the element in the list
#Syntax: list.count(element)
#Return Value: The count() method will return 
# an integer value, i.e., the count of the given 
# element from the given list. It returns a 0 if 
# the value is not found in the given list.
list1 = ['red', 'green', 'blue', 'orange', 'blue', 'green', 'gray', 'green', 'yellow', 'purple', 'yellow', 'blue']
color_count = list1.count('blue')
print('The count of color: blue is ', color_count)

color_count1 = list1.count('green')
print('The count of color: green is ', color_count1)

list1 = [7,3,4,3,9,3,5,6,3]
count3 = list1.count(3)
print('The count of element: 3 is ', count3)
