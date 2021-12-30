'''
2 types of files: txt files and binary files
open() function to open files; Two arguments <file_name> and <mode> are needed to open files.
open("file_name.txt", 'r') # r for read, w for write, a for appending, and + for updating
rb for read in binary mode and rt read in text mode
'''
#This program open the file, read its entire content, and print the content
'''
f = open('09_01_poem.txt', 'r') #open the file; r is default value - no need to mention
#data = f.read() #read the file only once
data = f.read(10) #read the first 10 characters from the file
print(data, "\n")
f.close()  #must close the file

#This program open the file, read its entire content, and print the content

f = open('09_01_poem.txt', 'r') 
#read the first line
data = f.readline() #read one line at a time from the file
print(data, "\n")

#read the second line
data = f.readline() #read one line at a time from the file
print(data, "\n")
f.close()  #must close the file
'''
# To check if a given word is present in a file
f = open('09_01_poem.txt', 'r')
data = f.read()
if 'Twinkle' in data:
    print("Twinkle is present in a file")
else:
    print("Twinkle is not present in a file")
f.close()