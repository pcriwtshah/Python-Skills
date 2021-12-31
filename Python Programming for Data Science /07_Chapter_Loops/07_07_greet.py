#This program greets every students who came to learn Python
'''
student =["Tom", "Harry", "Johny", "Markas", "Franky", "Carl"]
for item in student:
    print("Welcome to learn Python,", item)
'''

#Create an empty list
students = []
num = int(input("How many students are there?"))
for i in range(0, num):
    #x = input("Enter the name of the students: \n") #this also works
    students.append(input("Enter the name of the students: \n")) #add elements to the list
#print(students) #to check if list is created

#Greet all students in the list
for item in students:
    print("Welcome to learn Python,", item)

#Greet Students whose name starts with M
student =["Tom", "Harry", "Johny", "Markas", "Franky", "Carl", "Meghan"]
for name in student:
    if name.startswith("M"):
        print("Hello " + name)
