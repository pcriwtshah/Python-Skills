# for loop is used to iterate through a sequence like lists, tuple, strings
fruits =["Banana", "Watermelon", "Mango", "Grapes"]
for item in fruits:
    print(item)
print("Done with fruits list using for loop\n")

#range() function
for i in range(8):
    print(i)

print("\n\n")
for i in range(2,8):
    print(i )  

print("\n\n")
for i in range(2,16, 2):
    print(i ) 

# for loop with else
fruits =["Banana", "Watermelon", "Mango", "Grapes"]
for item in fruits:
    print(item)
else:
    print("Done with fruits list using for-else loop\n")
