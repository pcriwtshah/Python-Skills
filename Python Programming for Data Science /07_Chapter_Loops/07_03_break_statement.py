#This program illustrates how to use break. break will aslo work with for loop

fruits =["Banana", "Watermelon", "Mango", "Grapes"]
j = 0
while j<len(fruits):
    print(fruits[j])
    if j == 2:
        break #will not print all items in fruits. when j==2, loop stops
    j += 1

print("Done with lists using while and break\n")


fruits =["Banana", "Watermelon", "Mango", "Grapes"]
j = 0
while j<len(fruits):
    print(fruits[j])
    if j == 2:
        break #will not print all items in fruits. when j==2, loop stops
    j += 1
else: #This part will not execute because while loop didn't complete
    print("Done with lists using while and break\n")