i = 0 #initialize i
while i < 10: #condition if true, body will be executed, otherwise not
    print(i)
    i += 1 #iterate i so that it is in the loop and exits loop when it is false
print("Done printing 0 to 9\n\n")

#This can be better done with for loop; no need to write j += 1
fruits =["Banana", "Watermelon", "Mango", "Grapes"]
j = 0
while j<len(fruits):
    print(fruits[j])
    j += 1
print("Done with lists\n")

# while - else loop
fruits =["Banana", "Watermelon", "Mango", "Grapes"]
j = 0
while j<len(fruits):
    print(fruits[j])
    j += 1
else:
    print("Done with lists using while - else loop\n")