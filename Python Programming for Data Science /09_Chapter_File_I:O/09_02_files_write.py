#This program will open a file if it exits otherwise it will create a new file and write in ut
'''
f = open('09_02_poem.txt', 'w') #This file 09_02_poem.txt doesn't exit. So it wil be created. If it exits, this syntax will override it.
f.write("This is my poem.\nI don't know how to write poem")
f.close() #Once you open the file, don't forget to close
'''

'''
#This program will open a file and append the texts
f = open('09_02_poem.txt', 'a') 
f.write("\nI am appending this sentence to this file.\nEach time I run the program, each time it will be appended")
f.write("\nI can call this write function as many times as I need before I close the file")
f.close() #Once you open the file, don't forget to close
'''


#open, read, write or append using with statement. Benefit: No need to close the file

with open('09_02_poem.txt', 'r') as f: #doesn't create new file if it doen't exit in r mode
    a = f.read()
print(a)

with open('poem.txt', 'w') as f: # create new file if it doen't exit in w mode or override if it exists
    b = f.write("Hello")
print(b)