for i in range(10):
    if i == 5:
        continue #This loop will not execute when i == 5. Unlike break the loop will continue
    print(i)
else:
    print("Done with for - else loop with continue")

#prints only even numbers
for i in range(10):
    if i%2 == 1:
        continue #This loop will not execute when i == 5. Unlike break the loop will continue
    print(i)
else:
    print("Done with printing even numbers using for - else loop with continue")

#prints only odd numbers
for i in range(10):
    if i%2 == 0:
        continue #This loop will not execute when i == 5. Unlike break the loop will continue
    print(i)
else:
    print("Done with printing odd numbers using for - else loop with continue")