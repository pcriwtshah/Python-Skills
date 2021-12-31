# Lists are mutable. Create lists using []
a =[2, 4, 5, 7, 8, 12, 13, 14, 15]
#print the list 
print(a)
a[0] = 98 #replaces 0th element in list a
print(a) #print he updated list

#Access the lement using index
print(a[3])

#create a list with elements of different data types
b = [3, 4.32, "harry", {1, 2, 3}]
print(b)

#Create list of objects entered by user
# f1 = input("Enter the fruits numbered 1:\n")
# f2 = input("Enter the fruits numbered 2:\n") #To get two cursor at two locations, press alt +  location
# f3 = input("Enter the fruits numbered 3:\n")
# f4 = input("Enter the fruits numbered 4:\n")
# f5 = input("Enter the fruits numbered 5:\n")
# f6 = input("Enter the fruits numbered 6:\n")
# f7 = input("Enter the fruits numbered 7:\n")
# #to get new line, press command + enter
# fruits_List = [f1, f2, f3, f4, f5, f6, f7]


#Create a list of marks of 6 students and sort it
m1 = input("Enter the marks of students numbered 1:\n")
m2 = input("Enter the marks of students numbered 2:\n") #To get cursors at more than two locations, press alt + shift + location
m3 = input("Enter the marks of students numbered 3:\n")
m4 = input("Enter the marks of students numbered 4:\n")
m5 = input("Enter the marks of students numbered 5:\n")
m6 = input("Enter the marks of students numbered 6:\n")

marks = [m1, m2, m3, m4, m5, m6]
marks.sort()
#print(marks.sort()) # doesn't work
print(marks)
print(sum(a)) # make sure m1,m2 ...m5,m6 are int not strings
print(marks[0]+marks[1]+marks[2])